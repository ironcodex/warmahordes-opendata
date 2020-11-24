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
        name = name.replace("_AND_", "#and ")
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
    LEAST_DISTURBANCE = enum.auto()
    PLACED = enum.auto()
    REPLACING_MODELS = enum.auto()


class Combat(_BaseRule):
    BACK_STRIKE = enum.auto()
    ENGAGED_AND_ENGAGING = enum.auto()
    FREE_STRIKE = enum.auto()
    POWER_ATTACKS = enum.auto()
    HEAD_BUTT = enum.auto()
    POWER_STRIKE = enum.auto()
    SLAM = enum.auto()
    SWEEP = enum.auto()
    THROW = enum.auto()
    TRAMPLE = enum.auto()
    CONCEALMENT_AND_COVER = enum.auto()
    TARGET_IN_MELEE = enum.auto()
    KNOCKDOWN = enum.auto()
    STATIONARY = enum.auto()


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
    description=_(
        "This model can make an Assault ranged attack.\n\nA model with the Assault advantage can make one ranged attack as part of a charge during its activation. This ranged attack must occur after the model ends its movement but before it begins its Combat Action and must target the model charged. A model that begins a charge in melee cannot make an Assault ranged attack as part of that charge. If the target is not in the charging model's melee range after ending its movement, the charge fails, but the model with Assault can still make the Assault ranged attack before its activation ends. A model can make an Assault ranged attack while in melee."
    ),
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
    description=_(
        "This model is a gunfighter.\n\nA model with the Gunfighter advantage can make ranged attacks targeting models in its melee range and/or can target models engaging it. A model with the Gunfighter advantage can also make free strikes with ranged weapons. If it does not have a melee weapon, it gains a melee range of 0.5\".\n\nA model with the Gunfighter advantage can make charges. If it makes a charge, the model can make its initial attacks with its ranged weapons, but these attacks can target only models in its melee range. The charging gunfighter's first melee or ranged attack after ending its charge movement must target the model it charged. If the charging gunfighter did not fail its charge and cannot make its first melee or ranged attack against the charge target, the charging gunfighter can make its first attack against any eligible target. Remember, your first attack after charging is a charge attack only if you make it with a melee weapon, and a model in melee cannot aim.\n\nGunfighter does not allow a model to make melee and ranged attacks during the same activation."
    ),
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
        "The diameter in inches of the template an area-of-effect (AOE) weapon uses for determining which models are hit by the attack. When using an AOE weapon, center the template on the determined point of impact. All models within the template are affected and potentially suffer the attack's damage and effects."
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
        "The first part of a model's activation is its Normal Movement. Models generally move only during this portion of their activations, though some special rules permit movement at other times.\n\nWhen a model resolves its Normal Movement, it must choose one of the following options:\n  • Forfeit its Normal Movement • Aim\n  • Full advance\n  • Run\n  • Charge\n\nAdditionally some models can choose to perform a power attack encompassing its Normal Movement and Combat Action such as a slam or trample power attack."
    ),
)

Movement.ADVANCING.update(
    keyword=_("Advancing"),
    description=_(
        "Advancing refers to movement a model intentionally makes, not to involuntary movement caused by other effects, such as being pushed or slammed. A model can change its facing at any time during its advance, but when it advances it must always move in the direction it is facing. Make all measurements from the front of an advancing model's base. Determine the distance a model advances by measuring how far the leading edge of its base travels. The distance moved is absolute. Changing facing by rotating in place is still advancing even though the model's position on the table does not change. A model's base cannot pass over another model's base while advancing. This means that if a gap between the bases of two models is too small for another model's base to fit between them, the third model cannot move through the space."
    ),
)

