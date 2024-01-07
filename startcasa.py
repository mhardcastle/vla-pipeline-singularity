# Find the measurement set in the working directory and create a CASA pipescript that refers to it

import glob
import sys

ms=glob.glob('*.ms')[0]

lines=open('/usr/local/src/casa_pipescript.py')
with open('casa_pipescript.py','w') as outfile:
    for l in lines:
        outfile.write(l.replace('mySDM',ms))

