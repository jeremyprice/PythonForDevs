"""
Using itemgetter to sort on a different item in a list/tuple.
In this case, the second item will be the object of the sort.
This program uses both the sort method and the sorted function.
"""

from operator import itemgetter

my_list = [['z', '3'],['a', '2'],['g', '4']]
my_list.sort(key=itemgetter(1))
print my_list, '\n'

my_list = [['z', '3'],['a', '2'],['g', '4']]
my_list.sort(reverse=True, key=itemgetter(1))
print my_list, '\n'

my_list = [['z', '3'],['a', '2'],['g', '4']]
nu_list = sorted(my_list, key=itemgetter(1))
print nu_list, '\n'

nu_list = sorted(my_list, key=itemgetter(1), reverse = True)
print nu_list, '\n'


