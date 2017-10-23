#!usr/bin/env python

import sys

output_string = ''

i = 1
while i < len(sys.argv):
   if len(output_string) < len(sys.argv[i]):
      output_string = sys.argv[i]
   i = i + 1

print output_string


