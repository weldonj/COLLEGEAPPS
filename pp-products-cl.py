#!usr/bin/env python

import sys
prev = 1
curr = 0
digits = sys.argv[1]

i = 0 
while i < len(digits):
   curr = int(digits[i]) * prev
   prev = curr
   print curr
   i = i + 1




