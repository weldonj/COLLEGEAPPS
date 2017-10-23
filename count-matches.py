#!usr/bin/env python

import sys

pattern = sys.argv[1]
s = raw_input()
total = 0

while s != 'end':
   i = 0
   while i < len(s): 
      
      if s[i:i + len(pattern)] == pattern:
         total = total + 1
         i = i + len(pattern) - 1
      i = i + 1



   print total
   total = 0
   s = raw_input()

      
