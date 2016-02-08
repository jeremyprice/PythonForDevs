"""
This program reads a variable number of fahrenheit temperatures from
the command line and converts them to centigrade.  Note - it skips the
first parameter.

"""

from sys import argv

print type(argv), argv
firsttime = True
for str_temp in argv:
    if firsttime:   # Is this the first parameter?  If so, skip it.
        firsttime = False
        continue
    try:            # Is the data numeric? 
        f_temp = float(str_temp)
    except ValueError:
        print str_temp, 'This data is not nummeric'
    else:
        cent_temp = 5.0 / 9.0 * (f_temp - 32)
        print '{:4s} {:5.1f}'.format(str_temp, cent_temp)

