"""
This program simulates rolling a pair of dice 100,000 times and
calculates the percentage of the time each possible roll occurs.
These results are then compared (visually) to the mathematically
derived results.
"""

from random import randrange

roll_lst = 13 * [0]
rolls = 100000
for i in range(rolls):
    j = randrange(1, 7) + randrange(1, 7)
    roll_lst[j] += 1
roll = 2
for i in roll_lst[2:]:
    tmp = float(i) / rolls
    print '{:2d} {:6.2%}'.format(roll, tmp)
    roll += 1
    
