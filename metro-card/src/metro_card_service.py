from typing import Dict

from .metro_card import MetroCard
from .station_stats import StationStats
from .passenger import Passenger
from .constants import RECHARGE_FEE_PERCENTAGE, DISCOUNT_DIVISOR


class MetroCardService:
    def __init__(self) -> None:
        self.metro_card_dict: Dict[str, MetroCard] = {}
        self.station_stats_dict: Dict[str, StationStats] = {}

    def add_card_balance(self, card_id: str, balance: int):
        """
        Method to add card balance to the MetroCard
        """
        if card_id not in self.metro_card_dict:
            metro_card = MetroCard(card_id, balance)
            self.metro_card_dict[card_id] = metro_card
        else:
            metro_card = self.metro_card_dict.get(card_id)
            metro_card.add_to_balance(balance)

    def perform_check_in(self, card_id: str, passenger_type: str, station_name: str):
        """
        Method to perform calculation of travel charge, discount applied, and
        update the station stats
        """
        travel_amount_charged = 0
        discount_applied = 0

        # Fetch travel_charge_based_on_passenger_type
        travel_charge_based_on_passenger_type: int = int(Passenger(passenger_type).get_travel_charge_based_on_passenger_type())

        metro_card = self.metro_card_dict.get(card_id)
        # Calculate discount if applicable
        if metro_card.card_swiped_for_one_way:
            discounted_amount = travel_charge_based_on_passenger_type // DISCOUNT_DIVISOR
            travel_charge_based_on_passenger_type = discounted_amount
            travel_amount_charged += discounted_amount
            discount_applied += discounted_amount
        else:
            travel_amount_charged += travel_charge_based_on_passenger_type

        # Check if metro card has sufficient balance for travel journey
        if metro_card.balance < travel_charge_based_on_passenger_type:
            # Calculate amount to be recharged
            amount_to_be_recharged = travel_charge_based_on_passenger_type - metro_card.balance
            metro_card.add_to_balance(amount_to_be_recharged)
            travel_amount_charged += int(amount_to_be_recharged * RECHARGE_FEE_PERCENTAGE)

        # Update MetroCard data
        metro_card.deduct_from_balance(travel_amount_charged)
        metro_card.card_swiped_for_one_way = not metro_card.card_swiped_for_one_way

        # Update MetroCard data with metro_card_dict
        self.metro_card_dict[card_id] = metro_card

        # Calculate station stats
        if station_name in self.station_stats_dict:
            station_stats = self.station_stats_dict.get(station_name)
        else:
            station_stats = StationStats()
        station_stats.update_stats(passenger_type, travel_amount_charged, discount_applied)
        self.station_stats_dict[station_name] = station_stats

    def print_summary(self):
        # Sort the keys of station_stats_dict dictionary in ascending order
        self.station_stats_dict = dict(sorted(self.station_stats_dict.items(), key=lambda x: x[0], reverse=True))

        for station_name, station_stats in self.station_stats_dict.items():
            print(f'TOTAL_COLLECTION {station_name} {station_stats.total_amount_collected} {station_stats.total_discount_given}')
            print('PASSENGER_TYPE_SUMMARY')

            # Sort the dictionary, first based on value in descending order, and then based on key in ascending order
            passenger_count_list_by_type = sorted(station_stats.passenger_type_count.items(), key=lambda x: (-x[1], x[0]))

            for passenger_count_tuple in passenger_count_list_by_type:
                passenger_type, count = passenger_count_tuple[0], passenger_count_tuple[1]
                print(passenger_type, count)
