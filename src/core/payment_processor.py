class PaymentProcessor:
    def __init__(self):
        self.balance = 0.0

    def add_credit(self, amount: float) -> None:
        self.balance += max(0.0, float(amount))

    def charge(self, cost: float) -> bool:
        if self.balance >= cost:
            self.balance -= cost
            return True
        return False
