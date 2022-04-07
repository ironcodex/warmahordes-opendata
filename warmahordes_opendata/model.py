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
from dataclasses import dataclass, field

import yaml

from warmahordes_opendata import util
from warmahordes_opendata.i18n import _


class BaseYAMLObject(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(**loader.construct_mapping(node))


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


class Spell(BaseYAMLObject):
    yaml_tag = "!warmahordes_opendata.Spell"

    def __init__(
        self,
        name="",
        description="",
    ):
        super().__init__()

        self.name = name.strip()
        self.description = _(description.strip())

        self.key = util.slugify(name)
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


class Model(BaseYAMLObject):
    yaml_tag = "!warmahordes_opendata.Model"

    def __init__(self, ppid=0, name="", role="", factions=None, scans=0, **kwargs):
        super().__init__()

        self.ppid = ppid
        self.name = name.strip()
        self.role = role.strip()
        self.factions = factions
        self.scans = scans

        self.key = util.slugify(self.name)

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


class ThemeForce(BaseYAMLObject):
    yaml_tag = "!warmahordes_opendata.ThemeForce"

    def __init__(
        self,
        name="",
        factions=None,
        flavor="",
        army_composition=None,
        requisition_options=None,
        special_rules=None,
    ):
        super().__init__()

        self.name = name.strip()
        self.factions = factions
        self.flavor = flavor.strip()
        self.army_composition = army_composition
        self.requisition_options = requisition_options
        self.special_rules = special_rules

        self.key = util.slugify(self.name)

    def __repr__(self):
        return "%s(name='%s', factions=%s)" % (
            self.__class__.__name__,
            self.name,
            self.factions,
        )

    def to_dict(self):
        return dict(
            name=self.name,
            factions=self.factions,
            flavor=self.flavor,
            army_composition=self.army_composition,
            requisition_options=self.requisition_options,
            special_rules=self.special_rules,
        )

    def fmt_composition(self):
        army_composition = [c["description"] for c in self.army_composition]

        return "\n\n".join(army_composition)

    def fmt_requisition(self):
        requisition_options = [o["description"] for o in self.requisition_options]
        return "\n\n".join(requisition_options)

    def fmt_rules(self):
        special_rules = [
            f"{rule['description'].strip()} ({rule['clarification'].strip()})"
            if rule.get("clarification", None)
            else rule["description"].strip()
            for rule in self.special_rules
        ]

        return "\n\n".join(special_rules)

    def to_rule(self):
        return Rule(name=self.name, description=self.fmt_rules())


class Scope(enum.Enum):
    CORE = "core"
    MODEL = "model"
    WEAPON = "weapon"


class Rule(BaseYAMLObject):
    yaml_tag = "!warmahordes_opendata.Rule"

    def __init__(
        self,
        scope=Scope.CORE,
        name="",
        abbreviation="",
        description="",
        options=None,
        see_also=None,
    ):
        super().__init__()

        self.scope = Scope(scope)
        self.name = name.strip()
        self.abbreviation = abbreviation.strip()
        self.description = _(description.strip())
        self.options = options
        self.see_also = see_also

        title = f"{self.abbreviation}, {self.name}" if self.abbreviation else self.name

        self.key = util.slugify(title)
        self.title = _(title)

    def __repr__(self):
        return (
            "%s(title='%s', description='%s', see_also=%s)"
            % (
                self.__class__.__name__,
                self.title,
                self.description,
                self.see_also,
            )
            if self.see_also
            else "%s(title='%s', description=%s)"
            % (
                self.__class__.__name__,
                self.title,
                self.description,
            )
        )

    def to_dict(self):
        return dict(
            name=self.name,
            abbreviation=self.abbreviation,
            description=self.description,
            see_also=self.see_also,
        )
