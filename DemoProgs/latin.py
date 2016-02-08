"""

This program reads a file conataining Latin-1 encoded data and prints
it along with its hex representation.  Notice the latin charaters use
the 8th bit.  Processing this data does not require an encoding
declaration in WIndows.

"""
import binascii
# fin = open('c:/pydata/latin.txt', 'r')
fin = open('/home/student/pydata/latin.txt', 'r')
for line in fin:
    for char in line:
        print char,
    print '{0}'.format(binascii.b2a_hex(line))
x = 'Comércio Mineiro'
print x
x = 'Com\xe9rcio Mineiro'
print x
