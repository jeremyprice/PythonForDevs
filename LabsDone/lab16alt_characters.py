"""

This program evaluates all of the characters in the book,
"Alice in Wonderland."  It ignores all of the punctuation characters and
changes all alphabetic characters to lower case.  Then, it uses a 
dictionary to count character occurrences.  It then creates a list of tuples
from the dictionary and sorts the results by
the number of occurrences in descending order.  

"""
from string import whitespace
from operator import itemgetter

alice_chars = {}  # create an empty dictionary
#fin = open('/home/student/pydata/alice_in_wonderland.dat')
fin = open('c:/pydata/alice_in_wonderland.dat', 'r')
bookin = fin.read()
bookin = bookin.lower()

for each_char in bookin:
    if each_char in whitespace:
        continue
    if each_char not in alice_chars:
        alice_chars[each_char] = 1
    else:
        alice_chars[each_char] += 1
templist1 = zip(alice_chars.values(), alice_chars.keys())
templist1.sort(reverse=True)

for a, b in templist1:
        print '{0:2s}{1:5d}'.format(b, a)
print "We're done!"
fin.close()


