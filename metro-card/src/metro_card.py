class MetroCard:

    def __init__(self, card_id: str, balance: int) -> None:
        """
        Initialize a MetroCard object.

        Args:
        - card_id: ID of the metro card.
        - balance: Initial balance of the metro card.
        """
        self.__card_id = card_id
        self.__balance = balance
        self.__card_swiped_for_one_way = False

    def get_balance(self):
        return self.__balance

    def get_card_swiped_for_one_way(self) -> bool:
        return self.__card_swiped_for_one_way

    def add_to_balance(self, amount: int) -> None:
        self.__balance += amount

    def deduct_from_balance(self, amount: int) -> None:
        self.__balance -= amount

    def set_card_swiped_for_one_way(self, value: bool) -> None:
        self.__card_swiped_for_one_way = value
