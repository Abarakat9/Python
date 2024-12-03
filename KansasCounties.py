# @author Ahmad Barakat
def main():
    countyNames = ["Chase", "Crawford", "Ford", "Harper", "Kiowa",
    "McPherson", "Norton", "Republic", "Shawnee", "Wabaunsee"]
    countySeats = ["Cottonwood Falls", "Girard", "Dodge City", "Anthony",
    "Greensburg", "McPherson", "Norton", "Belleville",
    "Topeka", "Alma", ]
    countyPops = [2572, 38972, 34287, 5485, 2460,
    10038, 5459, 4674, 178909, 6877]
    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty to insert: ").title()
    seat = input(f"{name} County seat: ")
    pop = int(input(f"{name} County population (digits only): "))

    index = findInsertionIndex(countyNames, name)
    if index == len(countyNames):
        countyNames.append(name)
        countySeats.append(seat)
        countyPops.append(pop)
    else:
        countyNames.insert(index, name)
        countySeats.insert(index, seat)
        countyPops.insert(index, pop)
    
    print(countyNames)

    print()

    showCountyData(countyNames, countySeats, countyPops)
    name = input("\nCounty requiring population adjustment: ").title()
    index = linearSearch(countyNames, name)
    if index != -1:
        print(f"Current population of {name}: {countyPops[index]:,}")
        newPop = int(input("Enter the new population: "))
        countyPops[index] = newPop
    else:
        print(f"{name} County was not found")

    print()
    showCountyData(countyNames, countySeats, countyPops)    

# showCountyData displays the data for the given counties
# @param countyNames The list of county names
# @param countySeats The list of county seats
# @param countyPops The list of county populations
def showCountyData(countyNames, countySeats, countyPops):
    for i in range(len(countyNames)):
        print(countyNames[i])
        print(f"    Seat: {countySeats[i]}")
        print(f"    Population: {countyPops[i]:,}")

# findInsertionIndex finds the index where value is to be inserted
# into the list.
# @precondition The list of values is in increasing sorted order
# @param theList The list of values
# @param value the value to insert
# @return the located index
def findInsertionIndex(theList, value):
    for i in range(len(theList)):
        if value < theList[i]:
            return i
    return len(theList)

def linearSearch(countyNames, targetName):
    for i in range(len(countyNames)):
        if countyNames[i] == targetName:
            return i
    return -1
    



main()