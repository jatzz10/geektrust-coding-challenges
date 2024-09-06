class MetroCard:

    def __init__(self, card_id: str, balance: int) -> None:
        self.__card_id = card_id
        self.__balance = balance
        self.__card_swiped_for_one_way = False

    def get_balance(self):
        return self.__balance

    def get_card_swiped_for_one_way(self):
        return self.__card_swiped_for_one_way

    def add_to_balance(self, amount: int) -> None:
        self.__balance += amount

    def deduct_from_balance(self, amount: int) -> None:
        self.__balance -= amount

    def set_card_swiped_for_one_way(self, value: bool):
        self.__card_swiped_for_one_way = value
