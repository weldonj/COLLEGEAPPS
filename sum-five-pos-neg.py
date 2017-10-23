i = 0
sum_pos = 0
sum_neg = 0

while i < 5:

   curr = input()
  
   if curr <= 0:
     sum_neg = sum_neg + curr

   else:
     sum_pos = sum_pos + curr

   i = i + 1   

print sum_neg , sum_pos   
   







