"""
This class implements the __str__ method to format the account balance
"""

class BankAccount(object):  # Top tier class (super class)

    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable
    def withdraw(self, amount):  # a method
        self.balance -= amount
    def deposit(self, amount):     # another method
        self.balance += amount
    def __str__(self):
        print '__str__ method entered'
        return 'The balance for this account is ${:,.2f}'.format(
            self.balance)
    
a = BankAccount()  # Create an instance of Bankaccount
b = BankAccount()  # Create another instance
a.deposit(2500)
print a




