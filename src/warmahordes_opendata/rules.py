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


class _BaseRule(enum.Flag):
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


class Stat(_BaseRule):
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


class Advantage(_BaseRule):
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


class Immunity(_BaseRule):
    COLD = enum.auto()
    CORROSION = enum.auto()
    ELECTRICITY = enum.auto()
    FIRE = enum.auto()

    def __str__(self):
        return f"Imunity: {self._stringify_name()}"


class WeaponStat(_BaseRule):
    RANGE = enum.auto()
    RATE_OF_FIRE = enum.auto()
    AREA_OF_EFFECT = enum.auto()
    POWER = enum.auto()
    POWER_PLUS_STRENGTH = enum.auto()
    LOCATION = enum.auto()


class WeaponQuality(_BaseRule):
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


class Movement(_BaseRule):
    NORMAL_MOVEMENT = enum.auto()
    ADVANCING = enum.auto()
    AIM = enum.auto()
    FULL_ADVANCE = enum.auto()
    RUN = enum.auto()
    CHARGE = enum.auto()
    ENTERING = enum.auto()
    PUSHED = enum.auto()
    SLAMMED = enum.auto()
    THROWN = enum.auto()
    PLACED = enum.auto()
    REPLACING_MODELS = enum.auto()
    LEAST_DISTURBANCE = enum.auto()


class Combat:
    pass


# Model Statistics

Stat.SPEED.update(
    keyword=_("SPD, Speed"),
    description=_(
        "A model's movement rate. A model moves up to its SPD in inches when making a full advance."
    ),
)

Stat.STRENGTH.update(
    keyword=_("STR, Strengh"),
    description=_(
        "A model's physical strength. STR is used to calculate melee damage."
    ),
)

Stat.MELEE_ATTACK.update(
    keyword=_("MAT, Melee Attack"),
    description=_(
        "A model's skill with melee weapons such as swords and hammers or with natural weapons like fists and teeth. A model uses its MAT when making melee attack rolls."
    ),
)

Stat.RANGED_ATTACK.update(
    keyword=_("RAT, Ranged Attack"),
    description=_(
        "A model's accuracy with ranged weapons such as guns and crossbows or wiith thrown weapons like spears and knives. A model uses its RAT when making ranged attack rolls."
    ),
)

Stat.DEFENSE.update(
    keyword=_("DEF, Defense"),
    description=_(
        "A model's ability to avoid being hit by an attack. A model's size, quickness, skill, and even magical protection all contribute to its DEF. An attack roll must be equal to or greater than the target model's DEF to score a hit against it."
    ),
)

Stat.ARMOR.update(
    keyword=_("ARM, Armor"),
    description=_(
        "A model's ability to resist being damaged. This resistance can come from natural resilience, worn armor, or even magical benefits. A model takes 1 damage point for every point by which a damage roll exceeds its ARM."
    ),
)

Stat.COMMAND.update(
    keyword=_("CMD, Command"),
    description=_(
        "Every model with a CMD stat has a command range equal to its CMD in inches. A model is always completely within its own command range. Models in a unit that are in their unit commander's command range are considered to be in formation."
    ),
)

Stat.FOCUS.update(
    keyword=_("FOCUS, Focus"),
    description=_(
        "A measure of a model's arcane power. Only models with the Focus Manipulation special rule, such as warcasters, have a FOCUS stat. Focus determines a model's control range and beginning focus points. A model uses its FOCUS when making magic attack rolls."
    ),
)

Stat.FURY.update(
    keyword=_("FURY, Fury"),
    description=_(
        "Like FOCUS, FURY is a measure of model's primal arcane power. For warbeasts, FURY indicates how much the beast can be forced. When warbeasts are forced to perform certain actions, they generate fury. Models with the Fury Manipulation ability, such as warlocks, draw on tha tfury to enhance their own abilities. FURY determines a model's control range and beginning fury points, and the model uses its FURY when making magic attack rolls."
    ),
)

