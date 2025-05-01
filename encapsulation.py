# Encapsulation: Bundling data and methods that operate on the data within one unit (class).
# Private attributes: Declared with __ (double underscore), not accessible directly from outside the class.

class BankAccount:
    def __init__(self, name):
        # Private attributes (name mangling will make them inaccessible from outside)
        self.__name = name
        self.__balance = 1000  # Default balance

    # Getter method to access the private attribute
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be greater than 0")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

# Creating instance
account = BankAccount("Adarsha")
print(account.get_balance())  # Accessing balance via method (getter)

account.deposit(5000)  # Deposit money
print(account.get_balance())  # Updated balance

account.withdraw(300)  # Withdraw money
print(account.get_balance())  # Updated balance

# Cannot directly access private attributes (name mangling)
# print(account.__balance)  # Uncommenting this will raise an error

# Accessing via name mangling (for demonstration purposes, not recommended in practice)
print(account._BankAccount__balance)
