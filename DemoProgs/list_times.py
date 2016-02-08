"""
This program demonstrates the difference between append and
concatenate in lists when dealing with a relatively large additions
to a list.  The times increase exponentially for concatenation as the
number of operations increases due to the entire list being moved to
a new location each time.
"""

from time import time
lst = []
stme = time()
for num in xrange(100000):
    lst.append(num)
print '%.2f seconds the better way' % (time() - stme)

lst = []
stme = time()
for num in xrange(100000):
    lst= lst + [num]
print '%.2f seconds the other way' % (time() - stme)
