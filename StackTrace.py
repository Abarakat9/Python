def main():
    numbers = [num for num in range(11) if num%2 != 0]
    tot = someFun(numbers)
    print(numbers, tot)

def someFun(aList):
    addThree(aList, 0)
    addThree(aList,2)
    total = 0
    for num in aList:
        total += num
        return total

def addThree(myList, ndx):
    myList[ndx] += 3

main()

# Stack Info        Stack Vars      Stack Var Vals
# Function name     main            4
# Return Line #     
# Return Value      
# Function name     
# Return Line #     
# Return Value      
# Function name     
# Return Line #     
# Return Value      
# Function name     
# Return Line #     
# Return Value      
# Heap      
# Addy Value        
