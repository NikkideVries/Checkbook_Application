import os 
import subprocess


# Functions:
# view current balance

balance = 0
def current_balance(balance):
    print(f"Your current balance is: ${balance}")

    
    
# add_debit: withdrawal
def add_debit(balance):
    balance -= debit_amount
    print(f"Your current balance is:$ {balance}")
    with open('balance.txt', 'w') as f:
        f.write(f"{debit_amount}")
    return balance



# add_credit: deposit
def add_credit(balance):
    balance += credit_amount
    print(f"Your current balance is:$ {balance}")
    with open('balance.txt', 'w') as f:
        f.write(f"{debit_amount}")
    return balance

# user input funciton


while True:
    print('\n~~~ Welcome to your terminal checkbook! ~~~')
    print()
    print("What would you like to do?\n")
    print(" 1. View Current Balance") 
    print(" 2. Add a Debit (withdrawal)")
    print(" 3. Add a Credit (deposit)")
    print(" 4. Exit the Application\n")

    choice = input("Please select a choice:")

    if choice == "1":
        current_balance(balance)

    elif choice == "2":
        debit_amount = float(input("Enter the amount you would like to withdrawl: $"))
        balance = add_debit(balance)

    elif choice == "3":
        credit_amount = float(input("Enter the amount you would like to deposit: $"))
        balance = add_credit(balance)

    elif choice == "4":
        break
    else:
        print("Invalid Input")


print("Exiting the Application. Goodbye!")


