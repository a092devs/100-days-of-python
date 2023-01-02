# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
for i in student_heights:
    total_height += i
print(f"Total height of students: {total_height}")

total_num_of_students = 0
for i in student_heights:
    total_num_of_students += 1
print(f"Total number of students: {total_num_of_students}")

avg_height = round(total_height/total_num_of_students)
print(f"Average height of {total_num_of_students} students is: {avg_height}")