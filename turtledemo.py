#An example of a class
class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    type = "Shape type not assigned yet"
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * self.width + 2 * self.length
    def describe(self, text):
        self.type = text
    def scaleSize(self, scale):
        self.width = self.width * scale
        self.length = self.length * scale
class Square(Shape):
 def __init__(self,x):
        self.x = x
        self.y = x
        #Create a Square Class   
square = Square(100)
 
#Finding the area of your square
print(square.area())
 
#Finding the perimeter of your square
print(square.perimeter())
 
#Describing the rectangle
square.describe("A square shape")
print("Shape Type: " + square.type)
 
#Making the square 50% smaller
square.scaleSize(0.5)
 
#Print the new area of the square
print(square.area())


