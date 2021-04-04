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

from warmahordes_opendata import themes


class TestThemeForce(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.theme = themes.ThemeForce.find("Magnum Opus")[0]

    def test_type(self):
        self.assertIsInstance(self.theme, themes.ThemeForce)

    def test_repr(self):
        self.assertEqual(
            repr(self.theme),
            "ThemeForce(name='Magnum Opus', factions=['crucible_guard'])",
        )

    def test_name(self):
        self.assertEqual(self.theme.name, "Magnum Opus")

    def test_factions(self):
        self.assertEqual(self.theme.factions, ["crucible_guard"])

    def test_flavor(self):
        self.assertEqual(
            self.theme.flavor,
            "The Crucible Guard has unleashed its standing army in a show "
            "of force that unveils its impressive military innovations and "
            "tactical flexibility. Its highly trained and specialized "
            "soldiers fight in concert with skilled combat alchemists and "
            "support units to push up the field in a haze of alchemical "
            "smoke, backed up by the might of the Golden Crucible's advanced "
            "war machines.\n",
        )

    def test_to_dict(self):
        self.assertEqual(
            list(self.theme.to_dict().keys()),
            [
                "name",
                "factions",
                "flavor",
                "army_composition",
                "requisition_options",
                "special_rules",
            ],
        )
