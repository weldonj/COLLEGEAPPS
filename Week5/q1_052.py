import sys

def main():
   word = sys.argv[1]
   count = int(sys.argv[2]) % len(word)
   if count == 0:
      print(word)
   else:
   
      s = ''
      i = 0
      while i < count:
         s = word[-1:] + word[:-1] 
         word = s
         i = i + 1

      print(s)




if __name__ == '__main__':
    main()