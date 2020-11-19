from tests import base

from warmahordes_opendata import keywords


class TestTheme(base.TestCase):
    def test_immunities(self):
        self.assertEqual("Immunity: Fire", keywords.Immunity.FIRE.keyword)
