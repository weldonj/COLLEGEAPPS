#!usr/bin/env python

import sys

start = str(sys.argv[1])
dur = str(sys.argv[2])

if start[1] == ':':
   start_hour = int(start[0])
   start_min = int(start[2:4])
else:
   start_hour = int(start[0:2])
   start_min = int(start[3:5])

if dur[1] == ':':
   dur_hour = int(dur[0])
   dur_min = int(dur[2:4])
else:
   dur_hour = int(dur[0:2])
   dur_min = int(dur[3:5])

start_minutes = start_hour * 60 + start_min
dur_minutes = dur_hour * 60 + dur_min
end_minutes = start_minutes + dur_minutes

if end_minutes % 60 == 0:
   print str(end_minutes / 60 % 24)  + ':' + '00'
elif 10 <= end_minutes % 60:
   print str(end_minutes / 60 % 24)  + ':' + str(end_minutes % 60)
else:
   print str(end_minutes / 60 % 24)  + ':' + '0' + str(end_minutes % 60)
