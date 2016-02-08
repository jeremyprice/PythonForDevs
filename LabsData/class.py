""" Initial class exercise """

class BankAccount(object):  # Top tier class (super class)
    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable 
    def withdraw(self, amount):  # a method
        self.balance -= amount
        return self.balance
    def deposit(self, amount):     # another method
        self.balance += amount
        return self.balance

a = BankAccount()  # Create an instance of Bankaccount
b = BankAccount()  # Create another instance
a.deposit(100)    # Deposit $100 into account represented by variable a
