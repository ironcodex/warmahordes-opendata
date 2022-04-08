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

import os
from functools import cache
from importlib import resources

import yaml
from slugify import slugify as __slgf

__ROOT = resources.files(__package__)


@cache
def slugify(value):
    return __slgf(value, separator="_", replacements=(("&", "and"),))


def keywords_filter(collection, keywords):
    for word in keywords:
        collection = list(filter(lambda x: word in x, collection))

    return collection


@cache
def load_file(*path, root=__ROOT):
    with open(os.path.join(root, *path), "r") as fd:
        return yaml.safe_load(fd.read())


@cache
def load_dir(*path, root=__ROOT):
    root, dirs, files = next(os.walk(os.path.join(root, *path)))
    result = dict()

    for d in dirs:
        result[d] = load_dir(d, root=root)

    for f in files:
        data = load_file(f, root=root)
        result[data.key] = data

    return result


def flatten(tree, key=None):
    result = dict()

    for k, v in tree.items():
        if type(v) is dict:
            result.update(flatten(v, key))
        elif key is not None:
            result[getattr(v, key)] = v
        else:
            result[k] = v

    return result
