"""
INFPROG2 P02 - Inheritance in OOP
Author: Fabio Kapsahili
"""

"""
1.3 Tax reporting

The application should be completed with a solution tax report generator.
The class should be called TaxReport and have a method generate that takes a
bank application object as parameter and sums up the wealth for submission to the tax office.

Interests do not need to be considered.

The format should be similiar to the following:
    Tax report 2022 for fiscal year 2021
    ** Savings Account ** 50000.00 Fr
    ** Youth Account ** -10000.00 Fr
    ** Total ** 40000.00 Fr
"""

"""
P03 1.2 "Data use"

The application should be completed with a currency conversion if the currency is not CHF.
Therefore the currency conversion should be done in the TaxReport class.
The module currency_converter.py should be imported.
"""

from account.currency_converter import get_rate


class TaxReport:
    def __init__(self, bank_application):
        self.__bank_application = bank_application

    def __get_total_wealth(self, accounts):
        total = 0
        for account in accounts:
            total += account.get_balance()
        return total

    def generate(self):

        print(
            "Tax report 2022 for fiscal year 2021".format(
                self.__bank_application.get_fiscal_year(), self.__bank_application.get_fiscal_year() - 1
            )
        )
        for account in self.__bank_application.get_accounts():
            # convert the balance to CHF
            if account.get_currency() != "CHF":
                rate = get_rate(account.get_currency())
                if rate is not None:
                    balance = account.get_balance() * rate["result"]
                else:
                    balance = account.get_balance()

            print("** {} Account ** {} {} CHF".format(account.__class__.__name__, account.get_name(), balance))

        print("** Total ** {} Fr".format(self.__get_total_wealth(self.__bank_application.get_accounts())))
