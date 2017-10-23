#!usr/bin/env python

import sys

score = int(sys.argv[1])

i = 0
while i * 3 <= score:
   print str(i) + ' ' + str(score - (i * 3))
   i = i + 1 
