"""

Sample program to be used with 2to3 conversion.

"""

dct = {x: ord(x) - 65 for x in 'ABCDEFG'}
print 'Dictionary ',
print dct
lst = dct.items()
print 'List', lst
lst2 = sorted(lst)
lst3 = range(1, 11)
print lst2, '\n', lst3

