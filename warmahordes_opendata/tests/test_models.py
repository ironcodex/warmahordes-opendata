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

import unittest

from warmahordes_opendata import models


class TestModel(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.model = models.Model.find("Syvestro")[0]

    def test_type(self):
        self.assertIsInstance(self.model, models.Model)

    def test_repr(self):
        self.assertEqual(
            repr(self.model),
            "Model(ppid=4142, name='Aurum Adeptus Syvestro', "
            "role='warcaster', factions=['crucible_guard'], scans=4)",
        )

    def test_ppid(self):
        self.assertEqual(self.model.ppid, 4142)

    def test_name(self):
        self.assertEqual(self.model.name, "Aurum Adeptus Syvestro")

    def test_role(self):
        self.assertEqual(self.model.role, "warcaster")

    def test_factions(self):
        self.assertEqual(self.model.factions, ["crucible_guard"])

    def test_scans(self):
        self.assertEqual(self.model.scans, 4)

    def test_to_dict(self):
        self.assertEqual(
            self.model.to_dict(),
            dict(
                ppid=4142,
                name="Aurum Adeptus Syvestro",
                role="warcaster",
                factions=["crucible_guard"],
                scans=4,
            ),
        )

    def test_search(self):
        # Crucible Guard Mechanik
        mechanik = models.Model.find("cru gua mec")[0]

        self.assertEqual(mechanik.name, "Crucible Guard Mechanik")

    def test_get_by_ppid(self):
        self.assertEqual(models.Model.get_by_ppid(4142), self.model)

    def test_get_by_alias(self):
        self.assertIsNone(models.Model.get_by_alias("syvestro"))
        self.assertEqual(models.Model.get_by_alias("syvestro1"), self.model)
        self.assertEqual(models.Model.get_by_alias("syvestro 1"), self.model)
        self.assertEqual(models.Model.get_by_alias("syvestro_1"), self.model)


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
