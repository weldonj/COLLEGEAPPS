sum_pos = 0
sum_neg = 0
curr = input()
while curr != 0:

  
   if curr <= 0:
     sum_neg = sum_neg + curr

   else:
     sum_pos = sum_pos + curr
  
   curr = input()

print sum_neg , sum_pos   
   







