# Multiple Inheritance: A class can inherit from more than one base class.
# MRO (Method Resolution Order): Determines the order in which methods are looked up in the inheritance hierarchy.

class Horse:
    def run(self):
        print("I can run")

class Donkey:
    def carry_load(self):
        print("I can carry load")

# Mule class inherits from both Horse and Donkey
class Mule(Horse, Donkey):
    def eat(self):
        print("I can eat")

# Creating instance of Mule class
mule = Mule()
mule.eat()  # Calling method from Mule class
mule.run()  # Calling method from Horse class
mule.carry_load()  # Calling method from Donkey class

# Check MRO (Method Resolution Order)
print(Mule.mro())  # MRO shows the method resolution order: Mule -> Horse -> Donkey -> Object
