# Banking System Simulation
# This program simulates a simple banking system
# @author Ahmad Barakat


def main():
    balance = 1500
    choice = getMenuChoice()
    while True:
        choice = getMenuChoice()
        if (choice != "E"):
            if (choice == "W"):
                balance = processWithdrawal(balance)

            elif (choice == "D"):
                balance = processDeposit(balance)

            elif (choice == "B"):
                print(f"Current balance: {balance:,.2f}")
                print()
        else:
            print("Thank you for banking with us.")
            print()
            return


# getMenuChoice presents a banking menu of choices
# @return The customer's menu choice as a single upper
#   case letter.
def getMenuChoice():

    print("="*20)
    print("Enter W for Withdraw")
    print("Enter D for Deposit")
    print("Enter B for Balance")
    print("Enter E for Exit")
    print("="*20)
    choice = input("Please enter your menu choice: ").upper()
    return choice


# processWithdrawal pricesses a customer's withdrawal
# @param balance The current balance
# @return the updated balance

def processWithdrawal(balance):
    withdrawAmt = float(input("Enter withdrawal amount: $"))
    if (withdrawAmt <= 0 ):
        print("Improper withdraw amount entered.")
    elif (withdrawAmt > balance):
        print("Insufficient funds.")
    else:
        balance -= withdrawAmt
        print(f"Please take your ${withdrawAmt:,.2f}")
    print()

    return balance


# processDeposit processes a customer's deposit
# @param balance The current balance
# @return The updated balance

def processDeposit(balance):
    deposit = float(input("Enter deposit amount: $"))
    if (deposit <= 0):
        print("Improper deposit amount entered.")
    else:
        balance += deposit
        print(f"${deposit:,.2f} deposited.")
    print()

    return balance

main()