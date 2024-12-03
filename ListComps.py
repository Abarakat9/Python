nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList = [n for n in nums]
print(myList)

myList = [n*n for n in nums]
print(myList)

myList = [n for n in nums if n%2 == 0]
print(myList)

myList = [(letter, num) for letter in 'abcd' for num in range(4)]
print(myList)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)

myDict = {name: hero for name, hero in zip(names, heros)}
print(myDict)

# Set comprehensions

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
mySet = {n for n in nums}
print(mySet)