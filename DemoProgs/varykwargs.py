"""

This program demonstrates how unidentified keyword
arguments are handled/passed as a dictionary.  The receiving
identifier is preceded by two asterisks.

"""

def gets(**kwargs):
    print type(kwargs), len(kwargs), '\n', kwargs
    for i in kwargs:
        print i, kwargs[i], type(kwargs[i])
    
x = 12.34
y = 'string'
gets(a=1234, b=x+1, c=y+'s', d=12.34)


