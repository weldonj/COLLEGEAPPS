import sys
import string


def main():
   runner_dict = {}
   fastest_individual_times = []
   runners = sys.stdin.readlines()

   for runner in runners:
      legit_runner = True
      raw_times = []
      runner = runner.strip().split()
      runner_name = runner[0]
      times = runner[1:]
      
      for time in times:
         
         if time.split(':')[0].isdigit() and time.split(':')[1].isdigit():
            raw_times.append((int(time.split(':')[0]) * 60 + int(time.split(':')[1])))
         else:
            legit_runner = False

      if legit_runner == True:         
         fastest_individual_times.append(min(raw_times))
         runner_dict[min(raw_times)] = runner_name
         
   print(runner_dict[min(fastest_individual_times)] + ' : ' + str(min(fastest_individual_times)//60) + ':' + '{:0>2d}'.format(min(fastest_individual_times)%60))


if __name__ == '__main__':
    main()