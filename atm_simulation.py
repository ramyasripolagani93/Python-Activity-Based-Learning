balance = float(input("Enter starting balance: "))

if balance < 0:
    print("Balance cannot be negative.")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("Available balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                balance = balance + amount
                print("New balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance = balance - amount
                print("New balance:", balance)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid option.")