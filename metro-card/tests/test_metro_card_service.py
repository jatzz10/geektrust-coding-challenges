import unittest
from unittest.mock import patch
from src.metro_card_service import MetroCardService
from src.passenger import Passenger
from src.constants import DISCOUNT_DIVISOR, ZERO_DISCOUNT
from tests.contants import (METRO_CARD_DICT_LENGTH_1, TRAVEL_AMOUNT_CHARGED_50, TRAVEL_AMOUNT_CHARGED_100,
                            TRAVEL_AMOUNT_CHARGED_150, TRAVEL_AMOUNT_CHARGED_250, BALANCE_0, BALANCE_50, BALANCE_100,
                            BALANCE_200, BALANCE_250, ADULT_PASSENGER_COUNT_1, TOTAL_AMOUNT_COLLECTED_100,
                            TOTAL_AMOUNT_COLLECTED_200, RECHARGE_FEE_251)


class TestMetroCardServices(unittest.TestCase):
    def setUp(self):
        self.metro_card_service = MetroCardService()

    def test_add_card_balance(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(),
                         BALANCE_200)

    def test_calculate_travel_charge(self):
        self.assertEqual(self.metro_card_service.calculate_travel_charge('ADULT'),
                         Passenger('ADULT').get_travel_charge_based_on_passenger_type())

    def test_calculate_discount_for_one_way_journey(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.assertEqual(self.metro_card_service.calculate_discount(TRAVEL_AMOUNT_CHARGED_100, "MC1"), ZERO_DISCOUNT)

    def test_calculate_discount_for_return_journey(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.metro_card_service.get_metro_card_dict()["MC1"].set_card_swiped_for_one_way(True)
        self.assertEqual(self.metro_card_service.calculate_discount(TRAVEL_AMOUNT_CHARGED_100, "MC1"),
                         TRAVEL_AMOUNT_CHARGED_100 // DISCOUNT_DIVISOR)

    def test_add_recharge_fee_for_insufficient_balance(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.assertEqual(self.metro_card_service.add_recharge_fee_if_insufficient_balance("MC1", TRAVEL_AMOUNT_CHARGED_250), RECHARGE_FEE_251)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), BALANCE_250)

    def test_add_recharge_fee_for_sufficient_balance(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.assertEqual(self.metro_card_service.add_recharge_fee_if_insufficient_balance("MC1",
                         TRAVEL_AMOUNT_CHARGED_150), TRAVEL_AMOUNT_CHARGED_150)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), BALANCE_200)

    def test_update_station_stats(self):
        self.metro_card_service.update_station_stats("CENTRAL", "ADULT", TRAVEL_AMOUNT_CHARGED_100, ZERO_DISCOUNT)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_amount_collected(), TOTAL_AMOUNT_COLLECTED_100)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_discount_given(), ZERO_DISCOUNT)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()['CENTRAL'].get_passenger_type_count(),
                         {"ADULT": ADULT_PASSENGER_COUNT_1})

    def test_update_metro_card(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_100)
        self.metro_card_service.update_metro_card("MC1", TRAVEL_AMOUNT_CHARGED_50)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), BALANCE_50)
        self.assertTrue(self.metro_card_service.get_metro_card_dict()["MC1"].get_card_swiped_for_one_way())

    def test_perform_check_in(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_200)
        self.metro_card_service.perform_check_in("MC1", "ADULT", "CENTRAL")
        self.assertEqual(len(self.metro_card_service.get_metro_card_dict()), METRO_CARD_DICT_LENGTH_1)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_balance(), BALANCE_0)
        self.assertEqual(self.metro_card_service.get_metro_card_dict()["MC1"].get_card_swiped_for_one_way(), True)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_amount_collected(), TOTAL_AMOUNT_COLLECTED_200)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_total_discount_given(), ZERO_DISCOUNT)
        self.assertEqual(self.metro_card_service.get_station_stats_dict()["CENTRAL"].get_passenger_type_count(), {"ADULT": ADULT_PASSENGER_COUNT_1})

    def test_print_summary(self):
        self.metro_card_service.add_card_balance("MC1", BALANCE_100)
        self.metro_card_service.perform_check_in("MC1", "ADULT", "CENTRAL")
        with patch('builtins.print') as mock_print:
            self.metro_card_service.print_summary()
            mock_print.assert_called()
