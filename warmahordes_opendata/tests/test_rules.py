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

from warmahordes_opendata import rules


class TestRule(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.rule = rules.Rule.find("immunity_fire")[0]

    def test_type(self):
        self.assertIsInstance(self.rule, rules.Rule)

    def test_repr(self):
        self.assertEqual(
            repr(self.rule),
            "Rule(title='Immunity: Fire', description="
            "'This model does not suffer fire damage and"
            " is immune to the Fire continuous effect.', "
            "see_also=['Damage Type: Fire', 'Continuous Effect: Fire'])",
        )

    def test_name(self):
        self.assertEqual(self.rule.name, "Immunity: Fire")

    def test_description(self):
        self.assertEqual(
            self.rule.description,
            "This model does not suffer fire damage and "
            "is immune to the Fire continuous effect.",
        )

    def test_see_also(self):
        self.assertEqual(
            self.rule.see_also,
            ["Damage Type: Fire", "Continuous Effect: Fire"],
        )

    def test_to_dict(self):
        self.assertEqual(
            self.rule.to_dict(),
            dict(
                name="Immunity: Fire",
                abbreviation="",
                description="This model does not suffer fire damage "
                "and is immune to the Fire continuous effect.",
                see_also=["Damage Type: Fire", "Continuous Effect: Fire"],
            ),
        )
