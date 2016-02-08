"""
This demo program has a function that takes a variable number of
parameters and shows how a collector assembles them all in a tuple.
By tradition, we use *args for positional parameters and **kwargs
for keyword parameters.
"""

def myfnc(*args):
    print len(args), type(args)
    print args

x = 1
y = 2
z = 3
myfnc(x, y, z)

"""
But, what if you have a collection (e.g., a list) that you want
to pass to a function that is expecting individual elements.  Use
the * operator to pass the elements of the list instead of the
list itself.
"""
mylst = [x, y, z]
myfnc(*mylst)
