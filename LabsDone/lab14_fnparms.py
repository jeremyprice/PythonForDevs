"""
This program takes a variable number of fahrenheit temperatures from
the main program, tests them for validity and converts them to centigrade.  
"""

def f_to_c(*args):
    print type(args), args
 
    for temp in args:
        if isinstance(temp, int)or isinstance(temp, float): 
            cent_temp = 5.0 / 9.0 * (temp -32)
            print '{:6.1f} {:5.1f}'.format(temp, cent_temp)
        else:
            print temp, 'This data is not vaild'

f_to_c(111, -2, 73.5, 24, '2e', 88.2)

