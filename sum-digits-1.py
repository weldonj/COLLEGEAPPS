#!usr/bin/env python

import sys

s = str(sys.argv[1])
total = 0

i = 0
while i < len(s):
   total = total + int(s[i])
   i = i + 1

print total


