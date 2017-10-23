n = input()

i = 0
prev = 0
curr = 1
   
while i < n:
   print curr
   curr = prev + curr
   prev = curr - prev
   
   
   i = i + 1
