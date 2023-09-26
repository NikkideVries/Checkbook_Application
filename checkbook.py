#code without any comment: look at comments.ipynb to understand code. Grade this code.
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
    amount_str = input("How much money would you like to withdrawal: $")
    
    # Check if the input is a valid number
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        
        # Check if the amount is positive
        if amount > 0:
            # Check if there is sufficient balance
            if amount <= balance:
                balance -= amount
                print(f"Withdrawing: ${amount:.2f}")
                save_checkbook()
            else:
                print("Insufficient balance.")
        # the number cannot be less that zero
        else:
            print("Invalid amount. Please enter a positive value.")
    # the input cannot be a string or other ivalid inputc
    else:
        print("Invalid input. Please enter a valid number.")
        
        

# add_credit (deposit) function:
def add_credit():
    global balance
    amount_str = input("How much money would you like to deposit: ")
    
    # Check if the input is a valid number
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        
        # Check if the amount is positive
        if amount > 0:
            balance += amount
            print(f"Depositing: ${amount:.2f}")
            # this will update the checkbook balance and input the new value
            save_checkbook()
        else:
            print("Invalid amount. Please enter a positive value.")
    else:
        print("Invalid input. Please enter a valid number.")

# exit function: 
def exit_program():
    global balance
    save_checkbook()
    print("\nExiting Aplication. Goodbye!")
    print(f"Your balance is:  ${balance:.2f}\n")
    exit()        

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
        exit_program()
        #break
    else:
        print("Invalid choice. Please select a valid option (1-4).")