Movement.AIM.update(
    keyword=_("Aim"),
    description=_(
        "The model does not advance, not even to change its facing; then its Normal Movement ends. For the rest of the model's activation, it receives a +2 bonus to every ranged attack roll it makes. A model in melee cannot use its Normal Movement to aim."
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
        'The model rushes into melee range with a target and takes advantage of its momentum to make a more powerful first strike. A model that does not have a melee range or cannot make attacks also cannot charge. A model that forfeits its Combat Action cannot use its Normal Movement to charge that activation. A model cannot target a friendly model with a charge.\n\nDeclare a charge and its target before moving the model. A model requires line of sight to another model to target it. After declaring a charge, the charging model turns to face any direction that will bring its target into its melee range when it moves, ignoring terrain, the distance to the charge target, and other models. The charging model then advances up to its current speed (SPD) plus 3" in that direction, in a straight line. The charging model cannot voluntarily stop its movement until its target is in its melee range, but after that point it can end this movement at any time. Once the charging model has the charge target in its melee range, it must keep the charge target in its melee range for the rest of the charge. The charging model stops if it contacts a model, an obstacle, or an obstruction or if it is pushed, slammed, thrown, or placed during its charge movement. If a model contacts a model, an obstacle, or an obstruction while charging but is able to move through it for some reason (such as a special rule on the model), the charging model does not stop but is still considered to have contacted the model, obstacle, or obstruction. At the end of the charge movement, the charging model turns to directly face its target.\n\nSome effects require a model to charge. If a model is required to charge and either it cannot or there are no legal charge targets in its line of sight, the model activates but must forfeit its Normal Movement and Combat Action.\n\nA charging model that is engaging its charge target at the end of its charge movement has made a successful charge. The charging model must use its Combat Action to make either initial melee attacks or a special attack with a melee weapon.\n\nThe charging model\'s first melee attack after ending its charge movement must target the model it charged. If the charging model advanced at least 3", its first attack with a melee weapon targeting the model it charged is a charge attack. If that attack hits, the damage roll against the charge target is automatically boosted. After resolving its charge attack, the charging model completes its Combat Action normally.\n\nIf a charging model moved less than 3", its first attack with a melee weapon is not a charge attack. Its first attack must still be made against the charge target, however.\n\nIf a charging model ends its charge movement without its charge target in its melee range, it has made a failed charge. If a model makes a failed charge during its activation, its activation ends.\n\nSome models must meet special requirements to charge:\n  • A warjack must spend 1 focus point to use its Normal Movement to charge.\n  • A warbeast must be forced to use its Normal Movement to charge.\n  • A trooper must receive the Press Forward order to use its Normal Movement to charge. A trooper that receives the Press Forward order must use its Normal Movement to either run or charge. Troopers in the same unit can charge the same target or multiple targets.\n\nCavalry models have additional rules governing charges.\n\nIf the charging model did not fail its charge and cannot make its first melee attack against the charge target, the charging model can make its first melee attack against another eligible target. In that case, its first melee attack damage roll is not automatically boosted.'
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
        "Sometimes models are thrown as the result of a spell or attack. When a model is thrown, refer to the spell or attack that caused the throw to determine the model's point of impact, generally directly away from the attacking model. When resolving a throw power attack, however, it may be necessary to roll for deviation to determine the thrown model's point of impact. Move the thrown model from its current location in a straight line directly toward the point of impact. During this movement, a thrown model moves through models with smaller bases without contacting them. Unlike when a model is slammed, rough terrain does not affect this movement, but the thrown model still stops if it contacts an obstacle, an obstruction, or a model with an equal or larger base. After moving, the thrown model becomes knocked down and contacts all models with which it is base-to-base and all models whose bases it overlaps. The thrown model then suffers a damage roll determined by the spell or attack that caused the throw.\n\nAdd an additional die to the damage roll the thrown model suffers if it contacts an obstacle, an obstruction, or a model with an equal or larger base.\n\nIf a thrown model contacts a model with an equal or smaller base, the contacted model becomes knocked down and suffers a collateral damage roll determined by the spell or attack that caused the throw. A contacted model with a larger base than the thrown model does not suffer collateral damage and is not knocked down. Resolve any collateral damage simultaneously with the damage resulting from the spell or attack that caused the throw.\n\nIf a thrown model cannot be knocked down it must still forfeit its Normal Movement or Combat Action if it activates later in a turn in which it was thrown."
    ),
)

