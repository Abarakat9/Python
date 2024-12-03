class Person:
    def __init__(self, inName='', inAge = 0):
        self.setName(inName)
        self.setAge(inAge)

    def setName(self, inName):
        self.name = inName

    def getName(self):
        return self.name
    
    def setAge(self, inAge):
        if (inAge < 0):
            inAge = 0
        self.age = inAge
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return f"{self.getName()}, {self.getAge()}"