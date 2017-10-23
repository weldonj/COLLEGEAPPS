#!usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and not s[i].isupper():
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and s[j].isupper():
      j = j + 1
   print s[i:j] + ' ' + str(i)

