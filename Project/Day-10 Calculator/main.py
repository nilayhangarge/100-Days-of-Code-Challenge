from replit import clear
from art import logo
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  clear()
  print(logo)
  
  num1 = float(input("\nWhat's the first number? "))
  
  for symbols in operations:
    print(symbols)
  
  repeat = "y"
  while repeat == "y":
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    
    function = operations[operation_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    num1 = answer
    
    repeat = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if repeat == "n":
      print("BYE!!")
      calculator()

calculator()