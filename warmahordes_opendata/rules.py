#    Copyright 2020 IronCodex
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


class Rule(base.SearchableYAMLObject):
    yaml_tag = "!warmahordes_opendata.Rule"

    def __init__(
        self, name="", abbreviation="", description="", see_also=None
    ):
        super().__init__()

        self.title = f"{abbreviation}, {name}" if abbreviation else name
        self.key = self.slugify(self.title)

        self.name = name
        self.abbreviation = abbreviation
        self.description = description
        self.see_also = see_also

    def __repr__(self):
        return (
            "%s(title='%s', description=%s, see_also=%s)"
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
            key=self.key,
            name=self.name,
            abbreviation=self.abbreviation,
            title=self.title,
            description=self.description,
            see_also=self.see_also,
        )


Rule.dataset = base.flatten(base.load_dir("data/rules"))
