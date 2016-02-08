"""

This program creates a list and set comprehensions containing tuples and
a dictionary comprehension.  Both contain the given-fahrenheit and
calculated-centigrade temperatures.

"""

x = range(-40, 120, 10)
print x


print 'List Comprehension'  # This comprehension maps and filters
lcomp = [(i, 5.0/9.0*(i-32)) for i in x if i != 0 and i != 50]
for ftemp, ctemp in lcomp:
    print '{0:3d} = {1:.2f}'.format(ftemp,ctemp)

print '\nDictionary comprehension'
dcomp = {i: 5.0/9.0*(i-32) for i in x if i != 0 and i != 50}
for item in dcomp:
    print '{0:3d} = {1:.2f}'.format(item,dcomp[item])

print '\nSet Comprehension'
scomp = {(i, 5.0/9.0*(i-32)) for i in x if i != 0 and i != 50}
for ftemp, ctemp in scomp:
    print '{0:3d} = {1:.2f}'.format(ftemp,ctemp)

"""
This code compares a list comprehension versus loops to create a
two-dimensional list containing the traditional multiplication
table.  The comprehension replaces six statements.  The downside
is that it is not that clear to read even for this simple example.
"""
raw_input('Press enter to continue')
print '\nNested Comprehension'
rng = range(1, 10)
mtable = [[num1 * num2 for num1 in rng] for num2 in rng]
for entry in mtable:
    print entry

mtable2 = []
for num1 in rng:
    tmplst = []
    for num2 in rng:
        tmplst.append(num1 * num2)
    mtable2.append(tmplst)
for entry in mtable2:
    print entry