Movement.LEAST_DISTURBANCE.update(
    keyword=_("Least Disturbance"),
    description=_(
        "Some rules can cause the bases of moving models to overlap those of other models temporarily, such as when a model is thrown or slammed. Once the model has stopped moving, models must be repositioned so that no bases overlap. The model that was moving stays in its final position; other models are moved out of the way to make room. If the model that was moving overlaps the base of a model that cannot be moved, the moving model is repositioned using the rule of least disturbance.\n\nTo determine which models to move and where to move them, first identify the fewest models that would need to be moved to make room. Then find the locations to move them that create the least total distance moved. If multiple options yield the least distance—if one model is centered over another, for example—randomly determine the option to use. A model's facing does not change when the model is moved as a result of this rule."
    ),
)

Movement.PLACED.update(
    keyword=_("Placed"),
    description=_(
        "Sometimes models are placed in a new location as a result of a special rule or spell. Placing a model is not moving or advancing the model. Because a placed model did not advance, it cannot be targeted by free strikes. A model that is placed within an area, however, is considered to enter the area. There must be room for the model's base in the location the model is placed. A model cannot be placed in impassable terrain or with its base overlapping an obstacle, an obstruction, or another model's base. The player placing the model chooses its facing.\n\nWhen you are placing a friendly trooper model that is in formation, it must be placed in formation unless it is the unit commander. Unit commanders can be placed without considering formation."
    ),
)

Movement.REPLACING_MODELS.update(
    keyword=_("Replacing Models"),
    description=_(
        "When replacing one model with another, place the new model so the area covered by the smaller of their bases is completely within the area covered by the larger. If the two bases are the same size, place the new model in the same location as the one being replaced. There must be room for the model's base in the location the model is placed. The player choosing the placed model's new location chooses its facing."
    ),
)

# Combat

Combat.BACK_STRIKE.update(
    keyword=_("Back Strike"),
    description=_(
        "A back strike grants a +2 bonus to the attack roll of a melee, ranged, or magic attack. For a model to receive the back strike bonus, the point of origin of the attack must be completely in the back arc of the target of the attack."
    ),
)

Combat.ENGAGED_AND_ENGAGING.update(
    keyword=_("Engaged & Engaging"),
    description=_(
        "When a model is within an enemy model's melee range and in that model's line of sight, it is engaged. When a model has an enemy model in its melee range and line of sight, it is engaging that model. When a model is either engaged or engaging, it is in melee, which prevents it from making ranged attacks."
    ),
)

Combat.FREE_STRIKE.update(
    keyword=_("Free Strike"),
    description=_(
        "When an engaged model advances out of an enemy's melee range or line of sight, the enemy model can make a free strike against it just before it leaves. The model makes one normal melee attack with any melee weapon that has sufficient melee range to reach the moving model and gains a +2 bonus to its attack roll. If the attack hits, the damage roll is boosted.\n\nWhen the free strike is made treat the free striking model as being in the advancing model's back arc. Free strikes do not benefit from the back strike bonus.\n\nWhen a model with the Gunfighter advantage makes a free strike with a ranged weapon, it only gains the +2 to hit bonus against the model targeted by the attack. Likewise, if the attack hits, the damage roll against the model targeted by the free strike attack is boosted."
    ),
)

Combat.POWER_ATTACKS.update(
    keyword=_("Power Attacks"),
    description=(
        "Power attacks are attack options available to some models, such as warjacks and warbeasts. The power attacks available to other models are described in their special rules. Warjacks and warbeasts can make power attacks as follows.\n  • Lesser warbeasts cannot make power attacks.\n  • A light warjack or warbeast can make head-butt and slam power attacks. A light warjack with at least one non-crippled weapon with the Open Fist weapon quality can make throw power attacks. A light warbeast with at least one weapon with the Open Fist weapon quality can make throw power attacks.\n  • A heavy warjack or warbeast can make head-butt, slam, and trample power attacks. A heavy warjack with at least one non-crippled weapon with the Open Fist weapon quality can make throw power attacks. A heavy warbeast with at least one weapon with the Open Fist weapon quality can make throw power attacks.\n  • A colossal or gargantuan can make head-butt, slam, and trample power attacks. A colossal with at least one non-crippled melee weapon that has a location of L or R can make sweep power attacks. A colossal with at least one non- crippled weapon with the Open Fist weapon quality can make power strike and throw power attacks. A gargantuan with at least one melee weapon that has a location of L or R can make sweep power attacks. A gargantuan with at least one weapon with the Open Fist weapon quality can make power strike and throw power attacks.\n\nA warjack must spend 1 focus point to make a power attack. A warbeast must be forced to make a power attack.\n\nUnless otherwise noted, a model can make a power attack only during its activation. A model cannot make a power attack during an activation in which it charges. A model cannot target a friendly model with a power attack.\n\nWhen a model makes a power attack, do not apply the special rules on its weapons unless they specifically reference power attacks.\n\nA model that is able to do so can make additional melee attacks after making a power attack. A model cannot make a power attack as an additional attack."
    ),
)

