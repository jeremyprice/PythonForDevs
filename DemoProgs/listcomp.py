"""
This program provides examples of filter and map.
It first provides examples of these tasks performed with ordinary
programming techniques.  
"""

# This code creates this list [2, 5, 8, 11, 14, 17]
x = range(2,20,3)
print 'Original list:', x

# This loop selects only the even numbers to be included in a new list

y = []
for i in x:
    if i % 2 == 0:
        y.append(i)
print y

# This loop creates a new list containing the square of each entry in
# list x.
y = []
for i in x:
    y.append(i**2)
print y

# The following are two list comprehensions.  They accomplish the
# filtering and mapping operations in the looping operations above.
# See Python notes for a link to a tutorial on list comprehensions.

y = [i for i in x if i % 2 == 0]  # This comprehension filters
print y

y = [i**2 for i in x]  # This comprehension maps
print y

