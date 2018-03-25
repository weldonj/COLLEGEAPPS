import sys

def build_dictionary(filename):
   with open(filename, 'r') as f:
      d = {}
      lines = f.readlines()
      for line in lines:
         d[' '.join(line.strip().split()[0:-1])] = int(line.strip().split()[-1])
      return d


def main():
   person_dict = {}
   person_list = []
   totals_list = []
   calories = build_dictionary('calories.txt')
   info = sys.stdin.readlines()

   for line in info:
      total = 0
      person = line.strip().split(',')
      name, food = person[0], person[1:]

      for food in food:

         if food in calories:
            total = total + calories[food]
         else:
            total = total + 100

      totals_list.append(total)
      person_list.append(name)
      person_dict[total] = name
   totals_list = sorted(totals_list)
   num_strings = []
   for total in totals_list:
      num_strings.append(str(total))
   max_name = len(max(person_list, key=len))
   max_num = len(max(num_strings, key=len))
   for total in totals_list:
      print('{:>{}} : {:{}}'.format(person_dict[total], max_name, total, max_num))



if __name__ == '__main__':
    main()