# ATM banking details
balance = 10000
transactions = []

# Function to check account balance
def check_balance():
    print(f"\nCurrent Balance: Rs.{balance}\n")

# Function to deposit money
def deposit_money():
    global balance

    amount = float(input("Enter amount to deposit: Rs."))

    if amount <= 0:
        print("Amount must be greater than zero!\n")
        return

    balance += amount
    transactions.append(f"Deposited: Rs.{amount}")

    print(f"Rs.{amount} deposited successfully!")
    print(f"Updated Balance: Rs.{balance}\n")

# Function to withdraw money
def withdraw_money():
    global balance

    amount = float(input("Enter amount to withdraw: Rs."))

    if amount <= 0:
        print("Amount must be greater than zero!\n")
        return

    if amount > balance:
        print("Insufficient balance!\n")
        return

    balance -= amount
    transactions.append(f"Withdrawn: Rs.{amount}")

    print(f"Rs.{amount} withdrawn successfully!")
    print(f"Remaining Balance: Rs.{balance}\n")

# Function to show transaction history
def show_transactions():
    if not transactions:
        print("No transactions available.\n")
    else:
        print("\n--- Transaction History ---")

        for transaction in transactions:
            print(transaction)

        print()

# Main loop
while True:
    print("0. Exit")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Transaction History")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Thank you for using the ATM Banking System!")
        break
    elif choice == "1":
        check_balance()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        show_transactions()
    else:
        print("Invalid choice, try again.\n")
