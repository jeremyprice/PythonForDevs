"""
Dictionary comprehension example using scrabble letter scores from
Wikipedia as input in tuples (score, letters).  Example borrowed from
NMT site.
"""

scrbscores = [ (1, "EAOINRTLSU"), (2, "DG"), (3, "BCMP"),
           (4, "FHVWY"), (5, "K"), (8, "JX"), (10, "QZ")]
scrabbleMap = { letter: score
                 for score, letterList in scrbscores
                 for letter in letterList }
for letter in scrabbleMap:
    print letter, scrabbleMap[letter]
    
