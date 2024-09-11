import unittest
from src.station_stats import StationStats
from tests.contants import (TOTAL_AMOUNT_COLLECTED_0, TOTAL_DISCOUNT_GIVEN_0, TOTAL_DISCOUNT_GIVEN_50, DISCOUNT_APPLIED_50,
                            TOTAL_AMOUNT_COLLECTED_100, TRAVEL_AMOUNT_CHARGED_100, ADULT_PASSENGER_COUNT_1)


class TestStationStats(unittest.TestCase):
    def setUp(self):
        self.station_stats = StationStats()

    def test_init(self):
        self.assertEqual(self.station_stats.get_total_amount_collected(), TOTAL_AMOUNT_COLLECTED_0)
        self.assertEqual(self.station_stats.get_total_discount_given(), TOTAL_DISCOUNT_GIVEN_0)
        self.assertEqual(self.station_stats.get_passenger_type_count(), {})

    def test_add_to_total_amount_collected(self):
        self.station_stats.add_to_total_amount_collected(TOTAL_AMOUNT_COLLECTED_100)
        self.assertEqual(self.station_stats.get_total_amount_collected(), TOTAL_AMOUNT_COLLECTED_100)

    def test_add_to_total_discount_given(self):
        self.station_stats.add_to_total_discount_given(DISCOUNT_APPLIED_50)
        self.assertEqual(self.station_stats.get_total_discount_given(), TOTAL_DISCOUNT_GIVEN_50)

    def test_update_passenger_type_count(self):
        self.station_stats.update_passenger_type_count('ADULT')
        self.assertEqual(self.station_stats.get_passenger_type_count(), {'ADULT': ADULT_PASSENGER_COUNT_1})

    def test_update_stats(self):
        self.station_stats.update_stats('ADULT', TRAVEL_AMOUNT_CHARGED_100, DISCOUNT_APPLIED_50)
        self.assertEqual(self.station_stats.get_total_amount_collected(), TOTAL_AMOUNT_COLLECTED_100)
        self.assertEqual(self.station_stats.get_total_discount_given(), TOTAL_DISCOUNT_GIVEN_50)
        self.assertEqual(self.station_stats.get_passenger_type_count(), {'ADULT': ADULT_PASSENGER_COUNT_1})
