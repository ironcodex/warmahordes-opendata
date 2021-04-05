#    Copyright 2021 IronCodex
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from warmahordes_opendata import base


class ThemeForce(base.SearchableYAMLObject):
    yaml_tag = "!warmahordes_opendata.ThemeForce"

    def __init__(
        self,
        name="",
        factions=None,
        flavor="",
        army_composition=None,
        requisition_options=None,
        special_rules=None,
    ):
        super().__init__()

        self.name = name.strip()
        self.factions = factions
        self.flavor = flavor.strip()
        self.army_composition = army_composition
        self.requisition_options = requisition_options
        self.special_rules = special_rules

        self.key = self.slugify(self.name)

    def __repr__(self):
        return "%s(name='%s', factions=%s)" % (
            self.__class__.__name__,
            self.name,
            self.factions,
        )

    def to_dict(self):
        return dict(
            name=self.name,
            factions=self.factions,
            flavor=self.flavor,
            army_composition=self.army_composition,
            requisition_options=self.requisition_options,
            special_rules=self.special_rules,
        )

    def fmt_composition(self):
        army_composition = [c["description"] for c in self.army_composition]

        return "\n\n".join(army_composition)

    def fmt_requisition(self):
        requisition_options = [
            o["description"] for o in self.requisition_options
        ]
        return "\n\n".join(requisition_options)

    def fmt_rules(self):
        special_rules = [
            f"{rule['description'].strip()} ({rule['clarification'].strip()})"
            if rule.get("clarification", None)
            else rule["description"].strip()
            for rule in self.special_rules
        ]

        return "\n\n".join(special_rules)


ThemeForce.dataset = base.flatten(base.load_dir("data/themes"))
