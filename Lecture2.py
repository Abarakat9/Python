myInt = 3
myFloat = 3.0
myString = 'xyz'
myString = 'abc'
myBool = True
myBool = False
SALES_TAX_RATE = 0.91
FREEZING_IN_C = 0
BOILING_IN_C = 0
MAX_ENTRIES = 10

# Arithmetic Operators
Negation = "-"
Exponents = "**"
Addition = '+'
subtraction = '-'
multiplication = '*'
Division = '/'
FloorDivision = '//' # Whole numbers, nearest int to the number
RemainderModulus = '%'
print(5 % 2)

floatVar = 2.0
intVar = -4
print(floatVar + intVar ** 3)
print(intVar - floatVar / 2)
print(intVar * int(floatVar))

x = 5
x = x - 8
y = 2
z = 4
x = y / z + y * z

#Compound Operator!!!

price = 30
discount = 2
price = price - discount
price -= discount

result = 97
scale = 4
result = result * scale
result *= scale


numScores = 21
result / numScores
result /= numScores

# Compound Operators First Program

#Get the integer
number = int(input('Enter an integer: '))

#Modify the integer
increase = int(input("Increase the integer by how much? "))
number += increase
multiplier = int(input("Now, multiply by how much? "))
number += multiplier

#Display the final value
print("Final Value: ", number)
x = 2
x *= 2 + 3 * 2
print(x)