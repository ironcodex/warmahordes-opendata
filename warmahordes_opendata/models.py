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

from dataclasses import dataclass
from dataclasses import field
import enum

from warmahordes_opendata import base


class CapitalizedNamesMixin:
    def __str__(self):
        return " ".join((s.capitalize() for s in self.name.split("_")))


class BaseSize(CapitalizedNamesMixin, enum.IntEnum):
    """The physical size and mass of a model (p. 19).

    The physical size and mass of a model are reflected by its base size.
    There are five base sizes: small bases (30 mm), medium bases (40 mm),
    large bases (50 mm), extra large bases (80 mm) and huge bases (120 mm).
    Generally, most human-sized warrior models have small bases; larger
    creatures and light warjacks have medium bases; very large creatures and
    heavy warjacks have large bases; and colossals and massive vehicles,
    like battle engines, have huge bases. An icon indicating base size
    (30, 40, 50, 80, or 120) appears on a model's stat bar.
    """

    SMALL = 30
    MEDIUM = 40
    LARGE = 50
    EXTRA_LARGE = 80
    HUGE = 120


class WeaponLocation(CapitalizedNamesMixin, str, enum.Enum):
    """The location of a weapon in a model.

    The weapon stat bars of warjacks and huge-based models indicate where
    their weapons are located: left arm (L), right arm (R), head (H),
    or superstructure (S).
    When all of a warjack's system boxes for a location have been damaged,
    that system is crippled (see "Crippling Systems," p. 56).
    A weapon that is not in one of these locations is marked with "—".
    """

    NONE = "-"
    LEFT_ARM = "L"
    RIGHT_ARM = "R"
    HEAD = "H"
    SUPERSTRUCTURE = "S"


@dataclass
class WeaponStats:
    rng: float
    pow: int


@dataclass
class RangedWeaponStats(WeaponStats):
    rof: int = 1
    aoe: int = 0


@dataclass
class MeleeWeaponStats(WeaponStats):
    p_s: bool = True


@dataclass
class Weapon:
    name: str
    stats: WeaponStats
    location: WeaponLocation = WeaponLocation.NONE
    qualities: list = field(default_factory=list)
    rules: list = field(default_factory=list)


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

    @staticmethod
    def get_by_ppid(ppid):
        return _PPIDS.get(ppid, None)

    @classmethod
    def get_by_alias(cls, alias):
        alias = cls.slugify(alias)

        try:
            return _ALIASES[alias]
        except KeyError:
            try:
                if alias[-2] != "_":
                    return _ALIASES[f"{alias[:-1]}_{alias[-1]}"]
            except (IndexError, KeyError):
                pass
        return None


_MODELS = base.load_dir("data/models")
_PPIDS = base.flatten(_MODELS, key="ppid")
_ALIASES = {
    k: _PPIDS[v] for k, v in base.load_file("data/model_aliases.yaml").items()
}

Model.dataset = base.flatten(_MODELS)
