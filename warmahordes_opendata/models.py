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

import enum

import yaml


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


class Model:
    def __init__(
        self,
        ppid=0,
        name=None,
        job=None,
        keywords=None,
        factions=None,
        works_for=None,
        battlegroup_points=None,
        point_costs=None,
        field_allowance=None,
        attachments=None,
        scans=0,
    ):
        self.ppid = ppid
        self.name = name
        self.job = job
        self.keywords = keywords
        self.factions = factions
        self.works_for = works_for
        self.battlegroup_points = battlegroup_points
        self.point_costs = point_costs
        self.field_allowance = field_allowance
        self.attachments = attachments
        self.scans = scans

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        def strlist(lst):
            if lst is None:
                return None

            return [str(i) for i in lst]

        model = dict(
            ppid=self.ppid,
            name=self.name,
            job=self.job,
            keywords=strlist(self.keywords),
            factions=strlist(self.factions),
            works_for=strlist(self.works_for),
            battlegroup_points=self.point_costs,
            point_costs=self.point_costs,
            field_allowance=self.field_allowance,
            attachments=self.attachments,
            scans=self.scans,
        )

        return {k: v for k, v in model.items() if v is not None}

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as fd:
            return cls.from_dict(yaml.load(fd, yaml.BaseLoader))
