school = 'University of Kansas'
numCaps = 0

for ndx in range(len(school)):
    if school[ndx].isupper():
        numCaps += 1
print(f'Number of caps: {numCaps}')

myStr = 'abcdefg'

for ndx in range(len(school)):
    print(school[ndx], end="")
print()
for ndx in range(len(school), 0, -1):
    print(school[ndx-1], end="")

# () parentheses means you dont include outer last number
# [] brackets include all numbers listed
print()

LIMIT = 3
for i in range(1, LIMIT+1):
    print(i)
print("finished")

# print("This program will sum the integers from 1" + " to a use specified limit.")
# limit = int(input("Please enter a limit less than 20: "))

# #calculate the sum
# sum = 0
# for i in range (limit):
#     sum += 1

# #display result
# print(f"The sum of the integers from 1 to {limit} is {sum}")


sum = 0
for i in range(2, 101):
    if (i % 2 == 0):
        sum += i
print(sum)

sum = 0
for i in range(11, 32, 2):
    sum += i
print(sum)

for i in range(100,0,-1):
    if (i % 10 == 0):
        print(i, end=" ")
print()
#Nested loops

for i in range(3):
    for j in range(4):
        print(i + j, end=" ")
    print()

# numPeople = int(input("HOw many participants: "))
# numScores = int(input("How many scores each: "))

# totalAvg = 0
# for person in range(numPeople):
#     name = input("Name: ")
#     total = 0
#     for s in range(numScores):
#         score = float(input(f"Score {s+1}: "))
#         total += score
#     print(f'\tAverage: {total/numScores:.1f}')
#     print()
#     totalAvg += (total / numScores)
# print(f"Overall Average: {totalAvg/numPeople:.1f}")

Str = input("Enter a single word: ")

for currLen in range(1, len(Str) + 1):
    for startPosition in range(len(Str) - currLen + 1):
        for ndx in range(startPosition, startPosition + currLen):
            print(Str[ndx], end=" ")
        print()

numExams = int(input('Exams per student'))
moreGrades = 'Y'
while moreGrades == 'Y':
    print("Enter the exam grads. ")
    total = 0
    for i in range(1, numExams + 1):
        score = int(input(f"Exam {i}: "))
        total += score
        average = score/total
    print(f'The average is {average:.2f}')
    moreGrades = input("Countinue (Y/N").upper()
