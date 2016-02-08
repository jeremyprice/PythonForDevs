"""
This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade and prints the results.
Then it requests another input from the keyboard.
"""

while True:
    temp = raw_input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':  # The variable name must be repeated.
        break
    ftemp = float(temp)
    ctemp = 5.0/9.0*(ftemp-32)
    print '{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
        ftemp, ctemp)

print 'Conversions ended'
