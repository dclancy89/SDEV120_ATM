import math

quit = False

balance = 2500

def showInfo():
    print("Customer: Robert Brown")
    print("Username: rbrown")
    print(f"Account Balance: ${balance}\n")

showInfo()

while not quit:
    deposit = float(input("How much would you like to deposit? "))
    if(deposit < 0):
        print("You cannot deposit an amount less than 0")
    else:
        balance = balance + deposit
        showInfo()


    q = input("Would you like to perform another action? (Y/N)")
    if(q.lower() != "y"):
        quit = True


print("Have a great day!")