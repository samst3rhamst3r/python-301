# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(3)
r = Rectangle(2, 5)

print(f"Area and circumference of Circle is {c.area()} and {c.circumference()}.")
print(f"Area and perimeter of Rectangle is {r.area()} and {r.perimeter()}.")