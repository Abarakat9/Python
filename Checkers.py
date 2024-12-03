red_even = 'aceg'
red_odd = 'bdfh'
validData = False
UPPER_ROW = 8
LOWER_ROW = 1

row = input("Row (1-8): ")
if (row.isdigit()):
    row = int(row)
    if (LOWER_ROW < row < UPPER_ROW):
        validData = True
    else:
        print("Invalid Entry")


if (validData):
    column = input("Column (a-h): ")
    if (column in red_even or column in red_odd):

        if (column in red_even):
            if (row % 2 == 0):
                color = 'red'
            else:
                color = 'black'
        else:
            if (row % 2 == 0):
                color = 'black'
            else:
                color = 'red'
        print(color)