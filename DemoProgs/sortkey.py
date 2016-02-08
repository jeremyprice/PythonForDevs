"""

This program deals with various ways to sort one- and two-dimensional
lists.  With key= you should think of the function as receiving one
element of the list at a time.  In the case of the two-dimensional list,
each element is, itself, a list.  The data being transformed must follow
all of the pertinent rules.  For example, if you add a string to lst1,
using key=abs will fail on a TypeError.  In all cases, the original data
elements remain unchanged.

"""
lst1 = [12, -1, 18, -6, -14, 8]
lst2 = ['Smith', 'sally', 'sadie', 'Sam']
lst3 = [['sally', -12, 'F'], ['Sam', -10, 'm'], ['sadie', 10, 'f']]

z = sorted(lst1, key=abs) # sorts by the absolute value of each element
print z

z = sorted(lst2, key=str.lower) # sorts by the lower-case version of
print z                         # each element

z = sorted(lst3, key=lambda y: abs(y[1])) # sorts by the absolute value
print z                     # of the second element in each substring

# This lambda creates a tuple (a list would work too) containing the
# absolute value of the second element and then the lower-case version
# of the first element in each substring.
z = sorted(lst3, key=lambda y: (abs(y[1]), y[0].lower()))
print z
