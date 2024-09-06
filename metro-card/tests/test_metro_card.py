import unittest
from ..src.metro_card import MetroCard


class TestMetroCard(unittest.TestCase):
    def setUp(self):
        self.metro_card = MetroCard("MC1", 200)

    def test_init(self):
        self.assertEqual(self.metro_card.get_balance(), 200)
        self.assertFalse(self.metro_card.get_card_swiped_for_one_way())

    def test_add_to_balance(self):
        self.metro_card.add_to_balance(100)
        self.assertEqual(self.metro_card.get_balance(), 300,
                         f"Expected balance to be 300 after adding 100, but got {self.metro_card.get_balance()}")

    def test_deduct_from_balance(self):
        self.metro_card.deduct_from_balance(100)
        self.assertEqual(self.metro_card.get_balance(), 100,
                         f"Expected balance to be 100 after deducting 100, but got {self.metro_card.get_balance()}")

    def test_set_card_swiped_for_one_way(self):
        self.metro_card.set_card_swiped_for_one_way(True)
        self.assertTrue(self.metro_card.get_card_swiped_for_one_way(),
                        f"Expected card_swiped_for_one_way as True, but got {self.metro_card.get_card_swiped_for_one_way()}")
