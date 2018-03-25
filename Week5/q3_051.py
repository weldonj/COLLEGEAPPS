import sys
import string

def main():

   lines = sys.stdin.readlines()
   for line in lines:
      s = ''
      line = line.strip()
      for c in line:
         if c in string.ascii_uppercase:
            s = s + c
         else:
            s = s + ' '
      print(max(s.split(), key=len))


if __name__ == '__main__':
    main()