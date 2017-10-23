i = 0
prev = input()

while i < 5:

   curr = input()

   if curr == prev:
      print 'equal'

   elif curr > prev:
      print 'higher'

   else:
      print 'lower'

   prev = curr
   
   i = i + 1








