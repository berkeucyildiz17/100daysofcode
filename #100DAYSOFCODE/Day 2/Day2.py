'''

num_char = len(input("What is your name ?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

'''

'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

result = first_digit + second_digit

print (result)

'''

'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(float(weight)/(float(height)**2))

'''

'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age=int(age)
days = 365*(90-new_age)
weeks = 52*(90-new_age)
months= 12*(90-new_age)

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)

'''