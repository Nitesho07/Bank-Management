import json
import random
import string
from pathlib import Path


class Bank:
    """
    A simple Bank Management System using Python OOPs and JSON for data storage.
    """

    database = 'data.json'
    data = []

    try:
        with open(database) as fs:
            data = json.loads(fs.read())
    except Exception as err2:
        print(f"an exception occured as {err2}")

    @staticmethod
    def __update():  # __ is added to make it private to bank server
        """Update the JSON database file with the latest Bank data."""
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountGenerate(cls):
        """Generate a unique 11-digit account number for a new account."""
        num = random.choices(string.digits, k=11)
        id = num
        random.shuffle(id)
        userData = [i for i in Bank.data if i["accountNo."] == id]
        try:
            if not userData:
                return "".join(id)
            else:
                Bank.__accountGenerate()
        except Exception as err3:
            print(f"An unexpected error occured as {err3}")

    def create_account(self):
        """Create a new bank account with name, age, email, PIN, and an auto-generated account number."""
        info = {
            "name": input("Tell your name :-  "),
            "age": int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin": int(input("Tell your 4 digit pin :- ")),
            "accountNo.": Bank.__accountGenerate(),
            "balance": 0
        }

        userData = [i for i in Bank.data if i["email"] == info["email"]]

        if userData != []:
            print("Account Already exist")
        else:
            if info['age'] < 18:
                print("Sorry you cannot create your account  ")
            elif len(str(info['pin'])) != 4:
                print("The pin should be of 4 digits ")
            else:
                for i in info:
                    print(f"{i} : {info[i]} ")

                print("Please note your account number ")
                Bank.data.append(info)

                Bank.__update()
                print("✅ Account created successfully! ")

    def deposite_money(self):
        """Deposit money into an existing account (limit: 10,000 per transaction)."""
        accNo = input("Enter your Acccount Number :-   ")
        pin = int(input("Enter your pin :- "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNo and i['pin'] == pin
        ]

        if not userData:
            print("Sorry Your Account does not exist")
        else:
            amount = int(input("Enter the money to Deposite :- "))
            if amount > 10000:
                print("Sorry the amount is more than 10000")
            elif amount < 0:
                print(" Please Enter a valid amoount to Deposite ")
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount Deposited Succesfully ")

    def withdraw_money(self):
        """Withdraw money from an existing account after verifying balance and PIN."""
        accNo = input("Enter your Acccount Number :-   ")
        pin = int(input("Enter your pin :- "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNo and i['pin'] == pin
        ]

        if not userData:
            print("Sorry Your Account does not exist")
        else:
            print(f'Your balance : {userData[0]["balance"]}')
            amount = int(input("Enter the money to Withdraw :- "))
            if amount > userData[0]['balance']:
                print("Insufficient Balance ")
            elif amount < 0:
                print(" Please Enter a valid amoount to Withdraw ")
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print(" Succesfully Withdrawn ")

    def show_details(self):
        """Display account details (name, age, email, PIN, account number, balance) for a valid account."""
        accNo = input("Enter your Acccount Number :-   ")
        pin = int(input("Enter your pin :- "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNo and i['pin'] == pin
        ]

        if not userData:
            print("Sorry Your Account does not exist")
        else:
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")

    def update_details(self):
        """Update account details like name, email, or PIN after verifying account credentials."""
        accNo = input("Enter your Acccount Number :-   ")
        pin = int(input("Enter your pin :- "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNo and i['pin'] == pin
        ]

        if not userData:
            print("Sorry Your Account does not exist")
        else:
            print("Enter the following details to update or Press Enter to Skip ")

            name = input("Enter Your name to Update :- ")
            email = input("Enter your new Email :- ")
            newPin = input("Create New pin of 4 digits :- ")

            if newPin == '':
                newPin = userData[0]['pin']
            else:
                if not (newPin.isalnum() and len(newPin) == 4):
                    print("Invalid PIN , Keeping old Pin")
                    newPin = userData[0]['pin']
                else:
                    newPin = int(newPin)

            newData = {
                "name": name if name != "" else userData[0]['name'],
                "email": email if email != "" else userData[0]['email'],
                "pin": newPin
            }

            userData[0].update(newData)

            Bank.__update()
            print("Your Details Updated Succesfully")

    def delete(self):
        """Delete an existing bank account permanently after confirmation."""
        accNo = input("Enter your Acccount Number :-   ")
        pin = int(input("Enter your pin :- "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNo and i['pin'] == pin
        ]

        if not userData:
            print("Sorry Your Account does not exist")
        else:
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")
            check = input("Press Enter if you want to delete your account : ")

            if check == '':
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Account deleted Succesfully ")
                Bank.__update()


user = Bank()
while True:
    print("Press 1 for Creating a account")
    print("Press 2 for Depositing the money in the bank")
    print("Press 3 for Withdrawing the money ")
    print("Press 4 for Details ")
    print("Press 5 for Updating the details")
    print("Press 6 for Deleting your account")
    print("Press 0 to exit")

    try:
        check = int(input("Tell your Response :- "))

        if check == 1:
            user.create_account()
        elif check == 2:
            user.deposite_money()
        elif check == 3:
            user.withdraw_money()
        elif check == 4:
            user.show_details()
        elif check == 5:
            user.update_details()
        elif check == 6:
            user.delete()
        elif check == 0:
            print("👋 Thank you for using Bank Management System.")
            break
        else:
            print("❌Invalid Response")
    except Exception as err1:
        print(f"An unexpected error occured as {err1}")
