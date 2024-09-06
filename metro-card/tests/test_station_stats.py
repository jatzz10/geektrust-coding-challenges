import unittest
from src.station_stats import StationStats


class TestStationStats(unittest.TestCase):
    def setUp(self):
        self.station_stats = StationStats()

    def init(self):
        self.assertEqual(self.station_stats.get_total_amount_collected(), 0)
        self.assertEqual(self.station_stats.get_total_discount_given(), 0)
        self.assertEqual(self.station_stats.get_passenger_type_count(), {})

    def test_add_to_total_amount_collected(self):
        self.station_stats.add_to_total_amount_collected(100)
        self.assertEqual(self.station_stats.get_total_amount_collected(), 100)

    def test_add_to_total_discount_given(self):
        self.station_stats.add_to_total_discount_given(50)
        self.assertEqual(self.station_stats.get_total_discount_given(), 50)

    def test_update_passenger_type_count(self):
        self.station_stats.update_passenger_type_count('ADULT')
        self.assertEqual(self.station_stats.get_passenger_type_count(), {'ADULT': 1})

    def test_update_stats(self):
        self.station_stats.update_stats('ADULT', 100, 50)
        self.assertEqual(self.station_stats.get_total_amount_collected(), 100)
        self.assertEqual(self.station_stats.get_total_discount_given(), 50)
        self.assertEqual(self.station_stats.get_passenger_type_count(), {'ADULT': 1})
