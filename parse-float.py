#!usr/bin/env python

import sys

f = sys.argv[1]

i = 0
while i < len(f) and f[i] != '.':
   i = i + 1

if i < len(f):
   print f[0:i]
   print f[i+1:len(f)]

