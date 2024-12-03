MIN_D = 59.5

#Get Score
score = float(input("Please enter the score: "))

#Display feedback

if (score >= MIN_D):
    print('you passed!')
else:
    print('You failed!!!')

directionsNeeded = input('Directions needed? (Y or N): ').upper()

if(directionsNeeded[0] == 'Y'):
    print("South on Quivera past 119th")
    print('Turn right on hill into the KU Edwards campus')

floatNum = float(input("Enter a floating point number: "))

if (floatNum == 0):
    print("Zero")
else:
    if (floatNum < 0):
        print('Negative')
    else: 
        print('Positive')
    
floatNum = abs(floatNum)
if (floatNum < 1):
    print('small')
elif (floatNum > 1000000):
    print('large')

print('end')

