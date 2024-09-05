from typing import Dict


class StationStats:
    def __init__(self):
        self.total_amount_collected: int = 0
        self.total_discount_given: int = 0
        self.passenger_type_count: Dict[str, int] = {}

    def add_to_total_amount_collected(self, amount: int):
        self.total_amount_collected += amount

    def add_to_total_discount_given(self, amount: int):
        self.total_discount_given += amount

    def update_passenger_type_count(self, passenger_type: str):
        if passenger_type in self.passenger_type_count:
            self.passenger_type_count[passenger_type] += 1
        else:
            self.passenger_type_count[passenger_type] = 1

    def update_stats(self, passenger_type: str, travel_charge: int, discount_applied):
        self.add_to_total_amount_collected(travel_charge)
        self.add_to_total_discount_given(discount_applied)
        self.update_passenger_type_count(passenger_type)
