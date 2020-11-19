# flake8: noqa
import enum
import string

from warmahordes_opendata._i18n import _


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

# Advantages
Advantage.ADVANCE_DEPLOYMENT.update(
    keyword=_("Advance Deployment"),
    description=_("This model can be placed after normal deployment, up to 6\" beyond the established deployment zone."),
)

Advantage.AMPHIBIOUS.update(
    keyword=_("Amphibious"),
    description=_("This model treats shallow water as open terrain while advancing. While completely in shallow water, this model gains concealment and does not block line of sight."),
)

Advantage.ARC_NODE.update(
    keyword=_("Arc Node"),
    description=_("This warjack is a channeler equipped with an arc node and can act as a conduit for spells cast by its warcaster."),
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
    description=_("This model can participate in combined melee attacks with other models in its unit."),
)

Advantage.COMBINED_RANGED_ATTACK.update(
    keyword=_("Combined Ranged Attack"),
    description=_("This model can participate in combined ranged attacks with other models in its unit."),
)

Advantage.CONSTRUCT.update(
    keyword=_("Construct"),
    description=_("This model is a construct and is not a living model."),
)

Advantage.EYELESS_SIGHT.update(
    keyword=_("Eyeless Sight"),
    description=_("This model ignores cloud effects when determining line of sight. This model ignores concealment and Stealth and never suffers Blind."),
)

Advantage.FLIGHT.update(
    keyword=_("Flight"),
    description=_("This model treats all non-impassable terrain as open terrain while advancing. It can advance through obstructions and other models if it has enough movement to move completely past them. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle, an obstruction, or another model. This model ignores intervening models when declaring its charge target. While knocked down or stationary, this model loses Flight."),
)

Advantage.GUNFIGHTER.update(
    keyword=_("Gunfighter"),
    description=_("This model is a gunfighter."),
)

Advantage.INCORPOREAL.update(
    keyword=_("Incorporeal"),
    description=_("This model treats all non-impassable terrain as open terrain while advancing. It can move through obstructions and through other models if it has enough movement to move completely past them. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle, an obstruction, or another model. Other models, including slammed, pushed, or thrown models, can move through this model without effect if they have enough movement to move completely past it. This model does not count as an intervening model. This model is immune to continuous effects and non-magical damage. This model cannot be moved by a push, slam, or throw. When this model makes a melee or ranged attack, before the attack roll is made it loses Incorporeal until the start of its next activation. This model cannot make free strikes while Incorporeal."),
)

Advantage.JACK_MARSHAL.update(
    keyword=_("’Jack Marshal"),
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
    description=_("This model treats rough terrain as open terrain while advancing. While charging, slam power attacking, or trample power attacking, this model does not stop its movement when it contacts an obstacle."),
)

Advantage.SOULLESS.update(
    keyword=_("Soulless"),
    description=_("This living model does not generate a soul token when it is destroyed."),
)

Advantage.STEALTH.update(
    keyword=_("Stealth"),
    description=_("Ranged and magic attacks targeting this model from a point of origin greater than 5\" away automatically miss. This model is not an intervening model when determining line of sight from a model more than 5\" away."),
)

Advantage.TOUGH.update(
    keyword=_("Tough"),
    description=_("When this model is disabled, roll a d6. On a 5 or 6, remove 1 damage point from this model; it is no longer disabled and becomes knocked down. While knocked down, this model loses Tough."),
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

# Weapon Qualities

WeaponQuality.BLESSED.update(
    keyword=_("Blessed"),
    description=_(
        "Attacks with this weapon ignore bonuses from spells, including animi, that add to a model’s ARM or DEF."
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
