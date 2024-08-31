from . import metro_card
from enum import Enum


class PassengerType(Enum):
    ADULT = 'ADULT'
    SENIOR_CITIZEN = 'SENIOR_CITIZEN'
    KIDS = 'KIDS'


class PassengerTravelCharge(Enum):
    ADULT = 200
    SENIOR_CITIZEN = 100
    KIDS = 50


class Passenger:

    def __init__(self, passenger_type: str) -> None:
        self.passenger_type = passenger_type
        self.has_travelled_count = 0
        # self.issued_metro_card = metro_card.MetroCard()
        self.travel_charge = PassengerTravelCharge[self.passenger_type].value

    def calculate_cost_of_travel(self) -> int:
        return self.travel_charge // 2 if self.has_travelled_count == 2 else self.travel_charge