Combat.HEAD_BUTT.update(
    keyword=_("Head-Butt"),
    description=_(
        'A model making a head-butt power attack smashes its head into a model to drive it to the ground. A head-butt power attack made by a colossal or gargantuan has a 2" melee range. A head-butt power attack made by any other model has a 0.5 melee range. The attacking model makes a melee attack roll against its target. If the attack hits, the target becomes knocked down and then suffers a power attack damage roll.\n\nA model cannot head-butt a model with a larger base.'
    ),
)

Combat.POWER_STRIKE.update(
    keyword=_("Power Strike"),
    description=_(
        "Only colossals and gargantuans can make power strikes.\n\nA model making a power strike power attack uses the force of its tremendous melee power to send a smaller-based model flying. A model must have at least one non-crippled weapon with the Open Fist weapon quality to make a power strike power attack. The power strike power attack has a melee range equal to that weapon's melee range. Its target must be in the Open Fist's field of fire and have a smaller base than the colossal or gargantuan.\n\nThe attacking model makes a melee attack against the target. If the attack hits, the target is slammed d6 + 2 directly away from the colossal or gargantuan and suffers a power attack damage roll."
    ),
)

Combat.SLAM.update(
    keyword=_("Slam"),
    description=_(
        'A model making a slam power attack rams a model with the full force of its body to send the target model flying backward and knock it to the ground. A slam combines a model\'s Normal Movement and Combat Action. A model cannot make a slam power attack if it forfeited either its Normal Movement or its Combat Action that activation.\n\nA slam power attack made by a colossal or gargantuan has a 2" melee range. A slam power attack made by any other model has a 0.5" melee range.\n\nA model making a slam power attack during its activation can attempt to slam any model that is in its line of sight at the beginning of its Normal Movement. Declare a slam and its target before moving the slamming model. Remember, a model requires line of sight to another model to target it. After declaring a slam, turn the slamming model to directly face the slam target. The slamming model then advances its full SPD plus 3" directly toward its target. The slamming model cannot voluntarily stop its movement unless its target is in its melee range, but it can end this movement at any point with its target in its slam power attack\'s melee range. It stops if it contacts a model, an obstacle, or an obstruction or if it is pushed, slammed, thrown, or placed during its slam movement. If a model contacts a model, an obstacle, or an obstruction while moving as part of a slam power attack but is able to move through it for some reason, the slamming model does not stop but is still considered to have contacted the model, obstacle, or obstruction.\n\nThe slamming model cannot change its facing after advancing as part of a slam.\n\nA slamming model that ends its slam movement with its target in the melee range of its slam power attack has made a successful slam. If the slamming model advanced at least 3", it makes a melee attack roll against its target. A model that slam power attacks a model with a larger base suffers –2 to its attack roll. If the attack hits, the target is slammed d6" directly away from the attacker, becomes knocked down, and then suffers a power attack damage roll.\n\nIf the slamming model has a smaller base than the model it slammed, the slammed model is slammed half the distance rolled.\n\nSmaller-based models hit by a slam power attack made by a huge-based model are moved an additional 2".\n\nIf a slamming model makes a successful slam but moved less than 3", the model still makes an attack roll against its target. If the target is hit, it suffers a power attack damage roll but is not slammed. These are still slam attack rolls and slam damage rolls.\n\nA model that does not end its slam movement with its target within its slam melee range has failed its slam power attack. If a model fails its slam power attack during its activation, its activation ends.'
    ),
)

