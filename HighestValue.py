# @author Ahmad Barakat

from random import randint
def main():

    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    low = int(input("Lowest potential value: "))
    high = int(input("Highest potential value: "))

    matrix = []
    addDimensions(matrix, rows, cols)

    matrix = getTable(rows, cols)

    fillMatrix(matrix, low, high)
    displayMatrix(matrix)

    highestVal, highestLocation = findHighest(matrix)
    print(f"The highest value is {highestVal} and is located at {highestLocation}")

    # addDimensions creates storage for a rows x cols matrix initialized to 0's
    # @param matrix The location of the matrix
    # @param rows The number of rows
    # @param cols The number of columns
def addDimensions(matrix, rows, cols):
    for row in range(rows):
        nextRow = [0] * cols
        matrix.append(nextRow)

    # getTable creates a rows x cols table initialized to 0's
    # @param rows The number of rows
    # @param cols The number of columns
    # @return the rectangular table
def getTable(rows, cols):
    table = []
    for row in range(rows):
        nextRow = [0] * cols
        table.append(nextRow)
    return table

    # displayMatrix displays a matrix in table format with a cell width of 4
    # @param matrix The matrix to display
def displayMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]:4d}", end = "")
        print()
print()
    # fillMatrix fills a matrix with random integers in the range -10 through 10
    # @param matrix The matrix to fill
    # @param low The lowest random number
    # @param high The highest random number
def fillMatrix(matrix, low, high):

    for rowList in matrix:
        for col in range(len(rowList)):
            rowList[col] = randint(low, high)

#findHighest finds the location of the highest value
# in the matrix
# @param matrix The matrix to search
# @return tuple containing row and column findex of highest value

def findHighest(matrix):
    highestVal = matrix[0][0]
    highRowIndex = 0
    highColIndex = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > highestVal:
                highestVal = matrix[row][col]
                highRowIndex = row
                highColIndex = col
            
    return highestVal, (f"[{highRowIndex}][{highColIndex}]")


main()
