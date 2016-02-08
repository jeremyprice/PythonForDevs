"""
This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results. 
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 / 9.0 * (xtmp - 32)
    print '%.1f degrees Fahrenheit is %.1f degrees Centigrade' % (
        xtmp, nutmp)
    

temp = 72
fahrenheit_to_centigrade(temp)
    

