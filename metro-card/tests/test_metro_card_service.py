import unittest
from unittest.mock import patch
from ..src.metro_card_service import MetroCardService
from ..src.passenger import Passenger
from ..src.constants import DISCOUNT_DIVISOR


class TestMetroCardServices(unittest.TestCase):
    def setUp(self):
        self.metro_card_service = MetroCardService()

    def test_add_card_balance(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), 200)

    def test_calculate_travel_charge(self):
        self.assertEqual(self.metro_card_service.calculate_travel_charge('ADULT'),
                         Passenger('ADULT').get_travel_charge_based_on_passenger_type())

    def test_calculate_discount_for_one_way_journey(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.assertEqual(self.metro_card_service.calculate_discount(100, "MC1"), 0)

    def test_calculate_discount_for_return_journey(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.metro_card_service.get_metro_card_dict()["MC1"].set_card_swiped_for_one_way(True)
        self.assertEqual(self.metro_card_service.calculate_discount(100, "MC1"), 100 // DISCOUNT_DIVISOR)

    def test_add_recharge_fee_for_insufficient_balance(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.assertEqual(self.metro_card_service.add_recharge_fee_if_insufficient_balance("MC1", 250), 251)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), 250)

    def test_add_recharge_fee_for_sufficient_balance(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.assertEqual(self.metro_card_service.add_recharge_fee_if_insufficient_balance("MC1", 150), 150)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), 200)

    def test_update_station_stats(self):
        self.metro_card_service.update_station_stats("CENTRAL", "ADULT", 100, 0)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_amount_collected(), 100)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_discount_given(), 0)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()['CENTRAL'].get_passenger_type_count(), {"ADULT": 1})

    def test_update_metro_card(self):
        self.metro_card_service.add_card_balance("MC1", 100)
        self.metro_card_service.update_metro_card("MC1", 50)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), 50)
        self.assertTrue(self.metro_card_service.get_metro_card_dict()["MC1"].get_card_swiped_for_one_way())

    def test_perform_check_in(self):
        self.metro_card_service.add_card_balance("MC1", 200)
        self.metro_card_service.perform_check_in("MC1", "ADULT", "CENTRAL")
        self.assertEqual(len(self.metro_card_service.get_metro_card_dict()), 1)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), 0)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_card_swiped_for_one_way(), True)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_amount_collected(), 200)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_discount_given(), 0)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_passenger_type_count(), {"ADULT": 1})

    def test_print_summary(self):
        self.metro_card_service.add_card_balance("MC1", 100)
        self.metro_card_service.perform_check_in("MC1", "ADULT", "CENTRAL")
        with patch('builtins.print') as mock_print:
            self.metro_card_service.print_summary()
            mock_print.assert_called()
