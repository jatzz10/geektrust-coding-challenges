
class MetroCard:

    def __init__(self, card_id: str, balance: float) -> None:
        self.card_id = card_id
        self.balance = balance

    def has_sufficient_balance(self, cost_of_travel: float) -> bool:
        return True if cost_of_travel <= self.balance else False

    def recharge_balance(self, cost_of_travel: float) -> None:
        self.balance += cost_of_travel + (0.02 * cost_of_travel)
