"""

Sample program to be used with 2to3 conversion.

"""

dct = {x: ord(x) - 65 for x in 'ABCDEFG'}
print('Dictionary ', end=' ') # end= replaces the trailing comma.
print(dct)
lst = list(dct.items()) # items now creates an iterator like iteritems
print('List', lst)
lst2 = sorted(lst)  # sorted still creates a list - no chnage
lst3 = list(range(1, 11))  # range replaces xrange - creates an iterator
print(lst2, '\n', lst3) # No change here - default separator is a space

