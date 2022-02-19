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


class Spell(base.SearchableYAMLObject):
    yaml_tag = "!warmahordes_opendata.Spell"

    def __init__(
        self,
        name="",
        description="",
    ):
        super().__init__()

        self.name = name.strip()
        self.description = _(description.strip())

        self.key = self.slugify(name)
        self.title = _(name)

    def __repr__(self):
        return "%s(title='%s', description='%s')" % (
            self.__class__.__name__,
            self.title,
            self.description,
        )

    def to_dict(self):
        return dict(
            name=self.name,
            description=self.description,
        )


Spell.dataset = base.flatten(base.load_dir("data/spells"))
