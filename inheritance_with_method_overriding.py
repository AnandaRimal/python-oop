# Inheritance: A class can inherit properties and methods from another class.
# Method Overriding: A subclass can provide a specific implementation of a method defined in its superclass.

class Animal:
    # Abstract method that should be implemented by subclasses
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism using method overriding
def animal_sound(animal):
    print(animal.speak())

# Creating instances of Dog and Cat classes
dog = Dog()
cat = Cat()

# Calling the same method but different behavior (polymorphism)
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
