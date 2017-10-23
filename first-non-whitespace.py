#!usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and s[i].isspace():
   i = i + 1

if i < len(s):
   print str(i)
else:
   print '-1'

