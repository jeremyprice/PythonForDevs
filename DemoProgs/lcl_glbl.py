"""
This program shows what variables are known locally in the main program
as well as the function.  It also demonstrates why you need to be
careful when modifying a global, immutable variable from a function.
"""

def lcl_tst(a, b):
    z = a + b
    print dir(), '\n'
    x = 'changed'
    print 'x =', x, '\n'
    return

x = 'string1'
y = 'string2'
lngint = 1234567890123456789
print 'Globals -', dir(), '\n'
lcl_tst(x, y)
print 'x =', x
    
