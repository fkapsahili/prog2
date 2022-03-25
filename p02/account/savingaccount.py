"""
INFPROG2 P02 - Inheritance in OOP
Author: Fabio Kapsahili
"""

"""
1.1 Sub accounts

There should be two classes SavingAccount and YouthAccount which extend the existing BankAccount class.
The BankAccount class should be importd from the module bankaccount.py.

- SavingAccount:
    - Monthly interest rate of 0.1%. This rate should be updateable at any time.
    - The bank balance can be below zero. In that case every withdraw costs additional 2% of the amount withdrawn.

- YouthAccount:
    - The monthly interest rate is 2%. This rate should be changeable at any time.
    - The account can only be opened by a person who has an age of 25 years or below. The constructor
      should be used to check this.
    - Withdraw limit of 2000 per month.

The use of the bank account should be simulated over time with a simulation script. The computer's clock should be used
to invoke the methods in a certain oder with variable time gaps in between. 
"""

from account.bankaccount import BankAccount
from datetime import datetime


class SavingAccount(BankAccount):
    def __init__(self, currency="CHF", name=None, initial_balance=0):
        super().__init__(currency, interest_rate=0.001, name=name, balance=initial_balance)

    def get_balance(self):
        self.__add_interest()
        return super().get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The amount has to be greater than 0.")
        else:
            new_balance = self.get_balance() - amount
            if new_balance < 0:
                # add an addition 2% to the amount
                new_balance = new_balance - (amount * 0.02)
            super().set_balance(new_balance)

    def __add_interest(self):
        if super().get_balance() > 0:
            seconds_past = int((datetime.now() - super().get_updated_at()).total_seconds())

            # calculate how many times 10 seconds are past
            seconds_past_10 = seconds_past // 10
            if seconds_past_10 > 0:
                interest = super().get_interest_rate() * super().get_balance()
                super().deposit(interest)
