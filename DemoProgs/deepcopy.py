"""
Deep copy versus shallow copy is very important to understand.
"""

lst1 = [1,2,[3,4], [5,6], 7]
lst2 = lst1  # Creates alias only.  No copy.
lst2[4] = 8
print lst1
print lst2, '\n'
lst2 = list(lst1)  # Creates shallow copy.  2nd level is effectively aliased.
lst2[4] = 10
print lst1
print lst2, '\n'
lst2[2][1] = 15
print lst1
print lst2, '\n'

from copy import deepcopy
lst2 = deepcopy(lst1)  # Creates a true copy.  All levels unique.
lst2[2][1] = 88
print lst1
print lst2
