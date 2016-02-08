"""
This program reads the file containing the temperature and precipitation
data for San Antonio for 2012 and calculates the number of days that had
precipitation as well as the amount of rain that occurred for the year.
"""

fin = open('/home/student/pydata/tmpprecip2012.dat') # Linux
# fin = open('c:/pydata/tmpprecip2012.dat') # Windows
raincount = 0
raintotal = 0
for line in fin:
    try:
        rain = float(line[8:13])
    except ValueError:
        print '{!r} - Bad Data'.format(line)
        continue
    if rain > 0:
        raincount += 1
        raintotal += rain
print 'Rain days -', raincount
print 'Rain amount -', raintotal, 'inches'


    
