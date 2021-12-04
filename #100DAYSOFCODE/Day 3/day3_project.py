print("Welcome to Treasure Island.Your mission is to find the treasure")

way = input("Left or right ? ")


if way == "left" :
   how = input("Swim or wait ?")
   if how == "wait":
       door = input("Which door ? ")
       if door == 'yellow':
          print("You Win!")

       else:
           print("Game over")
           
   else:
       print("Game over")

else:
    print("Game over") 