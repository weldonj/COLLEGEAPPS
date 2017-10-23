#!usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and not s[i].isdigit():
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and s[j].isdigit():
      j = j + 1
   if j < len(s):
      k = j
      while k < len(s) and not s[k].isdigit():
         k = k + 1
      if k < len(s):
         l = k
         while l < len(s) and s[l].isdigit():
            l = l + 1
         if l <= len(s):
            print s[k:l] + ' ' + str(k)
