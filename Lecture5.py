# Logical Boolean Operators

s1 = 5
s2 = 3
s3 = -1
x = s1 < s2 and s2 < s3
print(x)

#The morgan's law!

not (s1 and s2)

print("I tink sometime in tha life im tuu competetive")

LOWER = 0
UPPER = 10
# Get the number
print("Guess a number between ", end = "")
guess = int(input(f"{LOWER} and {UPPER}: "))

#check for invalid number
if (guess >= LOWER and guess <= UPPER):
    print("Invalid Number")

PASS_GRADE = 59.5
grade = 60

message = 'PASS' if (grade > PASS_GRADE) else 'FAIL'

print(message)

name = "Jack Jackson"
zipcode = "66223k"
tempInput = "-2"
print('jack' in name.lower())