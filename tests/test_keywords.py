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

from tests import base

from warmahordes_opendata import i18n
from warmahordes_opendata import keywords


class TestKeywords(base.TestCase):
    def setUp(self):
        super().setUp()

        self.keyword = keywords.Immunity.FIRE.keyword

    def test_keyword(self):
        self.assertEqual("Immunity: Fire", self.keyword)

    def test_translate_pt_BR(self):
        self.assertNotEqual(str, type(self.keyword))
        self.assertEqual(
            "Imunidade: Fogo",
            i18n.translate(self.keyword, "pt_BR"),
        )
        self.assertEqual(
            "Imunidade: Fogo",
            i18n.translate("Immunity: Fire", "pt_BR"),
        )
