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

# flake8: noqa

import enum
import string

from warmahordes_opendata.i18n import _


class _BaseKeyword(enum.Flag):
    def __init__(self, *args, **kwargs):
        self.keyword = str(self)
        self.description = ""
        self.see_also = []

    def _stringify_name(self):
        name = self.name

        name = name.replace("_OF_", "#of ")
        name = name.replace("_PLUS_", "#plus ")

        name = string.capwords(name.replace("_", " "))

        return name.replace("#", " ")

    def __str__(self):
        return self._stringify_name()

    def update(self, keyword, description, see_also=[]):
        self.keyword = keyword
        self.description = description
        self.see_also.extend(see_also)


class ModelStatistic(_BaseKeyword):
    SPEED = enum.auto()
    STRENGTH = enum.auto()
    MELEE_ATTACK = enum.auto()
    RANGED_ATTACK = enum.auto()
    DEFENSE = enum.auto()
    ARMOR = enum.auto()
    COMMAND = enum.auto()
    FOCUS = enum.auto()
    FURY = enum.auto()
    THRESHOLD = enum.auto()


class Advantage(_BaseKeyword):
    ADVANCED_DEPLOYMENT = enum.auto()
    AMPHIBIOUS = enum.auto()
    ARC_NODE = enum.auto()
    ASSAULT = enum.auto()
    CAVALRY = enum.auto()
    COMBINED_MELEE_ATTACK = enum.auto()
    COMBINED_RANGED_ATTACK = enum.auto()
    CONSTRUCT = enum.auto()
    EYELESS_SIGHT = enum.auto()
    FLIGHT = enum.auto()
    GUNFIGHTER = enum.auto()
    INCORPOREAL = enum.auto()
    JACK_MARSHAL = enum.auto()
    OFFICER = enum.auto()
    PARRY = enum.auto()
    PATHFINDER = enum.auto()
    SOULLESS = enum.auto()
    STEALTH = enum.auto()
    TOUGH = enum.auto()
    UNDEAD = enum.auto()


class Immunity(_BaseKeyword):
    COLD = enum.auto()
    CORROSION = enum.auto()
    ELECTRICITY = enum.auto()
    FIRE = enum.auto()

    def __str__(self):
        return f"Imunity: {self._stringify_name()}"


class WeaponStatistic(_BaseKeyword):
    RANGE = enum.auto()
    RATE_OF_FIRE = enum.auto()
    AREA_OF_EFFECT = enum.auto()
    POWER = enum.auto()
    POWER_PLUS_STRENGTH = enum.auto()
    LOCATION = enum.auto()


class WeaponQuality(_BaseKeyword):
    BLESSED = enum.auto()
    BUCKLER = enum.auto()
    CHAIN_WEAPON = enum.auto()
    CONTINUOUS_EFFECT_CORROSION = enum.auto()
    CONTINUOUS_EFFECT_FIRE = enum.auto()
    CRITICAL_CORROSION = enum.auto()
    CRITICAL_DISRUPTION = enum.auto()
    CRITICAL_FIRE = enum.auto()
    DAMAGE_TYPE_COLD = enum.auto()
    DAMAGE_TYPE_CORROSION = enum.auto()
    DAMAGE_TYPE_ELECTRICITY = enum.auto()
    DAMAGE_TYPE_FIRE = enum.auto()
    DAMAGE_TYPE_MAGICAL = enum.auto()
    DISRUPTION = enum.auto()
    OPEN_FIRST = enum.auto()
    SHIELD = enum.auto()
    WEAPON_MASTER = enum.auto()


# Model Statistics

