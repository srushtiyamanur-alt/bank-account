name = input("Enter customer name: ")
balance = float(input("Enter initial balance: "))

deposit = float(input("Enter deposit amount: "))
balance += deposit

withdraw = float(input("Enter withdrawal amount: "))
if balance - withdraw >= 2000:
    balance -= withdraw
    print(f"Withdrawal successful. Updated Balance for {name}: Rs. {balance:.2f}")

