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
