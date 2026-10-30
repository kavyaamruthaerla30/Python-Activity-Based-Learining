balance = float(input("Opening balance: "))
n = int(input("Number of transactions: "))
successful = 0

if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count")
else:
    for i in range(n):
        kind = input("Transaction type (D/W): ").upper()
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif kind == "D":
            balance += amount
            successful += 1
        elif kind == "W" and amount <= balance:
            balance -= amount
            successful += 1
        elif kind == "W":
            print("Insufficient balance")
        else:
            print("Invalid transaction type")
    print(f"Final balance: Rs. {balance:.2f}")
    print(f"Successful transactions: {successful}")
