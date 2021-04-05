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
from warmahordes_opendata.i18n import _
from warmahordes_opendata import themes


class Rule(base.SearchableYAMLObject):
    yaml_tag = "!warmahordes_opendata.Rule"

    def __init__(
        self, name="", abbreviation="", description="", see_also=None
    ):
        super().__init__()

        self.name = name.strip()
        self.abbreviation = abbreviation.strip()
        self.description = _(description.strip())
        self.see_also = see_also

        title = (
            f"{self.abbreviation}, {self.name}"
            if self.abbreviation
            else self.name
        )

        self.key = self.slugify(title)
        self.title = _(title)

    def __repr__(self):
        return (
            "%s(title='%s', description='%s', see_also=%s)"
            % (
                self.__class__.__name__,
                self.title,
                self.description,
                self.see_also,
            )
            if self.see_also
            else "%s(title='%s', description=%s)"
            % (
                self.__class__.__name__,
                self.title,
                self.description,
            )
        )

    def to_dict(self):
        return dict(
            name=self.name,
            abbreviation=self.abbreviation,
            description=self.description,
            see_also=self.see_also,
        )


_RULES = base.load_dir("data/rules")
_RULES["theme_forces"] = {
    theme.key: Rule(name=theme.name, description=theme.fmt_rules())
    for theme in themes.ThemeForce.dataset.values()
}

_GROUPS = [g for g in _RULES.keys()]
Rule.dataset = base.flatten(_RULES)
