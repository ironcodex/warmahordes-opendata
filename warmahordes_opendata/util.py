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
def slugify(text: str) -> str:
    """Makes a slug from the given text"""
    return __slgf(text, separator="_", replacements=(("&", "and"),))


def keywords_filter(collection: list, keywords: list) -> list:
    """Filters a list of elements based on a list of keywords.

    :param collection: The collection to be filtered.
    :param keywords: A list of keywords to be used when fitering the collection.

    :returns: A list composed of all elements in the original collection that
    contain all required keywords.
    """
    for word in keywords:
        collection = list(filter(lambda x: word in x, collection))

    return collection


@cache
def load_file(*path: tuple, root: str = __ROOT) -> yaml.YAMLObject:
    """Loads a yaml file using yaml.safe_load.

    :param path: Relative path to the yaml file.
    :param root: Where the relative path should start from, defaults to package path.

    :returns: An object of the class mapped in the yaml file.
    """
    with open(os.path.join(root, *path), "r") as fd:
        return yaml.safe_load(fd.read())


@cache
def load_dir(*path: tuple, root: str = __ROOT) -> dict:
    """Loads all yaml files recursively under a specific path.

    :param path: Relative path to the starting directory.
    :param root: Where the relative path should start from, defaults to package path.

    :returns: A dictionary with the content of all yaml files found. Sub directories
              and file names are part of the dictionary's structure matching the file
              system tree.
    """
    root, dirs, files = next(os.walk(os.path.join(root, *path)))
    result = dict()

    for d in dirs:
        result[d] = load_dir(d, root=root)

    for f in files:
        data = load_file(f, root=root)
        result[data.key] = data

    return result


def flatten(tree: dict, key: str = "") -> dict:
    """Flattens a multi level dictionary tree to a single level.

    :param tree: The dictionary to be flattened.
    :param key: An attribute name in the leaf object to be used as the new key.

    :returns: A dictionary contains all leaf elements found recursively in the tree.
    """
    result = dict()

    for k, v in tree.items():
        if type(v) is dict:
            result.update(flatten(v, key))
        else:
            result[getattr(v, key) if key else k] = v

    return result
