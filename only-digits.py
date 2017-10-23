#!usr/bin/env python

import sys

s = str(sys.argv[1])
output = ''

i = 0
while i < len(s):
   curr = s[i]
   if curr.isdigit():
      output = output + str(s[i])
   i = i + 1

print output
