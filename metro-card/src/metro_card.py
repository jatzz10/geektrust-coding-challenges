class MetroCard:

    def __init__(self, card_id: str, balance: int) -> None:
        self.card_id = card_id
        self.balance = balance
        self.card_swiped_for_one_way = False

    def add_to_balance(self, amount: int) -> None:
        self.balance += amount

    def deduct_from_balance(self, amount: int) -> None:
        self.balance -= amount
