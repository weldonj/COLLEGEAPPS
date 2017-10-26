#!usr/bin/env python

import sys

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = raw_input()

while n != 'end':
   
   i = 0
   while int(n) != int(a[i]):
      i = i + 1
   
   b[i] = b[i] + 1
   n = raw_input()
   
j = 0
while j < len(a):
   print a[j], b[j] * '*'
   j = j + 1
