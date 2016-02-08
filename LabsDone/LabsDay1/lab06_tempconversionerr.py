"""
This program reads a temperature in fahrenheit from the keyboard,
converts it to centigrade and prints the results.
It catches invalid data and keeps the program running.
"""

while True:
    temp = raw_input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print 'Input contains non-numeric data - try again'
        continue
    ctemp = 5.0 / 9.0 * (ftemp - 32)
    print '{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp)
