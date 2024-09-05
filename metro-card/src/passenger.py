from enum import Enum
from .constants import ADULT_TRAVEL_CHARGE, SENIOR_CITIZEN_TRAVEL_CHARGE, KID_TRAVEL_CHARGE


class PassengerType(Enum):
    ADULT = 'ADULT'
    SENIOR_CITIZEN = 'SENIOR_CITIZEN'
    KID = 'KID'


class PassengerTravelCharge(Enum):
    ADULT = ADULT_TRAVEL_CHARGE
    SENIOR_CITIZEN = SENIOR_CITIZEN_TRAVEL_CHARGE
    KID = KID_TRAVEL_CHARGE


class Passenger:

    def __init__(self, passenger_type: str) -> None:
        self.passenger_type = passenger_type

    def get_travel_charge_based_on_passenger_type(self):
        return PassengerTravelCharge[self.passenger_type].value
