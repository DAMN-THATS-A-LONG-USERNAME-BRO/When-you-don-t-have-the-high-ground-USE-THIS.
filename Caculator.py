operation = input("Please choose the operator which you would like to implement!")
number = int(input("Please choose a number! "))
number2 = int(input("Please choose another number! "))
if operation == "add":
  add = (number+number2)
  print(add)
if operation == "subtract":
  subtract = (number-number2)
  print(subtract)
if operation == "divide":
  divide = (number/number2)
  print(divide)
if operation == "multiply":
  multiply = (number*number2)
  print(multiply)
if operation == "power":
  power = (number**number2)
  print(power)
