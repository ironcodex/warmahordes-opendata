import oslo_i18n
from tests import base

from warmahordes_opendata import keywords


class TestKeywords(base.TestCase):
    def setUp(self):
        super().setUp()

        self.keyword = keywords.Immunity.FIRE.keyword

    def test_keyword(self):
        self.assertEqual("Immunity: Fire", self.keyword)

    def test_translate_pt_BR(self):
        self.assertEqual(
            "Imunidade: Fogo",
            oslo_i18n.translate(self.keyword, "pt_BR"),
        )
