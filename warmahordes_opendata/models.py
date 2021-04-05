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

import enum

from warmahordes_opendata import base


class BaseSize(enum.IntEnum):
    SMALL = 30
    MEDIUM = 40
    LARGE = 50
    HUGE = 120


class WeaponType(enum.Enum):
    MELEE = enum.auto()
    RANGED = enum.auto()


class WeaponLocation(enum.Enum):
    NONE = enum.auto()
    LEFT_ARM = enum.auto()
    RIGHT_ARM = enum.auto()
    HEAD = enum.auto()
    SUPERSTRUCTURE = enum.auto()

    def __str__(self):
        return self.name[0]


class BaseWeaponStats:
    def __init__(self, rng, pow):
        self.rng = rng
        self.pow = pow


class RangedWeaponStats(BaseWeaponStats):
    def __init__(self, rng, pow, rof=1, aoe=0):
        super().__init__(rng, pow)

        self.rof = rof
        self.aoe = aoe


class MeleeWeaponStats(BaseWeaponStats):
    def __init__(self, rng, pow, p_s=True):
        super().__init__(rng, pow)

        self.p_s = p_s


class Weapon:
    def __init__(
        self,
        name,
        stats,
        location=WeaponLocation.NONE,
        qualities=[],
        rules=[],
    ):
        self.name = name
        self.stats = stats
        self.location = location
        self.qualities = qualities
        self.rules = rules


class Model(base.SearchableYAMLObject):
    yaml_tag = "!warmahordes_opendata.Model"

    def __init__(self, ppid=0, name="", role="", factions=None, scans=0):
        super().__init__()

        self.ppid = ppid
        self.name = name.strip()
        self.role = role.strip()
        self.factions = factions
        self.scans = scans

        self.key = self.slugify(self.name)

    def __repr__(self):
        return "%s(ppid=%d, name='%s', role='%s', factions=%s, scans=%d)" % (
            self.__class__.__name__,
            self.ppid,
            self.name,
            self.role,
            self.factions,
            self.scans,
        )

    def to_dict(self):
        return dict(
            ppid=self.ppid,
            name=self.name,
            role=self.role,
            factions=self.factions,
            scans=self.scans,
        )


Model.dataset = base.flatten(base.load_dir("data/models"))
