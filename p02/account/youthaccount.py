"""
INFPROG2 P02 - Inheritance in OOP
Author: Fabio Kapsahili
"""

"""
1.1 Sub accounts

There should be two classes SavingAccount and YouthAccount which extend the existing BankAccount class.
The BankAccount class should be importd from the module bankaccount.py.

- YouthAccount:
    - The monthly interest rate is 2%. This rate should be changeable at any time.
    - The account can only be opened by a person who has an age of 25 years or below. The constructor
      should be used to check this.
    - Withdraw limit of 2000 per month.

The use of the bank account should be simulated over time with a simulation script. The computer's clock should be used
to invoke the methods in a certain oder with variable time gaps in between. 
"""

from account.bankaccount import BankAccount
from account.utils import calculate_age
from datetime import datetime


class Birthday:
    def __get__(self, obj, objtype=None):
        value = obj._birthday
        return value

    def __set__(self, obj, value):
        if value > datetime.today():
            raise ValueError("Birthday cannot be in the future.")
        elif calculate_age(value) > 25:
            raise ValueError("Age cannot be greater than 25.")
        obj._birthday = value


class YouthAccount(BankAccount):
    __birthday = Birthday()

    def __init__(self, birthday, currency="CHF", name=None, initial_balance=0):
        super().__init__(currency, interest_rate=0.02, name=name, balance=initial_balance)
        self.__birthday = birthday
        self.__withdraw_limit_monthly = 2000
        self.__withdraw_counter = 0
        self.__withdraw_limit_counter = 0

    def get_age(self):
        return calculate_age(self.__birthday)

    def get_withdraw_limit_monthly(self):
        return self.__withdraw_limit_monthly

    def get_withdraw_counter(self):
        return self.__withdraw_counter

    def get_withdraw_limit_counter(self):
        return self.__withdraw_limit_counter

    def get_balance(self):
        self.__add_interest()
        return super().get_balance()

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if super().get_is_closed():
            raise ValueError("The account is closed.")
        elif self.get_age() > 25:
            raise ValueError("The account is not open for this person.")
        elif amount <= 0:
            raise ValueError("The amount has to be greater than 0.")
        elif self.__withdraw_counter + amount > self.__withdraw_limit_monthly:
            raise ValueError("The withdraw limit has been reached.")
        elif super().get_balance() - amount < 0:
            raise ValueError("The balance cannot be negative.")
        else:
            super().withdraw(amount)
            self.__withdraw_counter += amount
            if self.__withdraw_counter > self.__withdraw_limit_monthly:
                self.__withdraw_limit_counter += 1
                self.__withdraw_counter = 0
            return True

    def __add_interest(self):
        if super().get_balance() > 0:
            seconds_past = int((datetime.now() - super().get_updated_at()).total_seconds())

            # calculate how many times 10 seconds are past
            seconds_past_10 = seconds_past // 10
            if seconds_past_10 > 0:
                interest = super().get_interest_rate() * super().get_balance()
                super().deposit(interest)