Stat.THRESHOLD.update(
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

WeaponStat.RANGE.update(
    keyword=_("RNG, Range"),
    description=_(
        "The maximum distance in inches between the attack's point of origin and the target before the attack will automatically miss. Measure range from the edge of the point of origin's base nearest to the target, up to the maximum range of the attack. Spray attacks use special range descriptors beginning with \"SP\". A RNG of \"CTRL\" indicates the weapon can target any model in the attacking model's control range. Remember, the attacking model needs line of sight to a model to target it. A RNG of \"*\" indicates the model's special rules contain information about determining the RNG. Some special rules can affect a weapon's range. If a weapon's RNG is reduced to 0 or less by some effect, the weapon cannot be used to make attacks."
    ),
)

WeaponStat.RATE_OF_FIRE.update(
    keyword=_("ROF, Rate of Fire"),
    description=_(
        "The number of initial attacks a model can make with this ranged weapon during its activation."
    ),
)

WeaponStat.AREA_OF_EFFECT.update(
    keyword=_("AOE, Area of Effect"),
    description=_(
        "The diameter in inches of the template an area-of-effect (AOE) weapon uses for determining which models are hit by the attack. When using an AOE weapon, center the template on the determined point of impact. All models within the template are affected and potentially suffer the attack's damage and effects. (See p. 51 for detailed rules on AOE attacks."
    ),
)

WeaponStat.POWER.update(
    keyword=_("POW, Power"),
    description=_(
        "The value used when making damage rolls. A weapon or attack marked with a POW of \"—\" does not cause damage. Some special rules can affect a weapon's POW. A weapon's POW can never be reduced to less than 0."
    ),
)

WeaponStat.POWER_PLUS_STRENGTH.update(
    keyword=_("P+S, Power plus Strength"),
    description=_(
        "The P+S value provides the sum of the model's base STR and the melee weapon's POW for quick reference."
    ),
)

WeaponStat.LOCATION.update(
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

# Movement

Movement.NORMAL_MOVEMENT.update(
    keyword=_("Normal Movement"),
    description=_(
        "The first part of a model’s activation is its Normal Movement. Models generally move only during this portion of their activations, though some special rules permit movement at other times.\n\nWhen a model resolves its Normal Movement, it must choose one of the following options:\n  • Forfeit its Normal Movement • Aim\n  • Full advance\n  • Run\n  • Charge\n\nAdditionally some models can choose to perform a power attack encompassing its Normal Movement and Combat Action such as a slam or trample power attack."
    ),
)

Movement.ADVANCING.update(
    keyword=_("Advancing"),
    description=_(
        "Advancing refers to movement a model intentionally makes, not to involuntary movement caused by other effects, such as being pushed or slammed. A model can change its facing at any time during its advance, but when it advances it must always move in the direction it is facing. Make all measurements from the front of an advancing model’s base. Determine the distance a model advances by measuring how far the leading edge of its base travels. The distance moved is absolute. Changing facing by rotating in place is still advancing even though the model’s position on the table does not change. A model’s base cannot pass over another model’s base while advancing. This means that if a gap between the bases of two models is too small for another model’s base to fit between them, the third model cannot move through the space."
    ),
)

Movement.AIM.update(
    keyword=_("Aim"),
    description=_(
        "The model does not advance, not even to change its facing; then its Normal Movement ends. For the rest of the model’s activation, it receives a +2 bonus to every ranged attack roll it makes. A model in melee cannot use its Normal Movement to aim."
    ),
)

Movement.FULL_ADVANCE.update(
    keyword=_("Full Advance"),
    description=_(
        "The model advances up to its current speed (SPD) in inches."
    ),
)

Movement.RUN.update(
    keyword=_("Run"),
    description=_(
        "The model advances up to twice its current speed (SPD) in inches. When a model uses its Normal Movement to run, it must forfeit its Combat Action before advancing and its activation ends as soon as it completes its run movement. A model cannot use its Normal Movement to run after casting a spell or using a feat that activation.\n\nIf a model cannot run due to some effect and is required to use its Normal Movement to run, instead of running it forfeits its Combat Action and makes a full advance, then its activation ends. A model that is required to run for some reason cannot cast spells or use its feat even if it cannot run.\n\nSome models must meet special requirements to run:\n  • A warjack must spend 1 focus point to use its Normal Movement to run.\n  • A warbeast must be forced to use its Normal Movement to run.\n  • A trooper must receive a Press Forward order to use its Normal Movement to run, or it must be compelled to run as a result of a game effect (such as being out of formation). A trooper that receives the Press Forward order must use its Normal Movement to either run or charge."
    ),
)

Movement.CHARGE.update(
    keyword=_("Charge"),
    description=_(
        'The model rushes into melee range with a target and takes advantage of its momentum to make a more powerful first strike. A model that does not have a melee range or cannot make attacks also cannot charge. A model that forfeits its Combat Action cannot use its Normal Movement to charge that activation. A model cannot target a friendly model with a charge.\n\nDeclare a charge and its target before moving the model. A model requires line of sight to another model to target it. After declaring a charge, the charging model turns to face any direction that will bring its target into its melee range when it moves, ignoring terrain, the distance to the charge target, and other models. The charging model then advances up to its current speed (SPD) plus 3" in that direction, in a straight line. The charging model cannot voluntarily stop its movement until its target is in its melee range, but after that point it can end this movement at any time. Once the charging model has the charge target in its melee range, it must keep the charge target in its melee range for the rest of the charge. The charging model stops if it contacts a model, an obstacle, or an obstruction or if it is pushed, slammed, thrown, or placed during its charge movement. If a model contacts a model, an obstacle, or an obstruction while charging but is able to move through it for some reason (such as a special rule on the model), the charging model does not stop but is still considered to have contacted the model, obstacle, or obstruction. At the end of the charge movement, the charging model turns to directly face its target.\n\nSome effects require a model to charge. If a model is required to charge and either it cannot or there are no legal charge targets in its line of sight, the model activates but must forfeit its Normal Movement and Combat Action.\n\nA charging model that is engaging its charge target at the end of its charge movement has made a successful charge. The charging model must use its Combat Action to make either initial melee attacks or a special attack with a melee weapon.\n\nThe charging model’s first melee attack after ending its charge movement must target the model it charged. If the charging model advanced at least 3", its first attack with a melee weapon targeting the model it charged is a charge attack. If that attack hits, the damage roll against the charge target is automatically boosted. After resolving its charge attack, the charging model completes its Combat Action normally.\n\nIf a charging model moved less than 3", its first attack with a melee weapon is not a charge attack. Its first attack must still be made against the charge target, however."If a charging model ends its charge movement without its charge target in its melee range, it has made a failed charge. If a model makes a failed charge during its activation, its activation ends.\n\nSome models must meet special requirements to charge:\n  • A warjack must spend 1 focus point to use its Normal Movement to charge.\n  • A warbeast must be forced to use its Normal Movement to charge.\n  • A trooper must receive the Press Forward order to use its Normal Movement to charge. A trooper that receives the Press Forward order must use its Normal Movement to either run or charge. Troopers in the same unit can charge the same target or multiple targets.\n\nCavalry models have additional rules governing charges.\n\nIf the charging model did not fail its charge and cannot make its first melee attack against the charge target, the charging model can make its first melee attack against another eligible target. In that case, its first melee attack damage roll is not automatically boosted.'
    ),
)

Movement.ENTERING.update(
    keyword=_("Entering"),
    description=_(
        "A model enters an area when it moves from not being within the area to being within the area, when it is put into play in the area, or when it is placed in the area. A model can suffer the effects of entering any particular area only once each time it advances."
    ),
)

Movement.PUSHED.update(
    keyword=_("Pushed"),
    description=_(
        "Sometimes models can be pushed as a result of an attack, a special rule, or a spell. A pushed model moves at half rate through rough terrain, suffers the effects of any hazards through which it moves, and stops if it contacts an obstacle, an obstruction, or another model."
    ),
)

Movement.SLAMMED.update(
    keyword=_("Slammed"),
    description=_(
        "Sometimes models are slammed as a result of a spell or attack. When a model is slammed, it is moved a certain distance directly away from the point of origin of the slam (usually the attacker), then becomes knocked down. The distance the slammed model is moved is determined by the spell or attack that caused the slam. The slammed model then suffers a damage roll determined by the spell or attack that caused the slam. A slammed model moves at half rate through rough terrain, suffers any damaging effects through which it passes, and stops if it contacts an obstacle, an obstruction, or a model with an equal or larger base. A slammed model moves through models with smaller bases than its own.\n\nAdd an additional die to the damage roll the slammed model suffers if it contacts an obstacle, an obstruction, or a model with an equal or larger base.\n\nIf a slammed model contacts a model with an equal or smaller base or moves through a model with a smaller base, the contacted model becomes knocked down and suffers a collateral damage roll determined by the spell or attack that caused the slam. A contacted model with a larger base does not suffer collateral damage and is not knocked down. Resolve any collateral damage simultaneously with the damage resulting from the spell or attack that caused the slam.\n\nIf a slammed model cannot be knocked down it must still forfeit its Normal Movement or Combat Action if it activates later in a turn in which it was slammed."
    ),
)

Movement.THROWN.update(
    keyword=_("Thrown"),
    description=_(
        "Sometimes models are thrown as the result of a spell or attack. When a model is thrown, refer to the spell or attack that caused the throw to determine the model’s point of impact, generally directly away from the attacking model. When resolving a throw power attack, however, it may be necessary to roll for deviation to determine the thrown model’s point of impact. Move the thrown model from its current location in a straight line directly toward the point of impact. During this movement, a thrown model moves through models with smaller bases without contacting them. Unlike when a model is slammed, rough terrain does not affect this movement, but the thrown model still stops if it contacts an obstacle, an obstruction, or a model with an equal or larger base. After moving, the thrown model becomes knocked down and contacts all models with which it is base-to-base and all models whose bases it overlaps. The thrown model then suffers a damage roll determined by the spell or attack that caused the throw.\n\nAdd an additional die to the damage roll the thrown model suffers if it contacts an obstacle, an obstruction, or a model with an equal or larger base.\n\nIf a thrown model contacts a model with an equal or smaller base, the contacted model becomes knocked down and suffers a collateral damage roll determined by the spell or attack that caused the throw. A contacted model with a larger base than the thrown model does not suffer collateral damage and is not knocked down. Resolve any collateral damage simultaneously with the damage resulting from the spell or attack that caused the throw.\n\nIf a thrown model cannot be knocked down it must still forfeit its Normal Movement or Combat Action if it activates later in a turn in which it was thrown."
    ),
)

Movement.PLACED.update(
    keyword=_("Placed"),
    description=_(
        "Sometimes models are placed in a new location as a result of a special rule or spell. Placing a model is not moving or advancing the model. Because a placed model did not advance, it cannot be targeted by free strikes. A model that is placed within an area, however, is considered to enter the area. There must be room for the model’s base in the location the model is placed. A model cannot be placed in impassable terrain or with its base overlapping an obstacle, an obstruction, or another model’s base. The player placing the model chooses its facing.\n\nWhen you are placing a friendly trooper model that is in formation, it must be placed in formation unless it is the unit commander. Unit commanders can be placed without considering formation."
    ),
)

Movement.REPLACING_MODELS.update(
    keyword=_("Replacing Models"),
    description=_(
        "When replacing one model with another, place the new model so the area covered by the smaller of their bases is completely within the area covered by the larger. If the two bases are the same size, place the new model in the same location as the one being replaced. There must be room for the model’s base in the location the model is placed. The player choosing the placed model’s new location chooses its facing."
    ),
)

Movement.LEAST_DISTURBANCE.update(
    keyword=_("Least Disturbance"),
    description=_(
        "Some rules can cause the bases of moving models to overlap those of other models temporarily, such as when a model is thrown or slammed. Once the model has stopped moving, models must be repositioned so that no bases overlap. The model that was moving stays in its final position; other models are moved out of the way to make room. If the model that was moving overlaps the base of a model that cannot be moved, the moving model is repositioned using the rule of least disturbance.\n\nTo determine which models to move and where to move them, first identify the fewest models that would need to be moved to make room. Then find the locations to move them that create the least total distance moved. If multiple options yield the least distance—if one model is centered over another, for example—randomly determine the option to use. A model’s facing does not change when the model is moved as a result of this rule."
    ),
)
