n = input()
m = input()

i = 0

while i < n:
  
   if i == 0:
      print m

   elif (m % 2) != 0 and i < n:
      m = m * 3 + 1
      print m

   elif (m % 2) == 0 and i < n:
      m = m / 2
      print m

   i = i + 1
