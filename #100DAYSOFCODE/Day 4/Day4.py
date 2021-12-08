'''

import random

tails_or_heads = random.randint(0,1)

if tails_or_heads == 0:
  print("Tails")
else:
  print("Heads")

'''
    
'''

import random

# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_list=random.randint(0,len(names)-1)
random_name=names[random_list]
print(f"{random_name} is going to buy the meal today" )

'''

'''

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

sellect_row = map [vertical-1]
sellect_row[horizontal-1]= "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

'''