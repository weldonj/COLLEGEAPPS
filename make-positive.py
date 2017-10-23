#!usr/bin/env python

n = raw_input()

while n != 'end':
   if n[0] == '-':
      print n[1:len(n)]
   else:
      print n
   n = raw_input()
   
   

