from . import metro_card
from . import passenger


class MetroCardService:
    def __init__(self, metro_card_info: metro_card, passenger_info: passenger) -> None:
        self.metro_card = metro_card_info
        self.passenger = passenger_info
        self.total_amount_collected = 0
        self.total_discount_given = 0
        self.total_passengers_travelled = 0

    def check_in(self, station: str):
        self.passenger.has_travelled_count += 1

    def calculate_collection_summary(self):
        pass

    def calculate_passenger_summary(self):
        pass
