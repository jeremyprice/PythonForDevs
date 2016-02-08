"""
This program includes a subclass (MinBalAcct) that inherits from
BankAccount and then overrides __init__, __str__ and withdraw.
It prevents accounts being set up that don't meet the minimum
balance requirements.
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

class MinBalAcct(BankAccount):
    def __init__(self, deposit, minbal):
        if deposit < minbal:
            raise ValueError, 'Deposit too small'
        self.minimum_bal = minbal
        self.balance = deposit
        BankAccount.acct_cntr += 1
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_bal:
            print 'Withdrawal request of {:,.2f}'.format(amount)
            print '   denied due to minimum balance requirement'
        else:
            self.balance -= amount
    def __str__(self):
        return ("The balance for this account is ${:,.2f}\n" +
               "The minimum balance is ${:,.0f}").format(self.balance,
                                                        self.minimum_bal)    
        
a = BankAccount()  # Create an instance of Bankaccount
b = BankAccount()  # Create another instance
print 'Number of accounts -', BankAccount.acct_cntr  # print class variable
del a
print 'Number of accounts -', BankAccount.acct_cntr
c = MinBalAcct(5000,1000)  # Create a minimum balance instance
print 'Number of accounts -', BankAccount.acct_cntr
print c
c.withdraw(4500)
try:
    d = MinBalAcct(500,1000)
except ValueError, msg:
    print "Account not established -", msg
print c
print d  # Verifies the instantiation did not occur.
    




