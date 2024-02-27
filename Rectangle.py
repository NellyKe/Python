class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
length = 5
width = 3
my_rectangle = Rectangle(length, width)

print("Area of the rectangle:", my_rectangle.area())
print("Perimeter of the rectangle:", my_rectangle.perimeter())
