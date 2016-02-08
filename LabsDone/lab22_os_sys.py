"""
This program shows the basic usage of several features in the
sys and os modules.  You may need to change the values of the
ds and di variables to get a meaningful result.
"""

import os, sys
ds = '/home/student/pydata/words.txt'
di = '/home/student/pydata'
# ds = 'c:/pydata/words.txt'
# di = 'c:/pydata'

print sys.argv
print os.getcwd()
print os.path.exists(ds), os.path.isdir(di), os.path.isfile(ds)
print os.path.isdir(ds), os.path.isfile(di)
print os.path.basename(ds), os.path.dirname(ds)
for item in os.environ:
    print item, os.environ[item]
sys.exit()
print 'Did we get this far?'
