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


class BaseSize(enum.IntEnum):
    SMALL = 30
    MEDIUM = 40
    LARGE = 50
    HUGE = 120


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
        self.range = rng
        self.power = pow


class RangedWeaponStats(BaseWeaponStats):
    def __init__(self, rng, pow, rof=1, aoe=0):
        super().__init__(rng, pow)

        self.rof = rof
        self.aoe = aoe


class MeleeWeaponStats(BaseWeaponStats):
    def __init__(self, rng, pow, p_s=True):
        self.range = rng
        self.power = pow
        self.plus_strength = p_s
