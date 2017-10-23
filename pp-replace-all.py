#!usr/bin/env python

import sys

pattern = sys.argv[1]
replacement = sys.argv[2]

s = raw_input()

while s != 'END':
   i = 0
   while i < len(s): 
      if s[i:i + len(pattern)] == pattern:
         s = s[0:i] + replacement + s[i + len(pattern):]
         i = i + len(replacement) - 1
      i = i + 1

   print s
   s = raw_input()

      
