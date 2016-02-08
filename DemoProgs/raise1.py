"""
Two ways to raise a standard exception
"""
def deposit1(amt):
    if amt < 1000:
        raise ValueError, 'Deposit too small'
    else:
        print 'Deposit OK'
    return

def deposit2(amt):
    if amt < 1000:
        raise ValueError('Deposit too small')
    else:
        print 'Deposit OK'
    return

try:
    deposit1(100)
except ValueError, msg:
    print msg

try:
    deposit2(100)
except ValueError, msg:
    print msg
