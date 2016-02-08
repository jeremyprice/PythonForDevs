"""
This program demonstrates the use of the __future__ module
Only divsion and print function are used.  Refer to Python
documentation for the others.
"""

from __future__ import division, print_function
print(7/3)  # print is now a function, not a statement
print('Why wait for version 3?', end = ' ') # The default end is \n
print('Really!')
for i in range(4):  # The default sep is a space
    print(i, i**2, sep = ' :-) ', end = ' --- ')