Combat.SWEEP.update(
    keyword=_("Sweep"),
    description=_(
        "A colossal or gargantuan can use its arms to scythe through models within its reach. A colossal or gargantuan chooses a non-crippled melee weapon with a location of L or R to make the sweep power attack. It then makes one melee attack with the weapon against each model in the weapon's field of fire that is within the weapon's melee range, ignoring intervening models when determining line of sight. This power attack does not require a target, but each separate attack does. These attacks are simultaneous. Models hit suffer a power attack damage roll."
    ),
)

Combat.THROW.update(
    keyword=_("Throw"),
    description=_(
        "A model making a throw power attack picks up and throws another model. A warjack must have at least one non-crippled weapon with the Open Fist weapon quality to make a throw power attack. A warbeast must have at least one weapon with the Open Fist weapon quality to make a throw power attack. A throw power attack has a melee range equal to the melee range of its non-crippled weapon with Open Fist. A model cannot throw power attack a model with a larger base; that is, a model with a larger base cannot be targeted.\n\nThe attacking model must first attempt to grasp the model it intends to throw by making a melee attack roll against it. If the attack hits, that model is grasped and tries to break free before it is lifted off the ground. Both models roll a d6 and add their current STR. An attacker with two non-crippled weapons with Open Fist rolls 2d6 instead. If the grasped model's total is greater, it breaks free and the attack ends. If the attacker's total equals or exceeds the grasped model's total, the grasped model is thrown.\n\nWhen your model throws another model, you can choose either to throw the model directly away from the attacker or to throw it at another model within the attacker's line of sight. The throw distance is equal to half the attacker's current STR in inches.\n\nIf you choose to have your model throw a model at another model, ignore the model being thrown when determining line of sight to the target. The target can have a larger base than the attacker. If the distance between the thrown model and the model it is being thrown at is beyond the throw distance, the point of impact is the point along the line from the thrown model to the model it is being thrown at equal to the throw distance. In this case, do not roll deviation. If the other model is within the throw distance, the attacker makes a melee attack roll against it. On a hit, move the thrown model from its current location directly toward the other model's base until it contacts the target.\n\nIf the target was in the throw range and the attack roll resulted in a miss, determine the thrown model's actual point of impact by rolling for deviation. Referencing the deviation rules, roll a d6 for direction and a d3 for distance in inches. Measure deviation from the center of the missed model's base. The deviation distance cannot exceed half the distance between the thrown model and the model that was missed.\n\nWhen moving the thrown model, it moves through the throwing model without contacting it.\n\nThe thrown model suffers a power attack damage roll."
    ),
)

Combat.TRAMPLE.update(
    keyword=_("Trample"),
    description=_(
        "A model making a trample power attack crashes its way through small-based models in its path. A trample combines a model's Normal Movement and Combat Action. A model cannot make a trample power attack if it forfeited either its Normal Movement or its Combat Action.\n\nDeclare a trample power attack at the beginning of the model's Normal Movement. Choose a direction in which you wish to trample, and turn the model to face that direction. The model then advances up to its current SPD plus 3\" in a straight line in that direction. It moves through any small-based model in its path, but there must be room for the trampling model's base at the end of the movement. It stops if it contacts a model with a medium or larger base, an obstacle, or an obstruction. If a model contacts a model with a medium or larger base, an obstacle, or an obstruction while moving as part of a trample power attack but is able to move through it for some reason, the trampling model does not stop but is still considered to have contacted the model, obstacle, or obstruction. The trampling model cannot change its facing during or after this movement. Do not resolve free strikes against the trampling model during this movement.\n\nAfter the model has finished its trample movement, it makes a melee attack roll against each small-based model it moved through during this movement. Models hit by a trample attack suffer a power attack damage roll. These attacks are simultaneous. When a trampling model hits a model with a Buckler or a Shield or while a model is benefiting from the Shield Wall order, the hit model gains the shield, buckler, or Shield Wall ARM bonus only if the trampling model first contacted the model through its front arc. A trampling model gains a back strike bonus against a model only if the trampling model was completely in that model's back arc when it first contacted that model.\n\nResolve free strikes against the trampling model after resolving all trample attacks. Small-based models contacted by the trampling model during its trample movement cannot make free strikes against the trampling model. Wait to resolve free strikes against the trampling model until after resolving all trample attacks. Ignore the distance between models when resolving free strikes against the trampling model; if a model was eligible to make a free strike against the trampling model during the trampling model's movement, it can do so whether or not the trampling model ended its movement in the eligible model's melee range."
    ),
)

