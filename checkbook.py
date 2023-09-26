#code without any comment: look at comments.ipynb to understand code
import os
import subprocess

checkbook = 'balance.txt'

balance = 0

# Check and read file
def load_checkbook():
    global balance
    if os.path.exists(checkbook):
        with open(checkbook, "r") as file:
            balance = float(file.readline())

# function to save the balance to 'balance.txt'
def save_checkbook():
    with open(checkbook, "w") as file:
        file.write(str(balance))
        
# function for current balance
def current_balance():
    print(f"Current Balance: ${balance}")
    
    
    
# add_debit (withdrawal) function:
def add_debit():
    global balance
    amount = float(input("How much money would you like to withdrawal: $"))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"Withdrawing: ${amount:.2f}")
            save_checkbook()
        else:
            print("Insufficient balance. You dont have enough funds to withdrawal")
    else:
        print("Invalid amount. Please enter a positive amount.")
        
        

# add_credit (deposit) function:
def add_credit():
    global balance
    amount = float(input("How much money would you like to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Depositing: ${amount:.2f}")
        save_checkbook()
    else:
        print("Invalid amount. Please enter a positive amount.")
        

load_checkbook()
print(' ~~~ Welcome to your terminal checkbook! ~~~')

while True:
    print("\nMenu:")
    print("1. View current balance")
    print("2. Add a debit (withdrawal)")
    print("3. Add a credit (deposit)")
    print("4. Exit")

    choice = input("Please make a choice: ")

    if choice == "1":
        current_balance()
    elif choice == "2":
        add_debit()
    elif choice == "3":
        add_credit()
    elif choice == "4":
        print("Exiting Aplication. Goodbye!")
        print(f"Your balance is:  ${balance:.2f}")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")