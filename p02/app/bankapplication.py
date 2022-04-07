"""
INFPROG2 P02 - Inheritance in OOP
Author: Fabio Kapsahili
"""

"""
1.2 Bank application

The bank application should be an interactive application. The user should be able to do the following:
- Open a new account
  - The user should be able to enter the following information:
    - Name
    - Birthday
    - Currency
    - Initial balance
    - Select the account type (SavingAccount or YouthAccount)
- Close an account
- Deposit money
- Withdraw money
- An account should be able to have a single owner (the user) and multiple bank mandates.

The application should store the accounts and should use an attribute current_account to store the currently
selected account.

!!! How to use the bank application !!!
- Make sure you have an account signed up.
- Also make sure you are logged in. Only authenticated users are able to access most parts of the bank application.
- run the main.py script to start the application.
"""

from account.youthaccount import YouthAccount
from account.savingaccount import SavingAccount
from .taxreporting import TaxReport
from datetime import datetime


class BankApplication:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.__current_user = None
        self.current_account = None

    def get_accounts(self):
        return self.accounts

    def get_fiscal_year(self):
        return datetime.now().year

    def __sign_up_or_sign_in(self):
        # Let the user sign up or sign in with the given credentials
        print("Please sign up or sign in.")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        choice = input("Please select an option: ")
        if choice == "1":
            self.__sign_up()
        elif choice == "2":
            self.__sign_in()
        elif choice == "3":
            exit()
        else:
            print("Invalid option.")
            self.__sign_up_or_sign_in()

    def __sign_in(self):
        # Let the user sign in with the given credentials
        print("Please sign in.")
        print("1. Login with username and password")
        print("2. Go back")
        choice = input("Please select an option: ")
        if choice == "1":
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            for user in self.users:
                if user["username"] == username and user["password"] == hash(password):
                    self.__current_user = user
                    self.__main_menu()

            if self.__current_user is None:
                print("Invalid username or password.")
                self.__sign_in()

    def __sign_up(self):
        # Let the user sign up with the given credentials
        print("Please sign up.")
        print("1. Create a new user")
        print("2. Go back")
        choice = input("Please select an option: ")
        if choice == "1":
            self.__create_user()
        elif choice == "2":
            self.__sign_up_or_sign_in()
        else:
            print("Invalid option.")
            self.__sign_up()

    def __create_user(self):
        print("Please create a new user.")
        print("1. Enter username")
        # make sure the username is at least 2 characters long
        username = input("Please enter a username: ")
        while len(username) < 2:
            print("Username must be at least 2 characters long.")
            username = input("Please enter a username: ")
        # make sure the username is unique
        for user in self.users:
            if user["username"] == username:
                print("Username already taken.")
                self.__create_user()
        # make sure the password is at least 2 characters long
        password = input("Please enter a password: ")
        while len(password) < 2:
            print("Password must be at least 2 characters long.")
            password = input("Please enter a password: ")
        # make sure the password is at least 2 characters long
        password_confirmation = input("Please confirm your password: ")
        while password_confirmation != password:
            print("Passwords do not match.")
            password = input("Please enter a password: ")
        # create the user
        self.users.append({"username": username, "password": hash(password)})

    def __require_authentication(self):
        while True:
            if self.__current_user is None:
                print("You are currently logged out.")
                self.__sign_up_or_sign_in()
            else:
                break

    def __ask_to_associate_mandates(self, account):
        while True:
            choice = input(
                "Please enter Y/N if you want to associate the new account with any other users / mandates: "
            )
            if choice == "Y":
                user = input("Please enter the username to associate: ")
                found = False
                for u in self.users:
                    if u["username"] == user:
                        found = True
                        try:
                            u["accounts"].append(account)
                            print("Successfully associated the account with the user.")
                        except KeyError:
                            self.__current_user["accounts"] = [account]
                            print("Successfully associated the account with the user.")

                if not found:
                    print("Invalid username.")
                    self.__ask_to_associate_mandates(account)
            elif choice == "N":
                break

    def __main_menu(self):
        print("Welcome to the bank application!")
        print("-------------------------------")
        if self.__current_user is not None:
            print("Logged in as: ", self.__current_user["username"])
        print("-------------------------------")
        print("Please select an option:")
        if self.__current_user is None:
            print("1. Sign up or sign in")
        print("2. Open a new account")
        print("3. Close an account")
        print("4. Deposit money")
        print("5. Withdraw money")
        print("6. Show account information")
        print("7. Exit")
        print("8. Show users table (Dev Mode)")
        print("9. Generate tax report")
        print("-------------------------------")

    def run(self):
        self.__main_menu()

        while True:
            try:
                option = int(input("Please select an option: "))
            except ValueError:
                print("Please select a valid option!")
                continue

            if option == 1:
                self.__sign_up_or_sign_in()

            if option == 2:
                self.__require_authentication()
                print("-------------------------------")
                print("Please select the account type:")
                print("1. Youth account")
                print("2. Saving account")
                print("-------------------------------")

                while True:
                    try:
                        account_type = int(input("Please select an option: "))
                    except ValueError:
                        print("Please select a valid option!")
                        continue

                    name = input("Please enter the Account Holder name: ")
                    birthday = input("Please enter the birthday (dd.mm.yyyy): ")
                    currency = input("Please enter the currency (CHF, EUR, USD): ")
                    balance = input("Please enter the initial balance: ")

                    try:
                        birthday = datetime.strptime(birthday, "%d.%m.%Y")
                    except ValueError:
                        print("Please enter a valid birthday!")
                        continue
                    if account_type == 1:
                        account = YouthAccount(name=name, birthday=birthday, currency=currency, initial_balance=balance)
                        self.accounts.append(account)
                        try:
                            self.__current_user["accounts"].append(account)
                        except KeyError:
                            self.__current_user["accounts"] = [account]
                        print("Account created successfully!")
                        self.__ask_to_associate_mandates(account)
                        self.__main_menu()
                        break
                    elif account_type == 2:
                        account = SavingAccount(
                            name=name, birthday=birthday, currency=currency, initial_balance=balance
                        )
                        self.accounts.append(account)
                        try:
                            self.__current_user["accounts"].append(account)
                        except KeyError:
                            self.__current_user["accounts"] = [account]
                        print("Account created successfully!")
                        self.__ask_to_associate_mandates(account)
                        self.__main_menu()
                        break
                    else:
                        print("Please select a valid option!")
                        continue

            elif option == 3:
                self.__require_authentication()
                if self.current_account is None:
                    print("Please select an account!")
                    continue

                print("-------------------------------")
                print("Are you sure you want to close the account?")
                print("1. Yes")
                print("2. No")
                print("-------------------------------")

                while True:
                    try:
                        option = int(input("Please select an option: "))
                    except ValueError:
                        print("Please select a valid option!")
                        continue

                    if option == 1:
                        self.accounts.remove(self.current_account)
                        print("-------------------------------")
                        print("The account has been successfully closed!")
                        print("-------------------------------")
                        break
                    elif option == 2:
                        break
                    else:
                        print("Please select a valid option!")
                        continue
            elif option == 4:
                self.__require_authentication()
                if self.current_account is None:
                    print("Please select an account!")
                    continue

                print("-------------------------------")
                try:
                    amount = float(input("Please enter the amount: "))
                except ValueError:
                    print("Please enter a valid amount!")
                    continue

                self.current_account.deposit(amount)
                print("-------------------------------")
                print("The amount has been successfully deposited!")
                print("-------------------------------")
            elif option == 5:
                self.__require_authentication()
                if self.current_account is None:
                    print("Please select an account!")
                    continue

                print("-------------------------------")
                try:
                    amount = float(input("Please enter the amount: "))
                except ValueError:
                    print("Please enter a valid amount!")
                    continue

                self.current_account.withdraw(amount)
                print("-------------------------------")
                print("The amount has been successfully withdrawn!")
                print("-------------------------------")
            elif option == 6:
                self.__require_authentication()
                if len(self.accounts) == 0:
                    print("There are no accounts!")
                    continue
                elif self.current_account is None:
                    print("Please select an account!")
                    print("-------------------------------")
                    # Make sure the user can only select an account from the list of its own accounts
                    for i, account in enumerate(self.__current_user["accounts"]):
                        print(f"{i+1}. {account}")
                    print("-------------------------------")
                    try:
                        account_id = int(input("Please select an account: "))
                        self.current_account = self.accounts[account_id - 1]
                        print(self.current_account)
                        print("-------------------------------")
                        print("The account has been successfully selected!")
                        print("Account holder:", self.current_account.get_name())
                        print(
                            f"Balance ({self.current_account.get_currency()}): {str(self.current_account.get_balance())}"
                        )
                        print("Status:", "Closed" if self.current_account.get_is_closed() else "Open")

                        print("Interest rate:", self.current_account.get_interest_rate())
                        print("-------------------------------")
                    except Exception as exc:
                        print(exc)
                        print("You need to select a valid account number, e.g. 1, 2, 3, ...")
                        continue
                    continue

                print("-------------------------------")
                print(self.current_account)
                print("-------------------------------")
            elif option == 7:
                print("-------------------------------")
                print("Thank you for using the bank application!")
                print("-------------------------------")
                break
            elif option == 8:
                print("-------------------------------")
                print("Users:")
                print(self.users)
                print("-------------------------------")
            elif option == 9:
                tax_report = TaxReport(self)
                print("-------------------------------")
                print("Tax report:")
                tax_report.generate()
            else:
                self.__main_menu()
                continue
