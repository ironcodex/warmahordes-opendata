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

from importlib import resources
import os

import yaml

ROOT = resources.files("warmahordes_opendata")


def load_dir(*path, root=ROOT):
    root, dirs, files = next(os.walk(os.path.join(root, *path)))
    result = dict()

    dirs.sort()
    for d in dirs:
        result[d] = load_dir(d, root=root)

    files.sort()
    for f in files:
        with open(os.path.join(root, f), "r") as fd:
            data = yaml.safe_load(fd.read())
            result[data.key] = data

    return result


def flatten(tree):
    result = dict()

    for k, v in tree.items():
        if type(v) is dict:
            result.update(flatten(v))
        else:
            result[k] = v

    return result


class BaseYAMLObject(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(**loader.construct_mapping(node))
