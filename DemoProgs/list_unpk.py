"""
This program demonstrates how the ability to unpack a list
can be very useful in keeping your code clean and eliminating
the use of some list indices.
"""


my_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for a, b, c in my_lst:
    print a, b, c
