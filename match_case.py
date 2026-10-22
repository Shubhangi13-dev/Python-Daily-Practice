'''
marks = 70

match marks:
    case 85|70|75|60|65:
     print(" Grade A")
    case 60|50|55|40:
     print(" Grade B")
    case 70|65|45:
     print(" Grade C")
    case 50|65|45:
     print("Grade E")
    case _ :
     print("Invalid input")


# Quater

Quater = 2

match Quater:
  case 1:
    print("Jan,Feb,Mar")
  case 2:
    print("Apr,May,Jun")
  case 3:
    print("July,Aug,Sep")
  case 4:
    print("Oct,Nov,Dec")
  case _ :
    print("invalid input")


# Arithmetic

num1 = int(input("enter 1st num :"))
num2 = int(input("enter 2nd num :"))

operator = input("enter operator (+,-,=,/,//,*): ")

match operator:
  case "+":
    print("Addition =", num1 + num2)

  case "-":
    print("Subtraction =", num1 - num2)

  case "*":
    print("Multiplication =", num1 * num2)

  case "/":
    if num2 != 0:
      print("Division =", num1 / num2)

    else:
      print("Cannot divide by zero")

  case _:
      print("Invalid operator")'''



# 10 questions

# 1 Integer value match
'''
num = int(input("enter number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")


# 2 String match

fruit = input("enter fruit: ").lower()

match fruit:
    case "apple":
        print("Apple selected")
    case "mango":
        print("Mango selected")
    case "banana":
        print("Banana selected")
    case _:
        print("Fruit not available")


# 3 One case multiple values

day = int(input("enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")


# 4 Guard - case and if

marks = int(input("enter marks: "))

match marks:
    case n if n >= 75:
        print("Distinction")
    case n if n >= 35:
        print("Pass")
    case _:
        print("Fail")


# 5 Variable capture

value = input("enter anything: ")

match value:
    case "hello":
        print("Hello!")
    case name:
        print("you entered:", name)


# 6 Tuple pattern

point = (0,0)

match point:
    case (0,0):
        print("Origin")
    case (x,0):
        print("On X- axis")
    case (0,y):
        print("On Y-axis")
    case (x,y):
        print("Other point")


# 7 List pattern

items = [10,20]

match items:
    case []:
        print("Empty list")
    case [x]:
        print("One item:", x)
    case [x,y]:
        print("Two items:", x, y)
    case _:
        print("Other list")


# 8 List first element match 

numbers = [1, 10, 20]

match numbers:
    case [1, *rest]:
        print("Starts with 1")
        print(rest)
    case _:
        print("Does not start with 1")


# 9 None match

result = None

match result:
    case None:
        print("No result")
    case value:
        print("Result:", value)'''


# 10 Arithmetic operator and guard

a = int(input("enter first number: "))
b = int(input("enter second number: "))
op = (input("enter operator (+, -, *, /):"))

match op:
    case "+":
      print(a+b)
    case "-":
      print(a - b)
    case "*":
      print(a * b)
    case "/" if b != 0:
      print(a / b)
    case "/":
      print("Cannot divide by zero")
    case _:
      print("Invalid operator")






    


