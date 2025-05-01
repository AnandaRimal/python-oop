# Polymorphism: The ability to define methods that can be used on different types of objects.
# Abstract Base Class (ABC): A class that cannot be instantiated and requires subclasses to implement its abstract methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, must be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # Formula for area of circle

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth  # Formula for area of rectangle

# Function that takes any shape and prints its area (polymorphism)
def calculate_area(shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(10, 5)

calculate_area(circle)  # Output: Area of circle
calculate_area(rectangle)  # Output: Area of rectangle
