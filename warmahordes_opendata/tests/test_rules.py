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

import unittest

from warmahordes_opendata import rules


class TestRule(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.rule = rules.Immunity.FIRE

    def test_keyword(self):
        self.assertEqual(self.rule.keyword, "Immunity: Fire")

    def test_description(self):
        self.assertEqual(
            self.rule.description,
            "This model does not suffer fire damage and "
            "is immune to the Fire continuous effect.",
        )