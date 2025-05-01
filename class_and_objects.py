# Class: A blueprint for creating objects.
# Object: An instance of a class with attributes and methods defined in the class.

class Parent:
    def __init__(self, name):
        # Instance variable
        self.name = name

    def greet(self):
        # Method of the class
        return f"Hello, I am {self.name}"

# Child class inherits Parent class (Inheritance)
class Child(Parent):
    def __init__(self, name, age):
        # Using super() to call Parent class's constructor
        super().__init__(name)
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

# Creating instance (object) of Child class
child = Child("Adarsha", 22)
print(child.greet())  # Calling method from Parent class (Inheritance)
print(child.introduce())  # Calling method from Child class
