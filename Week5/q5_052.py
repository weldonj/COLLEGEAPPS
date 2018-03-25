import sys

def main():
   student_dict = {}
   legit_students = []
   skipped_students = []
   individual_totals = []

   students = sys.stdin.readlines()
   for student in students:
      
      legit_student = True
      score = 0
      name = student.strip().split(':')[0]
      marks = student.strip().split(':')[1]
      marks = marks.split(',')
      for mark in marks:
         if mark.isdigit():
            score = score + int(mark)
         else:
            legit_student = False


      if legit_student == True:
         legit_students.append(name)
         individual_totals.append(score)
         student_dict[score] = name
      else:
         skipped_students.append(name)

   individual_totals = sorted(individual_totals, reverse=True)

# Output from here on

   for score in individual_totals:
      print(student_dict[score] + ' : ' + str(score))

   print('Skipped:')
   for student in skipped_students:

      print(student)


if __name__ == '__main__':
    main()