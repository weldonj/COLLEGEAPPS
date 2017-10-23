#!usr/bin/env python

import sys
output = int(sys.argv[1])

i = 1
while i < len(sys.argv):
   

   if int(sys.argv[i]) >= int(output):
      output = sys.argv[i]

   
   i = i + 1

print output