ModelStatistic.SPEED.update(
    keyword=_("SPD, Speed"),
    description=_(
        "A model's movement rate. A model moves up to its SPD in inches when making a full advance."
    ),
)
ModelStatistic.STRENGTH.update(
    keyword=_("STR, Strengh"),
    description=_(
        "A model's physical strength. STR is used to calculate melee damage."
    ),
)
ModelStatistic.MELEE_ATTACK.update(
    keyword=_("MAT, Melee Attack"),
    description=_(
        "A model's skill with melee weapons such as swords and hammers or with natural weapons like fists and teeth. A model uses its MAT when making melee attack rolls."
    ),
)
ModelStatistic.RANGED_ATTACK.update(
    keyword=_("RAT, Ranged Attack"),
    description=_(
        "A model's accuracy with ranged weapons such as guns and crossbows or wiith thrown weapons like spears and knives. A model uses its RAT when making ranged attack rolls."
    ),
)
ModelStatistic.DEFENSE.update(
    keyword=_("DEF, Defense"),
    description=_(
        "A model's ability to avoid being hit by an attack. A model's size, quickness, skill, and even magical protection all contribute to its DEF. An attack roll must be equal to or greater than the target model's DEF to score a hit against it."
    ),
)
ModelStatistic.ARMOR.update(
    keyword=_("ARM, Armor"),
    description=_(
        "A model's ability to resist being damaged. This resistance can come from natural resilience, worn armor, or even magical benefits. A model takes 1 damage point for every point by which a damage roll exceeds its ARM."
    ),
)
ModelStatistic.COMMAND.update(
    keyword=_("CMD, Command"),
    description=_(
        "Every model with a CMD stat has a command range equal to its CMD in inches. A model is always completely within its own command range. Models in a unit that are in their unit commander's command range are considered to be in formation."
    ),
)
ModelStatistic.FOCUS.update(
    keyword=_("FOCUS, Focus"),
    description=_(
        "A measure of a model's arcane power. Only models with the Focus Manipulation special rule, such as warcasters, have a FOCUS stat. Focus determines a model's control range and beginning focus points. A model uses its FOCUS when making magic attack rolls."
    ),
)
ModelStatistic.FURY.update(
    keyword=_("FURY, Fury"),
    description=_(
        "Like FOCUS, FURY is a measure of model's primal arcane power. For warbeasts, FURY indicates how much the beast can be forced. When warbeasts are forced to perform certain actions, they generate fury. Models with the Fury Manipulation ability, such as warlocks, draw on tha tfury to enhance their own abilities. FURY determines a model's control range and beginning fury points, and the model uses its FURY when making magic attack rolls."
    ),
)
ModelStatistic.THRESHOLD.update(
    keyword=_("THR, Threshold"),
    description=_("A measure of a warbeast's ability to resist frenzy."),
)

# Advantages

Advantage.ADVANCED_DEPLOYMENT.update(
    keyword=_("Advance Deployment"),
    description=_(
        'This model can be placed after normal deployment, up to 6" beyond the established deployment zone.'
    ),
)

Advantage.AMPHIBIOUS.update(
    keyword=_("Amphibious"),
    description=_(
        "This model treats shallow water as open terrain while advancing. While completely in shallow water, this model gains concealment and does not block line of sight."
    ),
)

Advantage.ARC_NODE.update(
    keyword=_("Arc Node"),
    description=_(
        "This warjack is a channeler equipped with an arc node and can act as a conduit for spells cast by its warcaster."
    ),
)

Advantage.ASSAULT.update(
    keyword=_("Assault"),
    description=_("This model can make an Assault ranged attack."),
)

Advantage.CAVALRY.update(
    keyword=_("Cavalry"),
    description=_("This model is a cavalry model."),
)

Advantage.COMBINED_MELEE_ATTACK.update(
    keyword=_("Combined Melee Attack"),
    description=_(
        "This model can participate in combined melee attacks with other models in its unit."
    ),
)

Advantage.COMBINED_RANGED_ATTACK.update(
    keyword=_("Combined Ranged Attack"),
    description=_(
        "This model can participate in combined ranged attacks with other models in its unit."
    ),
)

Advantage.CONSTRUCT.update(
    keyword=_("Construct"),
    description=_("This model is a construct and is not a living model."),
)

Advantage.EYELESS_SIGHT.update(
    keyword=_("Eyeless Sight"),
    description=_(
        "This model ignores cloud effects when determining line of sight. This model ignores concealment and Stealth and never suffers Blind."
    ),
)

Advantage.FLIGHT.update(
    keyword=_("Flight"),
    description=_(
        "This model treats all non-impassable terrain as open terrain while advancing. It can advance through obstructions and other models if it has enough movement to move completely past them. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle, an obstruction, or another model. This model ignores intervening models when declaring its charge target. While knocked down or stationary, this model loses Flight."
    ),
)

Advantage.GUNFIGHTER.update(
    keyword=_("Gunfighter"),
    description=_("This model is a gunfighter."),
)

Advantage.INCORPOREAL.update(
    keyword=_("Incorporeal"),
    description=_(
        "This model treats all non-impassable terrain as open terrain while advancing. It can move through obstructions and through other models if it has enough movement to move completely past them. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle, an obstruction, or another model. Other models, including slammed, pushed, or thrown models, can move through this model without effect if they have enough movement to move completely past it. This model does not count as an intervening model. This model is immune to continuous effects and non-magical damage. This model cannot be moved by a push, slam, or throw. When this model makes a melee or ranged attack, before the attack roll is made it loses Incorporeal until the start of its next activation. This model cannot make free strikes while Incorporeal."
    ),
)

