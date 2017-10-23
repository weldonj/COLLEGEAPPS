#!usr/bin/env python

n = raw_input()

while n != 'end':
   if n[len(n)-1] == '0' or n[len(n)-1] == '5':
      print n
   n = raw_input()
