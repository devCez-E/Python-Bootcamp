from functools import total_ordering


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#simple ver.
#print(sum(student_heights) / len(student_heights))

number_of_student = 0
total_height = 0

for student in student_heights:
    number_of_student += 1
    total_height += student

print(round(total_height / number_of_student))