Combat.CONCEALMENT_AND_COVER.update(
    keyword=_("Concealment & Cover"),
    description=_(
        'Terrain features, spells, and other effects can make it more difficult to hit a model with a ranged or magic attack. A model within 1" of an intervening terrain feature can gain either a concealment bonus or a cover bonus—depending on the type of terrain—to its DEF against ranged and magic attacks. If you can draw a line from any part of the attacker\'s volume to any part of the target model\'s volume and that line passes through a terrain feature, that terrain feature is intervening. Concealment and cover bonuses are not cumulative with themselves or each other, but they are cumulative with other effects that modify a model\'s DEF. In order to benefit from concealment or cover, the target model must be within 1" of that terrain feature along at least one straight line between it and the attacker. See “Terrain” on p. 86 for details on terrain features and how they provide concealment or cover.\n\nA model with concealment, either granted by being within 1" of a terrain feature that provides concealment in relation to its attacker or from another effect, gains +2 DEF against ranged and magic attack rolls. Concealment provides no benefit against spray attacks. Examples of concealment- granting terrain features include low hedges and bushes.\n\nA model with cover, granted either by being within 1" of a terrain feature that provides cover in relation to its attacker or from another effect, gains +4 DEF against ranged and magic attack rolls. Cover provides no benefit against spray attacks. Examples of cover-granting terrain features include stone walls, giant boulders, and buildings.\n\nRemember, huge-based models never gain the DEF bonuses from concealment or cover.'
    ),
)

Combat.TARGET_IN_MELEE.update(
    keyword=_("Targeting a Model in Melee"),
    description=_(
        "A large-or-smaller-based model in melee gains +4 DEF against non-spray ranged and magic attacks. Huge-based models never gain the Target in Melee DEF bonus.\n\nIgnore the target-in-melee DEF bonus when the point of origin of the ranged or magic attack is in melee with the model the attack roll is being made against."
    ),
)

Combat.KNOCKDOWN.update(
    keyword=_("Knockdown"),
    description=_(
        "Some attacks and special rules cause a model to become knocked down. While knocked down, a model does not have a melee range and cannot advance, make special actions, make attacks, cast spells, use feats, or be used to channel a spell. A knocked down model does not engage other models and cannot be engaged by them. As a consequence, a model is never in melee with a knocked down model. A melee attack against a knocked down model automatically hits. A knocked down model has a base DEF of 5. A knocked down model does not block line of sight and is never an intervening model.\n\nA knocked down model can stand up at the start of its next activation unless it became knocked down during its controller's turn. In that case it cannot stand up until its controller's next turn, even if it has not yet activated this turn. A model cannot stand up during a turn it was knocked down. Knockdown is not cumulative; a model cannot become knocked down while it is knocked down.\n\nEXAMPLE: A model becomes knocked down during your opponent's turn, and before it gets a chance to stand up it is affected by an attack that would normally cause it to be knocked down. It is not affected by the second instance of knockdown, so it can still stand up on your turn.\n\nTo stand up, a knocked down model forfeits either its Normal Movement or its Combat Action. A model that forfeits its Combat Action to stand can use its Normal Movement to make a full advance but cannot run, charge, or perform a slam or trample power attack that activation. When a model stands, it ceases to be knocked down."
    ),
)

Combat.STATIONARY.update(
    keyword=_("Stationary"),
    description=_(
        "Some attacks and special rules cause a model to become stationary. While stationary a model does not have a melee range and cannot advance, make special actions, make attacks, cast spells, use feats, be used to channel a spell, or give orders. A stationary model does not engage other models and cannot be engaged by them. As a consequence, a model is never in melee with a stationary model. A melee attack against a stationary model automatically hits. A stationary model has a base DEF of 5."
    ),
)
