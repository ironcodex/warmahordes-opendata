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
