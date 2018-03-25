import sys

def main():
   
   word = 'aeiou'
   lines = sys.stdin.readlines()
   
   for line in lines:
      line = line.strip()
      s = ''
      
      for c in line.lower():
         if c in word:
            s = s + c
      
      if s == word:
         print(line)

if __name__ == '__main__':
    main()