def Add (n1, n2):
    return n1 + n2

def Subtract (n1,n2):
    return n1 - n2

def Multiply (n1,n2):
    return n1 * n2

def Devide (n1,n2):
    return n1 / n2

operations = {
   "+" : Add,
   "-" : Subtract,
   "*" : Multiply,
   "/" : Devide
   }

num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
should_continue = True

while should_continue:
    
  operation_symbol = input("Pick an operatipon : ")
  num2 = int(input("What's the next number? "))
  calculator_function = operations[operation_symbol]
  answer1 = calculator_function(num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer1}")

  again = input(f"Type 'y' to continue claculating with {answer1}, or type 'n' to exit. : ")
  if again == "y":
      num1 = answer1
  else: 
      should_continue = False





