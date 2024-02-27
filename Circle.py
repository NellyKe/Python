import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = 4
my_circle = Circle(radius)

print("Area of the circle:", my_circle.area())
print("Perimeter of the circle:", my_circle.perimeter())
