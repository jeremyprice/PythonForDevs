"""
This program reads temperatures in fahrenheit from
the keyboard, converts them to centigrade (in a lambda function)
and prints the result.
"""

nutmp = lambda tmp : 5.0 /9.0 * (tmp - 32)
while True:
    temp = raw_input('Enter a temperature: ')
    if temp in 'qQ':  
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print 'Input contains non-numeric data - try again'
        continue
    ctemp = nutmp(ftemp)
    print '{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp)


