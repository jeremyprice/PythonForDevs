# -*- coding: latin-1 -*-

"""

This program reads a file conataining Latin-1 encoded data and prints
it along with its hex representation.  Notice the latin charaters use
the 8th bit.  Processing this data does not require an encoding
declaration in Windows.

"""
import binascii, sys
# fin = open('c:/pydata/latin.txt', 'r')
fin = open('/home/student/pydata/latin.txt', 'r')
for line in fin:
    for char in line:
        print char.decode(encoding='latin-1'),
    print '{0}'.format(binascii.b2a_hex(line))
x = 'Comércio Mineiro'
print x.decode(encoding='latin-1')
x = 'Com\xe9rcio Mineiro'
print x.decode(encoding='latin-1')
x = 'The temperature is 95\xb0'
print x.decode(encoding='latin-1')
