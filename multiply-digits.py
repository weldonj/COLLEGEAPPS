#!usr/bin/env python

import sys

s = str(sys.argv[1])
product = 1

i = 0
while i < len(s):
   curr = s[i]
   if curr.isdigit():
      product = product * int(curr)
   i = i + 1

print product
