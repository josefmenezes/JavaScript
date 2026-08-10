print("ATM Withdrawal System")

while True:
    amount = int(input("How much has to be withdrawn (Enter 0 to exit): "))

    
    if amount == 0:
        break

    if amount < 0:
        print("Invalid Amount!\n")
        continue

    if amount > 10000:
        print("Transaction limit exceeded! Maximum withdrawal is $10,000.\n")
        continue

    
    print(f"Withdrawal amount: ${amount}")
    break 

print("\nThank you for using the ATM!")
p