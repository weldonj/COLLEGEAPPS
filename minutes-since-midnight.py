#!usr/bin/env python

import sys
hours = 0
minutes = 0
mins_to_mid = 0

s = str(sys.argv[1])

if s[1] == ':':
   hours = int(s[0])
   minutes = int(s[2:len(s)])
else:
   hours = int(s[0:2])
   minutes = int(s[3:len(s)])

mins_to_mid = (hours * 60) + minutes

print mins_to_mid
