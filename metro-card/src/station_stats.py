from typing import Dict


class StationStats:
    def __init__(self):
        self.__total_amount_collected: int = 0
        self.__total_discount_given: int = 0
        self.__passenger_type_count: Dict[str, int] = {}

    def get_total_amount_collected(self):
        return self.__total_amount_collected

    def get_total_discount_given(self):
        return self.__total_discount_given

    def get_passenger_type_count(self):
        return self.__passenger_type_count

    def add_to_total_amount_collected(self, amount: int):
        self.__total_amount_collected += amount

    def add_to_total_discount_given(self, amount: int):
        self.__total_discount_given += amount

    def update_passenger_type_count(self, passenger_type: str):
        if passenger_type in self.__passenger_type_count:
            self.__passenger_type_count[passenger_type] += 1
        else:
            self.__passenger_type_count[passenger_type] = 1

    def update_stats(self, passenger_type: str, travel_charge: int, discount_applied):
        self.add_to_total_amount_collected(travel_charge)
        self.add_to_total_discount_given(discount_applied)
        self.update_passenger_type_count(passenger_type)
