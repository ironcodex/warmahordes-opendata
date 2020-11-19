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
