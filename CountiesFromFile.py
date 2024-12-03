# @author Ahmad Barakat
def main():
    # Create three empty lists named countyNames, countySeats, and countyPops
    countyNames = []
    countySeats = []
    countyPops = []

    state = input("Get county data for which state: ")

    #Call getCountyData with the state and the lists
    getCountyData(state, countyNames, countySeats, countyPops)

    EXIT = "4"
    choice = "0"
    while (choice != EXIT):
        print("(1) Show statistical summary")
        print("(2) Show counties within a given population range")
        print("(3) Show counties beginning with a certain letter")
        print("(4) Exit")

        choice = input("Choice? ")

        if choice == '1':
            showStatSummary(state, countyNames, countySeats, countyPops)
            print()
        elif choice == '2':
            lowerBound = int(input("Lower bound: "))
            upperBound = int(input("Upper bound: "))
            showPopulationRange(lowerBound, upperBound, countyNames, countySeats, countyPops)
            print()
        elif choice == '3':
            letter = input("Show counties beginning with which letter? ").upper()
            showCountySubset(letter, countyNames, countySeats, countyPops)
            print()
    print()
    
# getCountyData reads county data from a given state's file into the list
# parameters. The county name, its seat, and its population will be stored
# at the same index in each of the three different lists.
# @param state The name of the state for which data is to be read
# @param countyNames Will be filled with the state's county names
# @param countySeats Will be filled with the seat for each county
# @param countyPops Will be filled with populations for each county
def getCountyData(state, countyNames, countySeats, countyPops):

    if not (len(countyNames) == len(countySeats) == len(countyPops)):
        raise ValueError

    if state.lower() == "kansas":
        filename = "KansasCountyData.txt"
    elif state.lower() == "iowa":
        filename = "IowaCountyData.txt"
    
    #open file for reading
    import csv
    with open(filename, mode='r') as file:
        csvReader = csv.reader(file)

        #skip header line
        next (csvReader, None)
    
        for row in csvReader:
            countyNames.append(row[0])
            countySeats.append(row[1])
            countyPops.append(int(row[2]))
    
# showStatSummary displays the state population, the number of counties, and
# the average county population.
# @precondition countyNames, countySeats, and countyPops are parallel
# @param state The name of the state
# @param countyNames The county names for the state
# @param countySeats The county seats for the state
# @param countyPops The county populations for the state
def showStatSummary(state, countyNames, countySeats, countyPops):

    if not (len(countyNames) == len(countySeats) == len(countyPops)):
        raise ValueError
    
    print(f"Statistics for {state}")
    print(f"State population: {sum(countyPops):,}")
    print(f"Number of counties: {len(countyNames)}")
    print(f"Average county population: {sum(countyPops) / len(countyNames):,.0f}")


# showPopulationRange shows county information for those county populations
# within a given population range.
# @precondition countyNames, countySeats, and countyPops are parallel
# @param lowerBound The inclusive lower bound for the range
# @param upperBound The inclusive upper bound for the range
# @param countyNames The county names for the state
# @param countySeats The county seats for the state
# @param countyPops The county populations for the state

def showPopulationRange(lowerBound, upperBound, countyNames, countySeats, countyPops):
    
    if not (len(countyNames) == len(countySeats) == len(countyPops)):
        raise ValueError
     
    for i in range(len(countyPops)):
        if lowerBound <= countyPops[i] <= upperBound:
            print(f"{countyNames[i]},{countySeats[i]},{countyPops[i]}")

# showCountySubset shows county information for those county names
# beginning with a given letter.
# @precondition countyNames, countySeats, and countyPops are parallel
# @param letter The first letter to match
# @param countyNames The county names for the state
# @param countySeats The county seats for the state
# @param countyPops The county populations for the state
def showCountySubset(letter, countyNames, countySeats, countyPops):

    if not (len(countyNames) == len(countySeats) == len(countyPops)):
        raise ValueError
    
    for i in range(len(countyNames)):
        if countyNames[i][0] == letter:
            print(f"{countyNames[i]},{countySeats[i]},{countyPops[i]}")
    
main()
