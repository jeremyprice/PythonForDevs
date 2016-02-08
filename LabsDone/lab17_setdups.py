
"""
This code tests two sets of unique numbers for two or more duplicates.
It does this by testing the length of the intersection of the two sets.
If the intersection contains two or more items, there were that many
duplicates
"""

from random import sample
def has_duplicates(set1, set2):
        if len(set1.intersection(set2)) >= 2:
            return True
        else:
            return False

sets_lst = []
nums = range(1, 51)  # Produces a list with 50 integers from 1 to 50
control_set = set(sample(nums, 6))
for i in range(100):
    sets_lst.append(set(sample(nums, 6))) # creates a list containing 100 sets
two_dups = 0
for each_set in sets_lst:
    if has_duplicates(control_set, each_set):
        two_dups += 1
print 'At least two matches occurred %d times' % (two_dups)
                    
