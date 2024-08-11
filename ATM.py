import time

print("Please insert your CARD")
time.sleep(5)

password = 1234
pin = int(input("Enter your pin:"))

print("============================================================")
print("============================================================")

balance = 5000

if pin == password:
    while True:
        print("""
        1 == balance
        2 == withdraw amount
        3 == deposit balance
        4 == exit
        """)

        print("============================================================")
        print("============================================================")

        try:
            option = int(input("Please enter your choice:"))

            if option == 1:
                print(f"Your current balance is {balance}")
                print("============================================================")
                print("============================================================")

            elif option == 2:
                withdraw_amount = int(input("Please enter withdraw amount:"))

                if withdraw_amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print("============================================================")
                    print("============================================================")
                    print(f"Your current balance is {balance}")
                    print("============================================================")
                    print("============================================================")

            elif option == 3:
                deposit_amount = int(input("Please enter deposit amount:"))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print("============================================================")
                print("============================================================")
                print(f"Your updated balance is {balance}")
                print("============================================================")
                print("============================================================")

            elif option == 4:
                print("Exiting the system. Have a nice day!")
                break

            else:
                print("Invalid option. Please try again.")
                print("============================================================")
                print("============================================================")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            print("============================================================")
            print("============================================================")

else:
    print("Wrong pin, please try again with the correct pin :(")
