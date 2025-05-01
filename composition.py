# Composition: A "has-a" relationship where a class contains objects of other classes.

class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels are rotating")

class Car:
    # Composition: Car "has-a" engine and wheels
    def __init__(self):
        self.engine = Engine()  # Car has an engine
        self.wheels = Wheels()  # Car has wheels

    def drive(self):
        self.engine.start()
        self.wheels.rotate()

# Creating instance of Car
car = Car()
car.drive()  # Starting the car (using composition)

# Exercise: Computer class using composition
class Processor:
    def __init__(self, speed):
        self.speed = speed

    def process(self):
        print(f"Processing at {self.speed}")

class Memory:
    def __init__(self, size):
        self.size = size

    def load(self):
        print(f"Loading data into {self.size} memory")

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

    def read(self):
        print(f"Reading data from {self.capacity} storage")

class Computer:
    def __init__(self):
        self.processor = Processor("4.1 GHz")  # Composition: Computer "has-a" processor
        self.memory = Memory("16 GB")  # Composition: Computer "has-a" memory
        self.storage = Storage("1 TB")  # Composition: Computer "has-a" storage

    def processing(self):
        self.processor.process()

    def loading_data(self):
        self.memory.load()

    def reading_from_storage(self):
        self.storage.read()

# Creating instance of Computer class
computer = Computer()
computer.processing()  # Processing using computer's processor
computer.loading_data()  # Loading data using memory
computer.reading_from_storage()  # Reading from storage
