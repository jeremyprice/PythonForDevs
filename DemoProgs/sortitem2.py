"""
Using itemgetter to sort on two items in a list/tuple.
In this case, the second and third items will be the object
of the sort.  The program uses both the sort method and
the sorted function.
"""

from operator import itemgetter

my_list = [['john', 'B', 15],['jane', 'A', 12],['dave', 'B', 10]]
my_list.sort(key=itemgetter(1, 2))
print my_list, '\n'

my_list = [['john', 'B', 15],['jane', 'A', 12],['dave', 'B', 10]]
my_list.sort(reverse=True, key=itemgetter(1, 2))
print my_list, '\n'

my_list = [['john', 'B', 15],['jane', 'A', 12],['dave', 'B', 10]]
nu_list = sorted(my_list, key=itemgetter(1, 2))
print nu_list, '\n'

nu_list = sorted(my_list, key=itemgetter(1, 2), reverse=True)
print nu_list, '\n'
