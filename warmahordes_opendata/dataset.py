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

from collections import UserDict

from warmahordes_opendata import model, util


class BaseMemoryDataset(UserDict):
    def __init__(self, data: dict):
        super().__init__(util.flatten(data))

    def __getitem__(self, key) -> list:
        q = util.slugify(key)

        try:
            return [self.data[q]]
        except KeyError:
            return [self.data[k] for k in util.keywords_filter(self, set(q.split("_")))]


class ModelDataset(BaseMemoryDataset):
    def __init__(self):
        models = util.load_dir("data/models")

        super().__init__(models)

        self._ppid_dataset = util.flatten(models, key="ppid")
        self._aliases_dataset = {
            k: self._ppid_dataset[v]
            for k, v in util.load_file("data/model_aliases.yaml").items()
        }

    def get_by_ppid(self, ppid) -> model.Model:
        return self._ppid_dataset.get(ppid)

    def get_by_alias(self, alias) -> model.Model:
        alias = util.slugify(alias)

        try:
            return self._aliases_dataset[alias]
        except KeyError:
            try:
                if alias[-2] != "_":
                    return self._aliases_dataset[f"{alias[:-1]}_{alias[-1]}"]
            except (IndexError, KeyError):
                pass
        return None


class ThemeForceDataset(BaseMemoryDataset):
    def __init__(self):
        super().__init__(util.load_dir("data/themes"))


class RuleDataset(BaseMemoryDataset):
    def __init__(self):
        rules = util.load_dir("data/rules")
        themes = ThemeForceDataset()
        rules["theme_forces"] = {k: v[0].to_rule() for k, v in themes.items()}

        super().__init__(rules)
        self._groups = [g for g in rules]
