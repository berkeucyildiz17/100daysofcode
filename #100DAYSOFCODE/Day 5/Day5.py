'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_hight = 0
for hight in student_heights :
    total_hight += hight

total_student = 0
for student in student_heights:
    total_student += 1

Average = round(total_hight/total_student)
print(Average)

'''

'''

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for score in student_scores:
  if score>highest_score:
      highest_score = score

print(f"The highest score in the class is: {highest_score}")

'''

'''

#Write your code below this row 👇
Total = 0
for numbers in range (2,101,2) :
   Total += numbers
print(Total)


Total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        Total2 += number
print(Total2)

'''

'''

#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

'''