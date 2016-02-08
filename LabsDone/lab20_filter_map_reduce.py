"""
This program provides examples of filter, map and reduce.
It first provides examples of these tasks performed with ordinary
programming techniques.  Next it provides examples of how to filter
and map using list comprehensions.  Then it provides examples of getting
all three results with appropriate builtin functions along with Lambda
functions.  It is not the purpose of this course to teach comprehensions
or these functions; just to make you aware of these alternatives.
Also, you are likely to encounter these implementations in various
sites such as stackoverflow.com.
"""

# This code creates this list [2, 5, 8, 11, 14, 17]
x = range(2,20,3)
print 'Original list:', x

# This loop selects only the even numbers to be included in a new list
# This is an example of filtering.
y = []
for i in x:
    if i % 2 == 0:
        y.append(i)
print y

# This loop creates a new list containing the square of each entry in
# list x.  This is an example of mapping.
y = []
for i in x:
    y.append(i**2)
print y

# This loop sums all of the entries in list x.  It is an example of
# reducing.
y = 0
for i in x:
    y += i
print y


# The following are examples of filter, map and reduce implemented
# through built-in functions and lambda functions.  
z = filter(lambda i: i % 2 == 0, x)
print z

z = map(lambda i: i**2, x)
print z

z = reduce(lambda i, j: i + j, x)
print z
z = sum(x) # Summing is done so frequently, there is a built-in 
print z    # function for it which is much simpler than any of the
           # other examples I have shown you.
