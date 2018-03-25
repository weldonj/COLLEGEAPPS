import sys

def main():
   s = ''	
   line = sys.argv[1]

   if len(line) == 1:
      print(line)

   elif len(line) % 2 == 0:
      i = 0
      while i < len(line):
         s = s + line[i + 1] + line[i]
         i = i + 2
      print(s)

   else:
      i = 0
      while i < len(line) - 1:
         s = s + line[i + 1] + line[i]
         i = i + 2
      print(s + line[-1])


if __name__ == '__main__':
	main()