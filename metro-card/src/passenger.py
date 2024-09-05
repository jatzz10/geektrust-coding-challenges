from . import metro_card
from enum import Enum


class PassengerType(Enum):
    ADULT = 'ADULT'
    SENIOR_CITIZEN = 'SENIOR_CITIZEN'
    KID = 'KID'


class PassengerTravelCharge(Enum):
    ADULT = 200
    SENIOR_CITIZEN = 100
    KID = 50


class Passenger:

    def __init__(self, passenger_type: str) -> None:
        self.passenger_type = passenger_type

    def get_travel_charge_based_on_passenger_type(self):
        return PassengerTravelCharge[self.passenger_type].value