Advantage.JACK_MARSHAL.update(
    keyword=_("'Jack Marshal"),
    description=_("This model is a 'jack marshal and can command warjacks."),
)

Advantage.OFFICER.update(
    keyword=_("Officer"),
    description=_("This model is an Officer."),
)

Advantage.PARRY.update(
    keyword=_("Parry"),
    description=_("This model cannot be targeted by free strikes."),
)

Advantage.PATHFINDER.update(
    keyword=_("Pathfinder"),
    description=_(
        "This model treats rough terrain as open terrain while advancing. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle."
    ),
)

Advantage.SOULLESS.update(
    keyword=_("Soulless"),
    description=_(
        "This living model does not generate a soul token when it is destroyed."
    ),
)

Advantage.STEALTH.update(
    keyword=_("Stealth"),
    description=_(
        'Ranged and magic attacks targeting this model from a point of origin greater than 5" away automatically miss. This model is not an intervening model when determining line of sight from a model more than 5" away.'
    ),
)

Advantage.TOUGH.update(
    keyword=_("Tough"),
    description=_(
        "When this model is disabled, roll a d6. On a 5 or 6, remove 1 damage point from this model; it is no longer disabled and becomes knocked down. While knocked down, this model loses Tough."
    ),
)

Advantage.UNDEAD.update(
    keyword=_("Undead"),
    description=_("This model is an undead model and not a living model."),
)

# Immunities

Immunity.COLD.update(
    keyword=_("Immunity: Cold"),
    description=_("This model does not suffer cold damage."),
    see_also=[WeaponQuality.DAMAGE_TYPE_COLD],
)

Immunity.CORROSION.update(
    keyword=_("Immunity: Corrosion"),
    description=_(
        "This model does not suffer corrosion damage and is immune to the Corrosion continuous effect."
    ),
    see_also=[
        WeaponQuality.DAMAGE_TYPE_CORROSION,
        WeaponQuality.CONTINUOUS_EFFECT_CORROSION,
    ],
)

Immunity.ELECTRICITY.update(
    keyword=_("Immunity: Electricity"),
    description=_(
        "This model does not suffer electrical damage. Additionally, when lightning arcs as a result of a special rule, ignore models with Immunity: Electricity when determining which model the lightning arcs to. Lightning cannot arc from a model with Immunity: Electricity."
    ),
    see_also=[WeaponQuality.DAMAGE_TYPE_ELECTRICITY],
)

Immunity.FIRE.update(
    keyword=_("Immunity: Fire"),
    description=_(
        "This model does not suffer fire damage and is immune to the Fire continuous effect."
    ),
    see_also=[
        WeaponQuality.DAMAGE_TYPE_FIRE,
        WeaponQuality.CONTINUOUS_EFFECT_FIRE,
    ],
)

# Weapon Statistics

WeaponStatistic.RANGE.update(
    keyword=_("RNG, Range"),
    description=_(
        "The maximum distance in inches between the attack's point of origin and the target before the attack will automatically miss. Measure range from the edge of the point of origin's base nearest to the target, up to the maximum range of the attack. Spray attacks use special range descriptors beginning with \"SP\". A RNG of \"CTRL\" indicates the weapon can target any model in the attacking model's control range. Remember, the attacking model needs line of sight to a model to target it. A RNG of \"*\" indicates the model's special rules contain information about determining the RNG. Some special rules can affect a weapon's range. If a weapon's RNG is reduced to 0 or less by some effect, the weapon cannot be used to make attacks."
    ),
)

WeaponStatistic.RATE_OF_FIRE.update(
    keyword=_("ROF, Rate of Fire"),
    description=_(
        "The number of initial attacks a model can make with this ranged weapon during its activation."
    ),
)

WeaponStatistic.AREA_OF_EFFECT.update(
    keyword=_("AOE, Area of Effect"),
    description=_(
        "The diameter in inches of the template an area-of-effect (AOE) weapon uses for determining which models are hit by the attack. When using an AOE weapon, center the template on the determined point of impact. All models within the template are affected and potentially suffer the attack's damage and effects. (See p. 51 for detailed rules on AOE attacks."
    ),
)

WeaponStatistic.POWER.update(
    keyword=_("POW, Power"),
    description=_(
        "The value used when making damage rolls. A weapon or attack marked with a POW of \"—\" does not cause damage. Some special rules can affect a weapon's POW. A weapon's POW can never be reduced to less than 0."
    ),
)

