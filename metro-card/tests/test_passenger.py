import unittest
from ..src.passenger import Passenger, PassengerTravelCharge, PassengerType


class TestPassenger(unittest.TestCase):
    def init(self):
        passenger = Passenger('ADULT')
        self.assertEqual(passenger.get_passenger_type(), 'ADULT')

    def test_get_travel_charge_based_on_passenger_type(self):
        adult_passenger = Passenger('ADULT')
        self.assertEqual(adult_passenger.get_travel_charge_based_on_passenger_type(), PassengerTravelCharge.ADULT.value)

        senior_citizen_passenger = Passenger('SENIOR_CITIZEN')
        self.assertEqual(senior_citizen_passenger.get_travel_charge_based_on_passenger_type(),
                         PassengerTravelCharge.SENIOR_CITIZEN.value)

        kid_passenger = Passenger('KID')
        self.assertEqual(kid_passenger.get_travel_charge_based_on_passenger_type(), PassengerTravelCharge.KID.value)
