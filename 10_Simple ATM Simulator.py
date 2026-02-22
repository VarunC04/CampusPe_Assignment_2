# Q10: Simple ATM Simulator
# Simulates ATM menu with balance checks and conditions.

def atm_simulator():
    account_balance = 10000  # initial balance

    while True:
        print("\n===== ATM SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            menu_choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter 1–4.")
            continue

        # Option 1: Check balance
        if menu_choice == 1:
            print("Current Balance: ₹", account_balance)

        # Option 2: Deposit
        elif menu_choice == 2:
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid amount!")
                continue

            if deposit_amount <= 0:
                print("Amount must be positive.")
                continue

            account_balance += deposit_amount
            print("Deposit successful!")
            print("New Balance: ₹", account_balance)

        # Option 3: Withdraw
        elif menu_choice == 3:
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount!")
                continue

            if withdraw_amount <= 0:
                print("Amount must be positive.")
                continue

            if withdraw_amount > account_balance - 500:
                print("Insufficient balance! Minimum ₹500 required.")
                continue

            account_balance -= withdraw_amount
            print("Withdrawal successful!")
            print("New Balance: ₹", account_balance)

        # Option 4: Exit
        elif menu_choice == 4:
            print("Thank you! Exiting ATM.")
            break

        else:
            print("Invalid choice! Choose between 1–4.")

atm_simulator()
