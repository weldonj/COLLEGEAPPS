#!usr/bin/env python

import sys

pattern = sys.argv[1]
replacement = sys.argv[2]

original = raw_input()

while original != 'end':
   i = 0
   while i < len(original) and original[i:i + len(pattern)] != pattern:
      i = i + 1
   if i < len(original):
      print original[0:i] + replacement + original[i+len(pattern):len(original)] 
   else:
      print original
   original = raw_input()
      
