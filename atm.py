# ATM Program
# By Daniel Clancy
# v1.0 Updated 12-15-2020
# This program is a simulation of how an ATM works without the whole GUI layer

# I fully acknowledge that my use of global variables is not best practice, but python is not my primary programming language and I'm tired.

import math

# We're going to use parallel lists to mock up a database for the user information

# list of usernames
USERS = ["rbrown", "lwhite", "mblack", "dclancy2@ivytech.edu"]

# Yeah yeah, I know. Plain text passwords bad. But this isn't a real ATM
PASSWORDS = ["blue123", "red456", "green789", "C06259431"]

# list of names!
NAMES = ["Robert Brown", "Lisa White", "Mark Black", "Daniel Clancy"]

# account balances
SAVINGS_BALANCES = [2500, 500, 750, 600]
CHECKING_BALANCES = [35, 1250, 200, 900]


# set some global maximums
MAX_TRANSACTIONS = 3
TRANSACTION_MAXIMUM_AMOUNT = 500


quit = False
logged_in = False


# initial variable values
savings_balance = 0
checking_balance = 0
transactions = 0

users_name = ""

# Function to log the user in
def user_login():
    global logged_in, savings_balance, checking_balance, users_name
    username = input("Username: ")
    password = input("Password: ")

    if username in USERS:
        if password == PASSWORDS[USERS.index(username)]:
            logged_in = True
            savings_balance = SAVINGS_BALANCES[USERS.index(username)]
            checking_balance = CHECKING_BALANCES[USERS.index(username)]
            users_name = NAMES[USERS.index(username)]
        else:
            print("Incorrect username or password")
    else:
        print("Incorrect username or password")

# Displays the account balance info
def showInfo():
    print(f"Checking account: ${checking_balance}")
    print(f"Savings account: ${savings_balance}\n")
    print(f"Number of transactions this session: {transactions}")

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
    if amount < TRANSACTION_MAXIMUM_AMOUNT:
        if not has_coins(amount):
            if transaction_type == "deposit":
                deposit(amount, account)
            elif transaction_type == "withdrawl":
                withdrawl(amount, account) 
        else:
            print("Transactions must be in whole dollar amounts.")
    else:
        print("Transactions must be less than $500.")
    

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

    if amount < TRANSACTION_MAXIMUM_AMOUNT:
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
    else:
        print("Transactions must be less than $500.")



# main program loop
# so long as the user doesn't want to quit and the max transactions per session isn't exceeded
# we will run the loop
while (not quit) and (transactions < MAX_TRANSACTIONS):

    # check if the user is logged in. Validate if false.
    if not logged_in:
        user_login()

    # greet the users

    print(f"Hello {users_name}!")
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

    transactions = transactions + 1

    # I wish python had switch statments... :(
    # Take the users request and do the appropriate action
    if selection == "1":
        deposit_or_withdrawl("deposit")
        showInfo()
    elif selection == "2":
        deposit_or_withdrawl("withdrawl")
        showInfo()
    elif selection == "3":
        showInfo()
    elif selection == "4":
        transfer_balance()
        showInfo()
    elif selection == "5":
        quit = True
        break

    # We only need to ask if they haven't exeeded the max allowed transactions per session
    if transactions < MAX_TRANSACTIONS:
        q = input("Would you like to perform another action? (Y/N)")
        if(q.lower() != "y"):
            quit = True
            break


print("Have a great day!")