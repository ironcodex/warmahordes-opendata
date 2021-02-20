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

from importlib import resources
import os
import unittest

from warmahordes_opendata import models


class TestBaseSize(unittest.TestCase):
    def test_small_base(self):
        self.assertEqual(models.BaseSize.SMALL, 30)

    def test_medium_base(self):
        self.assertEqual(models.BaseSize.MEDIUM, 40)

    def test_large_base(self):
        self.assertEqual(models.BaseSize.LARGE, 50)

    def test_huge_base(self):
        self.assertEqual(models.BaseSize.HUGE, 120)


class TestWeaponLocation(unittest.TestCase):
    def test_right(self):
        self.assertEqual(str(models.WeaponLocation.RIGHT_ARM), "R")

    def test_left(self):
        self.assertEqual(str(models.WeaponLocation.LEFT_ARM), "L")


class TestWeapon(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.sword = models.Weapon("Sword", models.MeleeWeaponStats(0.5, 3))

        self.carbine = models.Weapon(
            "Carbine", models.RangedWeaponStats(10, 10)
        )

    def test_constructor(self):
        self.assertEqual(self.sword.name, "Sword")
        self.assertEqual(self.sword.stats.rng, 0.5)
        self.assertEqual(self.sword.stats.pow, 3)
        self.assertEqual(self.sword.stats.p_s, True)
        self.assertEqual(self.sword.location, models.WeaponLocation.NONE)

        self.assertEqual(self.carbine.name, "Carbine")
        self.assertEqual(self.carbine.stats.rng, 10)
        self.assertEqual(self.carbine.stats.rof, 1)
        self.assertEqual(self.carbine.stats.aoe, 0)
        self.assertEqual(self.carbine.stats.pow, 10)
        self.assertEqual(self.carbine.location, models.WeaponLocation.NONE)


class TestModel(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.model = models.Model.from_file(
            os.path.join(
                resources.files("warmahordes_opendata"),
                "data",
                "models",
                "crucible_guard",
                "warcaster",
                "aurum_adeptus_syvestro.yaml",
            )
        )

    def test_constructor(self):
        self.assertEqual(self.model.name, "Aurum Adeptus Syvestro")
