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

from warmahordes_opendata import i18n
from warmahordes_opendata import rules


class TestTranslation(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.message = rules.Immunity.FIRE.keyword

    def test_message(self):
        self.assertEqual(self.message, "Immunity: Fire")
        self.assertNotEqual(type(self.message), str)

    def test_pt_BR_is_available(self):
        self.assertIn("pt_BR", i18n.get_available_languages())

    def test_pt_BR_translation_from_message(self):
        self.assertEqual(
            i18n.translate(self.message, "pt_BR"),
            "Imunidade: Fogo",
        )

    def test_pt_BR_translation_from_str(self):
        self.assertEqual(
            i18n.translate("Immunity: Fire", "pt_BR"),
            "Imunidade: Fogo",
        )
