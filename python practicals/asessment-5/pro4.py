balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Transaction successful")
else:
    print("Insufficient balance")