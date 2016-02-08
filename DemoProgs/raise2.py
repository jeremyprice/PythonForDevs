"""
Create your own exception subclass inheriting from Exception.
You can add data that will be passed to the exception handler.
"""

class DepositError(Exception):
    pass

def deposit1(amt):    
    if amt < 1000:
        ex = DepositError('Deposit too small')
        ex.dep = amt
        ex.req = 1000
        raise ex
    else:
        print 'Deposit OK'
    return

try:
    deposit1(100)
except DepositError, ex:
    print ex, '-', ex.dep, '  Need at least', ex.req

