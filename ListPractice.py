# This program will provide practice with list creation,
# access, and manipulation
# @author Ahmad Barakat

from random import randint

def main():
    MAX_LIST_SIZE = 20
    LOW_VALUE = 1
    HIGH_VALUE = 50

    size = int(input(f"How many values up (up to {MAX_LIST_SIZE}) to generate? "))
    while size < 1 or size > MAX_LIST_SIZE:
        size = int(input(f"How many values up (up to {MAX_LIST_SIZE}) to generate? "))
    
    data = []
    for i in range(size):
        data.append(randint(LOW_VALUE, HIGH_VALUE))
    data.sort()
    
    for num in data:
        print(num, end=" ")

    min_value = data[0]
    max_value = data[-1]

    print()
    print("\nDisplay all values between what inclusive range?")
    lowerBound = int(input("Lower bound: "))
    while lowerBound < min_value:
        lowerBound = int(input("Lower bound: "))
    upperBound = int(input("Upper bound: "))
    while upperBound > max_value:
        upperBound = int(input("Upper bound: "))

    for num in data:
        if lowerBound <= num <= upperBound:
            print(num, end=" ")
    print()
    
    print("\nHistogram")
    for num in data:
        hist = ((num + 1) // 2) * "*"
        print(f"{num}: {hist}")

main()
