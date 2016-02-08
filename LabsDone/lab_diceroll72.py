"""
This program simulates the rolling of a pair of dice a predetermined
number of times.  It counts the number of 2's and the number of 7's
rolled.  Then it calculates the percetage of rolls that were 7's or 2's
respectively.  It prints the results formatted to one decimal place.
"""

from random import randrange
twos = 0
sevens = 0
counter = 10000
for i in range(counter):
    roll = randrange(1, 7) + randrange(1, 7)
    if roll == 2:
        twos += 1
    if roll == 7:
        sevens += 1

per2 = 100.0 * twos / counter
per7 = 100.0 * sevens / counter
print 'Total rolls -', counter
print '%.1f percent of the rolls were sevens' % (per7)
print '%.1f percent of the rolls were twos' % (per2)
    
