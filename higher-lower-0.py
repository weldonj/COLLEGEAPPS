prev = input()

while prev != 0:
   
   curr = input()

   if curr == prev and curr != 0:
      print 'equal'

   elif curr > prev and curr != 0:
      print 'higher'

   elif curr < prev and curr != 0:
      print 'lower'


   prev = curr
   








