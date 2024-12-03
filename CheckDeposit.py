# This program processes bank account checks
# and prevents a negative balalnce.
# @author Ahmad Barakat

balance = float(input("Please enter a balance: $"))
print()
checkAmount = 1
while checkAmount > 0:
    checkAmount = float(input("Check amount (0 or negative to end): $"))

    if checkAmount > 0:
        # Accept check amt smaller than balance
        if (checkAmount > balance):
            print("Warning: Check will bounce. No transaction occured.\n")
        else:
            balance -= checkAmount
            print(f"Current balance: ${balance:,.2f}\n")

# Display final balance
print(f"\nFinal balance: ${balance:,.2f}")