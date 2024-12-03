def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myList = [n for n in nums ]
    print(myList)
    myList = [n for n in nums if n % 2 == 0]
    # print(myList)
    myList.append(1)
    if 10 in myList:
        myList.remove(10)
    myList.insert(3, -4)
    myList.pop(1)
    sum = 0
    for i in range(len(myList)):
        sum += myList[i]
    # print(sum)
    # print(myList)
    modifyList(myList)
    print(myList)
    
    myDict = {"Ahmad": 25, "Noelle": 23, "Asta": 17, "Yuno": 18}
    print(modifyDict(myDict))

    
def modifyList(myList):
    amt = [4, 3, 21, 19, -9, 9]
    for i in range(len(amt)):
        myList.append(amt[i])
    myList.sort()
    return myList

def modifyDict(myDict):
    alpha = 'aeiou'
    for key in myDict:
        for letter in alpha:
            if letter in key:
                print(f"The letter {letter} is in {key}")
            else:
                print(f"The letter {letter} is not in {key}")
    print(myDict.keys())
    print(myDict.values())
    for value in myDict.values():
        if value < 18:
            print(f"{key}, {value} is not of legal age.")
    for key, value in myDict.items():
        print(f"Name: {key} Age: {value}")
    myDict['Ahmad'] = 11
    return myDict
main()