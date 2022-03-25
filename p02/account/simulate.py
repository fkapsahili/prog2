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

from savingaccount import SavingAccount
from youthaccount import YouthAccount
from time import sleep
from datetime import datetime


def main():
    print("Test scenario 1: Create a new Saving Account", end="\n")
    print("-------------------------------", end="\n\n")

    saving_account = SavingAccount()
    print("The monthly interest rate is:", saving_account.get_interest_rate())

    # Set the monthly interest rate to 0.2%
    saving_account.set_interest_rate(0.002)

    # Retrieve the monthly interest rate
    print("The monthly interest rate is:", saving_account.get_interest_rate())

    # Deposit some money and withdraw more than the balance
    saving_account.deposit(1000)
    sleep(10)
    print("The balance is:", saving_account.get_balance())
    sleep(10)
    print("The balance is:", saving_account.get_balance())
    saving_account.deposit(500)
    sleep(10)
    print("The balance is:", saving_account.get_balance())
    saving_account.withdraw(saving_account.get_balance())
    print("The balance is:", saving_account.get_balance())

    # Test if the account balance can be negative and if the withdaw costs an additional 2%
    saving_account.withdraw(100)
    print("The balance is:", saving_account.get_balance())

    # Create a new saving account
    print("Test scenario 2: Create a new Youth Account", end="\n")
    print("-------------------------------", end="\n\n")

    youth_account = YouthAccount(birthday=datetime(year=2000, month=1, day=1))
    print("The monthly interest rate is:", youth_account.get_interest_rate())

    # Set the monthly interest rate to 3.0%
    youth_account.set_interest_rate(0.03)

    # Retrieve the monthly interest rate
    print("The monthly interest rate is:", youth_account.get_interest_rate())

    # Deposit some money and withdraw more than the balance
    youth_account.deposit(1000)
    sleep(10)
    print("The balance is:", youth_account.get_balance())
    sleep(10)
    print("The balance is:", youth_account.get_balance())
    youth_account.deposit(1500)
    sleep(10)
    print("The balance is:", youth_account.get_balance())

    # Test if the account balance can reach more than 2000 per month
    try:
        youth_account.withdraw(2500)
    except ValueError as exc:
        print(exc)
        print(youth_account.get_balance())

    youth_account.withdraw(2000)


if __name__ == "__main__":
    main()
