from math import sqrt


aLongStr = 'Four score and seven years ago this contenent, ' + \
    'a new nation, conceived in Liberty, and dedicated '
print(aLongStr)

temperature = 20
windSpeed = 15
windChill = (35.74 + 0.6215 * temperature - 35.75 * pow(windSpeed, 0.16) +
              0.4275 * temperature * pow(windSpeed, 0.16))
print(round(windChill, 2))
myString = "Today is a good day!"
str1 = ""
print(myString[2])

husband = 'Jim'
wife = 'Laurie'
addressNumber = 12345
print(husband + " & " + wife)
print(husband[0] + " & " + wife[0])
print(len(husband))
print(len("husband"))
print("_" + "Echo-" * 5)
print(str(addressNumber) + " College Blvd")
print("She said, 'Touchdown Chiefs!'")
print('She said, "Touchdown Chiefs!"')

SALES_TAX_RATE = 0.081

#get the item and the price
itemName = input("Enter the item's name: ")
itemCost = float(input("Enter the " + itemName + "'s price $"))

#calculate and display the total cost
totalCost = itemCost + itemCost * SALES_TAX_RATE

print(f"Total Cost: ${totalCost:,.2f}")

# pet
petName = "Shadow"
weight  = 22.5
height = 20
print(f'{petName}: {weight} lbs, {height}" tall.')
print(f'{petName:s}: {weight:f} lbs, {height:d}" tall.')
output = f'{weight:.2f} lbs, {height + 2:d}" tall.'
print(output)

school = "Iowa State"
print(school)
school = school.upper()
print(school)
school = school.replace('IOWA', 'KANSAS')
print(school)
school = school.replace('S', 'Z')
print(school)
print()


leg1 = int(input("Enter the first leg of the triangle: "))
leg2 = int(input("Enter the second leg of the triangle: "))

hyp = sqrt(leg1 ** 2 + leg2 ** 2)
print(f'The hypotenuse of the triangle is {hyp:.2f}')

#get temp in F
tempF = int(input("The temperature in Fahrenheit is: "))
#convert temp to C
tempC = (tempF - 32) * 5/9

# output the C temp
print(f"The temperature in Celsius is {tempC:.2f}")


#coins
numCents = int(input("Enter total cents: "))
#calc quarters
numQ = numCents // 25
numCents = numCents %25
#calc dimes
numD = numCents // 10
numCents = numCents % 10
#calc nickels
numN = numCents // 5
numCents = numCents % 5
#output results
if (numQ > 0):
    print(f'{numQ} Quarters', end="")
    if (numQ > 1):
        print(f's', end="")
    print(f'; ', end="")
if (numD > 0):
    print(f'{numD} Dimes')
    if (numD > 1):
        print(f's')
    print(f'; ', end="")
if (numN > 0):
    print(f'{numN} Nickels')
    if (numN > 1):
        print(f's')
    print(f'; ', end="")
if (numCents > 0):
    if (numCents == 1):
        print(f'{numCents} Penny')
    else:
        print(f'{numCents} Pennies')
