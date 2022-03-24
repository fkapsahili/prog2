"""
INFPROG2 P01 - Objects
Author: Fabio Kapsahili
"""

"""
2.3 "Bank account" 

Write a class BankAccount that represents a bank account.

A bank account is unqiuely identified by a number, e.g. IBAN.
A bank account can be closed, and can be opened again.
Money can be deposited and withdrawn from the bank account.
The amount should have an account-specific currency, by default Swiss francs.
A bank account balance cannot be negative and not be above 100'000 in it's currency.

It is assumed that even a closed BankAccount instance can be reopened and vice versa.

The class should be tested using a non-interactive test suite.

Please not that the iso4217 library is required for the currency code validation and needs
to be installed via pip.
"""

import random
from string import ascii_lowercase, digits
from iso4217 import Currency
from datetime import datetime


class CurrencyCode:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        try:
            Currency(value)
            setattr(obj, self.private_name, value)
        except:
            raise ValueError("Currency code not supported.")


class BankAccount:
    __currency = CurrencyCode()

    def __init__(self, currency="CHF", balance=0, interest_rate=0.0):
        self.__account_number = self.__generate_account_number()
        self.__currency = currency
        self.__balance = balance
        self.__is_closed = False
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        self.__interest_rate = interest_rate

    def open(self):
        if self.__is_closed:
            self.__is_closed = False

    def close(self):
        if not self.__is_closed:
            self.__is_closed = True

    def deposit(self, amount):
        if self.__is_closed:
            raise ValueError("The account is closed.")
        elif amount <= 0:
            raise ValueError("The amount has to be greater than 0.")
        elif self.__balance + amount > 100000:
            raise ValueError("The balance cannot be greater than 100'000.")
        else:
            self.__balance += amount
            self.set_updated_at()

    def withdraw(self, amount):
        if self.__is_closed:
            raise ValueError("The account is closed.")
        elif amount <= 0:
            raise ValueError("The amount has to be greater than 0.")
        elif self.__balance - amount < 0:
            raise ValueError("The balance cannot be negative.")
        else:
            self.__balance -= amount
            self.set_updated_at()

    def get_is_closed(self):
        return self.__is_closed

    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency

    def get_interest_rate(self):
        return self.__interest_rate

    def get_created_at(self):
        return self.__created_at

    def get_updated_at(self):
        return self.__updated_at

    def get_account_number(self):
        return self.__account_number

    def set_balance(self, amount):
        self.__balance = amount

    def set_interest_rate(self, rate):
        self.__interest_rate = rate

    def set_updated_at(self):
        self.__updated_at = datetime.now()

    # show the current balance with the currency in a readable format
    def __repr__(self):
        return f"Account: {self.__account_number}, Balance: {self.__balance}"

    # generate a unique identifier with the prefix 'ba_', e.g. ba_1Kc5Qn2eZvKYlo2COU6VInx1
    def __generate_account_number(self):
        id = "".join(random.choice(ascii_lowercase + digits) for _ in range(24))
        res = "".join(random.choice((str.upper, str.lower))(char) for char in id)
        return "ba_" + res


def main():
    account = BankAccount()
    account.deposit(100)
    account.deposit(100)
    account.withdraw(50)
    account.withdraw(50)
    account.withdraw(50)
    print("Account number:", account.get_account_number())
    print("Current balance:", account.get_balance())
    print("Currency:", account.get_currency())

    # test that a closed bank account cannot withdraw money
    account.close()
    try:
        account.withdraw(50)
    except ValueError as exc:
        print(exc)

    # test that a closed bank account cannot deposit money
    try:
        account.deposit(50)
    except ValueError as exc:
        print(exc)

    # test that a negative balance is not possible
    account.open()
    account.withdraw(50)
    try:
        account.withdraw(50)
    except ValueError as exc:
        print(exc)
        print(account.__repr__())

    # test that a balance cannot be greater than 100'000
    account.deposit(100000)
    try:
        account.deposit(100)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
