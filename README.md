#Interactive ATM Banking Simulation(Python)
This script simulates a simple ATM machine. It prompts the user to insert a card, then asks for a PIN. If the correct PIN is entered, the user can perform various banking operations such as checking balance, withdrawing money, depositing money, or exiting the system.

Breakdown of the Script:

Importing the time Module
import time
The time module is imported to use the sleep function, which delays the execution of the program.

Prompting User to Insert Card
print("Please insert your CARD")
time.sleep(5)
The script prints a message to prompt the user to insert their card and then pauses for 5 seconds to simulate the time taken for this action.

Setting Up Password and Initializing Balance
password = 1234
balance = 5000
password is set to 1234, which is the correct PIN for accessing the ATM.
balance is initialized to 5000, representing the initial account balance.
Requesting PIN Input

pin = int(input("Enter your pin:"))
The script asks the user to enter their PIN. It converts the input from a string to an integer.

Checking the PIN
if pin == password:
The script checks if the entered PIN matches the preset password (1234).

ATM Menu Loop
while True:
    print("""
    1 == balance
    2 == withdraw amount
    3 == deposit balance
    4 == exit
    """)
If the PIN is correct, the script enters a while True loop, presenting the user with a menu of options.

Handling Menu Options
try:
    option = int(input("Please enter your choice:"))
The script prompts the user to choose an option from the menu and converts their choice into an integer.

Checking Balance
if option == 1:
    print(f"Your current balance is {balance}")
If the user selects option 1, the script prints the current balance.

Withdrawing Money
elif option == 2:
    withdraw_amount = int(input("Please enter withdraw amount:"))
    if withdraw_amount > balance:
        print("Insufficient funds!")
    else:
        balance -= withdraw_amount
        print(f"{withdraw_amount} is debited from your account.")
If the user selects option 2, they are prompted to enter the amount they want to withdraw.
The script checks if there are sufficient funds. If not, it prints an "Insufficient funds!" message.
If funds are sufficient, it debits the amount from the balance and updates the account balance.

Depositing Money
elif option == 3:
    deposit_amount = int(input("Please enter deposit amount:"))
    balance += deposit_amount
    print(f"{deposit_amount} is credited to your account.")
If the user selects option 3, they are prompted to enter the amount they wish to deposit.
The script credits the deposit amount to the balance and prints a confirmation message.

Exiting the System
elif option == 4:
    print("Exiting the system. Have a nice day!")
    break
If the user selects option 4, the script prints a goodbye message and breaks out of the loop, effectively exiting the ATM system.

Handling Invalid Options
else:
    print("Invalid option. Please try again.")
If the user enters an invalid option, the script informs them and prompts them to try again.

Handling Non-Numeric Input
except ValueError:
    print("Invalid input. Please enter a numeric value.")
If the user enters non-numeric input where a number is expected, a ValueError is caught, and the script prompts the user to enter a numeric value.


Handling Incorrect PIN
else:
    print("Wrong pin, please try again with the correct pin :(")
If the entered PIN does not match the preset password, the script prints an error message indicating the PIN is incorrect.


Summary
The script simulates a basic ATM system where users can check their balance, withdraw and deposit money, and exit the system. It includes error handling to manage incorrect or non-numeric inputs, and it provides a user-friendly interface for interacting with the ATM.
