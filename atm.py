import math

quit = False
logged_in = False

username = "rbrown"
password = "blue123"

savings_balance = 2500.00
checking_balance = 35.00

def showInfo():
    print(f"Checking account: ${checking_balance}")
    print(f"Savings account: ${savings_balance}\n")

showInfo()

while not quit:
    if not logged_in:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if (username == username_input) and (password == password_input):
            logged_in = True
            print("Welcome Robert Brown")
        else:
            quit = True
            break

    print("\nCurrent Balances:")
    print(f"Checking Account - ${checking_balance}")
    print(f"Savings Account  - ${savings_balance}")

    account = 0

    while (account != "1") and (account != "2"):
        print("\n\n1. Checking")
        print("2. Savings")
        account = input("Which account would you like to make a deposit? ")


        if (account != "1") and (account != "2"):
            print("You did not select a valid account. Try again.\n")



    deposit = float(input("How much would you like to deposit? "))
    if deposit < 0:
        print("You cannot deposit an amount less than 0")
    elif (deposit - math.floor(deposit)) != 0:
        print("Transactions must be in whole dollar amounts.")
    else:
        if account == "1":
            checking_balance = checking_balance + deposit
            showInfo()
        else:
            savings_balance = savings_balance + deposit
            showInfo()


    q = input("Would you like to perform another action? (Y/N)")
    if(q.lower() != "y"):
        quit = True


print("Have a great day!")