WeaponStatistic.POWER_PLUS_STRENGTH.update(
    keyword=_("P+S, Power plus Strength"),
    description=_(
        "The P+S value provides the sum of the model's base STR and the melee weapon's POW for quick reference."
    ),
)

WeaponStatistic.LOCATION.update(
    keyword=_("L/R/H/S, Location"),
    description=_(
        'The weapon stat bars of warjacks and huge-based models indicate where their weapons are located: left arm (L), right arm (R), head (H), or superstructure (S). When all of a warjack\'s system boxes for a location have been damaged, that system is crippled. A weapon that is not in one of these locations is marked with "—."'
    ),
)

# Weapon Qualities

WeaponQuality.BLESSED.update(
    keyword=_("Blessed"),
    description=_(
        "Attacks with this weapon ignore bonuses from spells, including animi, that add to a model's ARM or DEF."
    ),
)

WeaponQuality.BUCKLER.update(
    keyword=_("Buckler"),
    description=_(
        "This weapon has an integral buckler that gives the model a cumulative +1 ARM bonus; for example, a model with two of them gains a bonus of +2 ARM. A model does not gain this bonus while the weapon system with the buckler is crippled or when resolving damage that originates in its back arc."
    ),
)

WeaponQuality.CHAIN_WEAPON.update(
    keyword=_("Chain Weapon"),
    description=_(
        "Attacks with this weapon ignore the Buckler and Shield weapon qualities and Shield Wall."
    ),
)

WeaponQuality.CONTINUOUS_EFFECT_CORROSION.update(
    keyword=_("Continuous Effect: Corrosion"),
    description=_(
        "A model hit by this attack suffers the Corrosion continuous effect."
    ),
)

WeaponQuality.CONTINUOUS_EFFECT_FIRE.update(
    keyword=_("Continuous Effect: Fire"),
    description=_(
        "A model hit by this attack suffers the Fire continuous effect."
    ),
)

WeaponQuality.CRITICAL_CORROSION.update(
    keyword=_("Critical Corrosion"),
    description=_(
        "On a critical hit, the model hit by this attack suffers the Corrosion continuous effect."
    ),
)

WeaponQuality.CRITICAL_DISRUPTION.update(
    keyword=_("Critical Disruption"),
    description=_(
        "On a critical hit on a warjack, the warjack suffers Disruption. A warjack suffering Disruption loses its focus points and cannot channel spells or gain focus by any means, including by being allocated focus, for one round."
    ),
)

WeaponQuality.CRITICAL_FIRE.update(
    keyword=_("Critical Fire"),
    description=_(
        "On a critical hit, the model hit by this attack suffers the Fire continuous effect."
    ),
)

WeaponQuality.DAMAGE_TYPE_COLD.update(
    keyword=_("Damage Type: Cold"),
    description=_("This weapon causes cold damage."),
)

WeaponQuality.DAMAGE_TYPE_CORROSION.update(
    keyword=_("Damage Type: Corrosion"),
    description=_("This weapon causes corrosion damage."),
)

WeaponQuality.DAMAGE_TYPE_ELECTRICITY.update(
    keyword=_("Damage Type: Electricity"),
    description=_("This weapon causes electrical damage."),
)

WeaponQuality.DAMAGE_TYPE_FIRE.update(
    keyword=_("Damage Type: Fire"),
    description=_("This weapon causes fire damage."),
)

WeaponQuality.DAMAGE_TYPE_MAGICAL.update(
    keyword=_("Damage Type: Magical"),
    description=_("This weapon causes magical damage."),
)

WeaponQuality.DISRUPTION.update(
    keyword=_("Disruption"),
    description=_(
        "A warjack hit by this attack loses its focus points and cannot channel spells or gain focus by any means, including by being allocated focus, for one round."
    ),
)

WeaponQuality.OPEN_FIRST.update(
    keyword=_("Open Fist"),
    description=_(
        "This weapon is an Open Fist. A warjack can use a weapon with an Open Fist to make some power attacks."
    ),
)

WeaponQuality.SHIELD.update(
    keyword=_("Shield"),
    description=_(
        "This weapon is a shield that gives the model a cumulative +2 ARM bonus; for example, a model with two of them gains a bonus of +4 ARM. A model does not gain this bonus while the weapon system with the shield is crippled or when resolving damage that originates in its back arc."
    ),
)

WeaponQuality.WEAPON_MASTER.update(
    keyword=_("Weapon Master"),
    description=_(
        "When attacking with this weapon, add an additional die to its damage rolls."
    ),
)
