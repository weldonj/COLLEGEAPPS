#!usr/bin/env python

import sys

s = str(sys.argv[1])
total = 0

i = 0
while i < len(s):
   curr = s[i]
   if curr.isdigit():
      total = total + int(curr)
   i = i + 1

print total
