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

from warmahordes_opendata import model
from warmahordes_opendata.dataset import ModelDataset


class TestBaseSize(unittest.TestCase):
    def test_size(self):
        self.assertEqual(model.BaseSize.HUGE, 120)

    def test_str(self):
        self.assertEqual(str(model.BaseSize.EXTRA_LARGE), "Extra Large")


class TestWeaponLocation(unittest.TestCase):
    def test_location(self):
        self.assertEqual(model.WeaponLocation.RIGHT_ARM, "R")

    def test_str(self):
        self.assertEqual(str(model.WeaponLocation.LEFT_ARM), "Left Arm")


class TestWeapon(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.sword = model.Weapon("Sword", model.MeleeWeaponStats(0.5, 3))

        self.carbine = model.Weapon("Carbine", model.RangedWeaponStats(10, 10))

    def test_constructor(self):
        self.assertEqual(self.sword.name, "Sword")
        self.assertEqual(self.sword.stats.rng, 0.5)
        self.assertEqual(self.sword.stats.pow, 3)
        self.assertEqual(self.sword.stats.p_s, True)
        self.assertEqual(self.sword.location, model.WeaponLocation.NONE)

        self.assertEqual(self.carbine.name, "Carbine")
        self.assertEqual(self.carbine.stats.rng, 10)
        self.assertEqual(self.carbine.stats.rof, 1)
        self.assertEqual(self.carbine.stats.aoe, 0)
        self.assertEqual(self.carbine.stats.pow, 10)
        self.assertEqual(self.carbine.location, model.WeaponLocation.NONE)


class TestModel(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.dataset = ModelDataset()
        self.model = self.dataset["Syvestro"][0]

    def test_type(self):
        self.assertIsInstance(self.model, model.Model)

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
        mechanik = self.dataset["cru gua mec"][0]

        self.assertEqual(mechanik.name, "Crucible Guard Mechanik")

    def test_get_by_ppid(self):
        self.assertEqual(self.dataset.get_by_ppid(4142), self.model)

    def test_get_by_alias(self):
        self.assertIsNone(self.dataset.get_by_alias("syvestro"))
        self.assertEqual(self.dataset.get_by_alias("syvestro1"), self.model)
        self.assertEqual(self.dataset.get_by_alias("syvestro 1"), self.model)
        self.assertEqual(self.dataset.get_by_alias("syvestro_1"), self.model)
