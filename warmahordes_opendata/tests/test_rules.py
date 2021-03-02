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

import yaml

from warmahordes_opendata import rules


class TestRule(unittest.TestCase):
    def setUp(self):
        super().setUp()

        filename = os.path.join(
            resources.files("warmahordes_opendata"),
            "data",
            "rules",
            "immunities",
            "immunity_fire.yaml",
        )

        with open(filename, "r") as fd:
            self.yaml = fd.read()

        self.rule = yaml.safe_load(self.yaml)

    def test_type(self):
        self.assertIsInstance(self.rule, rules.Rule)

    def test_name(self):
        self.assertEqual(self.rule.name, "immunity_fire")

    def test_title(self):
        self.assertEqual(self.rule.title, "Immunity: Fire")

    def test_description(self):
        self.assertEqual(
            self.rule.description,
            "This model does not suffer fire damage and "
            "is immune to the Fire continuous effect.\n",
        )

    def test_see_also(self):
        self.assertEqual(
            self.rule.see_also, ["damage_type_fire", "continuous_effect_fire"]
        )

    def test_to_dict(self):
        self.assertEqual(
            self.rule.to_dict(),
            dict(
                name="immunity_fire",
                title="Immunity: Fire",
                description="This model does not suffer fire damage "
                "and is immune to the Fire continuous effect.\n",
                see_also=["damage_type_fire", "continuous_effect_fire"],
            ),
        )
