"""
This program accumulates by month the maximum high temperature, the
minimum high temperature, the number of days and the accumulated high
temperatures. The latter two are used to calculate the average high
temperature for the month.
"""

monlst = []
for i in range(12):
    monlst.append([0, 0, 0, 200]) # sublist[Days, Accum Temp, Max Hi, Min Hi]

fin = open('/home/student/pydata/tmpprecip2012.dat', 'r')
# fin = open('c:/pydata/tmpprecip2012.dat', 'r')
for linein in fin:
    try:
        mon = int(linein[0:2])
        temp = int(linein[13:16])
    except ValueError:
        print 'Bad Data', linein
        continue
    x = mon - 1
    monlst[x][0] += 1  # add 1 to the day count
    monlst[x][1] += temp  # accumulate the temperature
    if temp > monlst[x][2]:
        monlst[x][2] = temp  # update the max hi temp
    if temp < monlst[x][3]:
        monlst[x][3] = temp  # update the min hi temp

mon = 0
for cntr, totmp, maxtmp, mintmp in monlst:
    mon += 1
    print '{:2d} {:6.1f} {:3d} {:3d}'.format(
        mon, totmp/float(cntr), maxtmp, mintmp)
                   
                  
