# ATM Program
# By Daniel Clancy
# v0.3 Updated 12-8-2020
# This program is a simulation of how an ATM works without the whole GUI layer

# I fully acknowledge that my use of global variables is not best practice, but python is not my primary programming language and I'm tired.

import math

quit = False
logged_in = False

username = "rbrown"
password = "blue123"

savings_balance = 2500.00
checking_balance = 35.00

# Displays the account balance info
def showInfo():
    print(f"Checking account: ${checking_balance}")
    print(f"Savings account: ${savings_balance}\n")

# Checks if the amount entered has coins
# eg. 2.34 has coins, 3 does not have coins
def has_coins(amount):
    if amount - math.floor(amount) == 0:
        return False
    else:
        return True

# Lets the user choose between the two accounts
# will continue to loop until you choose a valid account
def choose_account():
    account = "0"

    while (account != "1") and (account != "2"):
        print("\n1. Checking Account")
        print("2. Savings Account")
        account = input("Choose an account: ")

    return account

# handles deposit and withdrawl logic
def deposit_or_withdrawl(transaction_type):
    account = choose_account()

    amount = float(input(f"How much would you like to {transaction_type}? "))
    if not has_coins(amount):
        if transaction_type == "deposit":
            deposit(amount, account)
        elif transaction_type == "withdrawl":
            withdrawl(amount, account)
    else:
        print("Transactions must be in whole dollar amounts.")


# does the actual deposit
def deposit(amount, account):
    global checking_balance, savings_balance
    if account == "1":
        checking_balance = checking_balance + amount
    elif account == "2":
        savings_balance = savings_balance + amount

# does the actual withdrawl with overdraft check
def withdrawl(amount, account):
    global checking_balance, savings_balance
    if account == "1":
        if amount <= checking_balance:
            checking_balance = checking_balance - amount
        else:
            print("You cannot overdraft your checking account.")
    elif account == "2":
        if amount <= savings_balance:
            savings_balance = savings_balance - amount
        else:
            print("You cannot overdraft your savings account.")

# does the balance transfer
# gets the account from and to and validates values
def transfer_balance():
    global checking_balance, savings_balance
    account_from = "0"

    # get a valid from account
    while (account_from != "1") and (account_from != "2"):
        print("\n1. Checking Account")
        print("2. Savings Account")
        account_from = input("Choose an account to transfer from: ")

    account_to = "0"
    display_string = ""
    # builds the string for the from account option
    if account_from == "1":
        display_string = "1. Savings Account"
    else:
        display_string = "1. Checking Account"

    # gets a valid to account
    while account_to != "1":
        print(display_string)
        account_to = input("Choose an account to transfer to: ")

    # amount to transfer
    amount = float(input("How much would you like to transfer? "))

    #check for coins!
    if not has_coins(amount):
        # I know this AND check isn't technically necessary but it
        # lays the foundation for a 3rd account or more.
        if (account_from == "1") and (account_to == "1"):
            if amount <= checking_balance:
                checking_balance = checking_balance - amount
                savings_balance = savings_balance + amount
            else:
                print("You cannot overdraft your checking account.")
        elif (account_from == "2") and (account_to == "1"):
            if account <= savings_balance:
                savings_balance = savings_balance - amount
                checking_balance = checking_balance + amount
            else:
                print("You cannot overdraft your savings account.")
    else:
        print("Transactions must be in whole dollar amounts.")


# main program loop
while not quit:

    # check if the user is logged in. Validate if false.
    if not logged_in:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if (username == username_input) and (password == password_input):
            logged_in = True
            print("Welcome Robert Brown")
        else:
            quit = True
            break

    # show the current balances
    print("\nCurrent Balances:")
    showInfo()

    account = 0

    valid_selection = False
    selection = "0"

    # get the user's choice for what they want to do
    # will continue to loop until they get a valid choice
    while not valid_selection:
        print("\n1. Deposit")
        print("2. Withdrawl")
        print("3. Balance Inquiry")
        print("4. Transfer Balance")
        print("5. Log Out")
        selection = input("What would you like to do today? ")


        if (selection != "1") and (selection != "2") and (selection != "3") and (selection != "4") and (selection != "5"):
            print("That was not a valid selection.")
        else:
            valid_selection = True

    # I wish python had switch statments... :(
    if selection == "1":
        deposit_or_withdrawl("deposit")
        showInfo()
    elif selection == "2":
        deposit_or_withdrawl("withdrawl")
        showInfo()
    elif selection == "3":
        transfer_balance()
        showInfo()
    elif selection == "4":
        showInfo()
    elif selection == "5":
        quit = True
        break


    q = input("Would you like to perform another action? (Y/N)")
    if(q.lower() != "y"):
        quit = True
        break


print("Have a great day!")