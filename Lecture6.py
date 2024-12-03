import math

limit = int(input("Please enter a number:"))

i = 1
sum = 0
while i <= limit:
    sum += i
    i += 1
print(f'The sum of the integers from 1 to {limit} is {sum}')

state_tax_rate = 0.065

salary = int(input("Please enter a salary (-1 to quit: )"))
while salary >= 0:
    incomeTax = salary * state_tax_rate
    print(f'Your tax: ${incomeTax:,.2f}')
print("Done")
value = 0.1
while not math.isclose(value, 1.0):
    print(f'Value: {value:.1f}')
    value += 0.1
print('the end')

halfLife = 0
amt = 1000
while amt > 0.0005:
    amt /= 2
    halfLife += 1
print(halfLife)

response = 'Y'
while response.upper()[0] == 'Y':
    temp = int(input("Enter the temp in F: "))
    temp = (temp - 32) * (5/9)
    print(f'{temp}C')
    response = input("Do you want to continue (Y/N)? ")

i = 0
count = 0
while count > 10:
    print(i)
    print(f"the square of {i} is {i*i}")
    i += 2
    count -= 1

print("Enter integers, enter 9999 to quit")
sum = 0
count = 0

num = int(input("Enter integer: "))
min = num
max = num
while num != 9999:
    if (num < min):
        min = num
    elif (num > max):
        max = num
    sum += num
    count += 1
    num = int(input("Enter integer: "))
print(f"Average is: {sum / count}")
print(f"The min is: {min}")
print(f"The max is: {max}")