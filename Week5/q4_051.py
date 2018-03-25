import sys
import string

def mean(l):
    total = 0
    for number in l:
        total = total + number
    return total / len(l)

def mode(l):
    count = 0
    for number in l:
        if l.count(number) > count:
            mode = number
            count = l.count(number)
    return(mode)

def median(l):
    if len(l) % 2 == 0:
       return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
       return l[len(l) // 2]

   
def main():
   numbers = []
   nums_in = sys.stdin.readlines()
   for number in nums_in:
      numbers.append(int(number.strip()))
      numbers = sorted(numbers)

   print('Mean: {:.1f}'.format(mean(numbers)))
   print('Mode: {:.1f}'.format(mode(numbers)))
   print('Median: {:.1f}'.format(median(numbers)))



if __name__ == '__main__':
    main()