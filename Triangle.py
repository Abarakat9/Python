# @author Ahmad Barakat

# This class is a triangle with a base and height
# Includes methods to set and get dimensions, calc area,
# and return string representation of the triangle.
class Triangle:

    def __init__(self, base=1, height=1):
        self.setBase(base)
        self.setHeight(height)
    
    def setBase(self, base):
        if base <= 0:
            raise ValueError(f"Illegal argument for triangle base: {base}")
        self.base = base
    
    def getBase(self):
        return self.base

    def setHeight(self, height):
        if height <= 0:
            raise ValueError(f"Illegal argument for triangle height: {height}")
        self.height = height
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return (self.base * self.height) / 2
    
    def __str__(self):
        return f"Base: {self.base}, Height: {self.height}"
    