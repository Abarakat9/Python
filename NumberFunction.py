class NumberFunction:
    def __init__(self, inNumbers):
        self.numbers = inNumbers

    def filterEvens(self):
        self.numbers = [num for num in self.numbers if num % 2 == 0]
        return self
    
    def square(self):
        self.numbers = [num ** 2 for num in self.numbers]
        return self
    
    def sumNumbers(self):
        return sum(self.numbers)
    
listOfNums = [val for val in range(1, 21)]

result = (NumberFunction(listOfNums).filterEvens().square().
          sumNumbers())
print(result)