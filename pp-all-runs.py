#!usr/bin/env python

import sys

s = sys.argv[1]

i = 1
count = 0

while i < len(s):
   if s[i] == s[i-1]:
      j = i
      while s[j] == s[j-1]:
         count = count + 1
      j = j + 1
   print s[j] + ' ' + str(count)
   count = 0
   i = i + 1
   
