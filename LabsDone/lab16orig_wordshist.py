"""

This program evaluates all of the words in the book,
"Alice in Wonderland."  It removes all of the punctuation characters and
changes all alphabetic characters to lower case.  Then, it uses a 
dictionary to count word occurrences.  It then creates a list of tuples
from the dictionary and sorts the results by
the number of occurrences in descending order.  

"""
from string import punctuation
from operator import itemgetter

alice_words = {}  # create an empty dictionary
fin = open('/home/student/pydata/alice_in_wonderland.dat')
# fin = open('c:/pydata/alice_in_wonderland.dat', 'r')
bookin = fin.read()
for i in punctuation:
    if i == '-':  # hyphens - special case; replace with a space
        bookin = bookin.replace(i, ' ')
    else:
        bookin = bookin.replace(i, '') # all other puctation - remove
bookin = bookin.lower()
wordlist = bookin.split()
for word in wordlist:
    if word not in alice_words:
        alice_words[word] = 1
    else:
        alice_words[word] += 1
templist1 = alice_words.items()
templist1.sort(key=itemgetter(1), reverse=True)

counter = 0
firstime = True
for a, b in templist1:
    if firstime:
        biggest = b
        firstime = False
    c = '*' * (int(float(b)/biggest * 20))
    # Note - int uses floor rather than round. A more accurate version:
    # c = '*' * (int(round(float(b)/biggest * 20)))
    # The result is only slightly different.  Try it and compare results.
    print '{:7s}{:4d}  {:s}'.format(a, b, c)
    counter += 1
    if counter > 20:
        break
print "We're done!"
fin.close()


