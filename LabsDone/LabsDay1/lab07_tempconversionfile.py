"""
This program reads temperatures in fahrenheit from
a file, converts them to centigrade and
creates a report file with the results.
Also, there is an example of using the !r format character.
"""

filein = open('/home/student/pydata/temps.dat')
fileout = open('/home/student/pydata/temprpt.txt', 'w')
# filein = open('c:/pydata/temps.dat')  # Windows file
# fileout = open('c:/pydata/temprpt.txt', 'w')  # Windows file
for linein in filein:
    try:
        ftemp = float(linein)
    except ValueError:
        print 'Input contains non-numeric data - {!r}'.format(linein)
        continue
    ctemp = 5.0 /9.0 * (ftemp - 32)
    outline =  \
    '{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade\n'.format(
        ftemp, ctemp)
    fileout.write(outline)
filein.close()
fileout.close()
