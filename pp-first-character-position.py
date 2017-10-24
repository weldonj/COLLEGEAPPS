#!usr/bin/env python

import sys

c = sys.argv[1]
s = raw_input()

i = 0
while i < len(s):
   if s[i] == str(c):
      print i
      i = len(s)
   i = i + 1
      
