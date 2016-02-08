"""
This class implements the __del__ method to decrement the
account counter when an account is deleted
"""

class BankAccount(object):  # Top tier class (super class)
    acct_cntr = 0         # class variable
    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable
        BankAccount.acct_cntr += 1 # Accessing a class variable
    def withdraw(self, amount):  # a method
        self.balance -= amount
    def deposit(self, amount):     # another method
        self.balance += amount
    def __str__(self):
        return 'The balance for this account is ${:,.2f}'.format(
            self.balance)
    def __del__(self):
        BankAccount.acct_cntr -= 1

a = BankAccount()  # Create a Bankaccount instance, print class variable 
print 'Number of accounts -', BankAccount.acct_cntr  
b = BankAccount()  # Create another instance and print class variable
print 'Number of accounts -', BankAccount.acct_cntr  
del a    # delete an instance and print class variable again
print 'Number of accounts -', BankAccount.acct_cntr



