
def frange(start, stop, step):

    i = start
    while i < stop:
        yield i
        i = i + step

for x in frange(0.5, 1.0, 0.1):
    print x


print
from decimal import Decimal
for x in frange(Decimal('0.5'), Decimal('1.0'), Decimal('0.1')):
    print x
    

