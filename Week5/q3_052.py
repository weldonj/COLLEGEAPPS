def build_dictionary(filename):
   with open(filename, 'r') as f:
      d = {}
      lines = f.readlines()
      for line in lines:
         d[line.strip().split()[0]] = int(line.strip().split()[1])
      return d

   
def extract_range(d, low, high):
   new_d = {}
   for key in d:
      if d[key] >= low and d[key] <= high:
         new_d[key] = d[key]
   return new_d