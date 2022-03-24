class BankAccount:
    def __init__(self, amount) -> None:
        self.amount = amount

    def withdraw(self, withdraw_amount):
        if self.amount > withdraw_amount:
            self.amount -= withdraw_amount
            return True

        return False

    def deposit(self, deposit_amount):
        self.amount += deposit_amount


b1 = BankAccount(200)
print(b1.withdraw(1000))
