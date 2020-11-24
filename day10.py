#!/usr/bin/python3


#
# day 10 - more about functions
#

# def my_function():
#     result = 3 * 2
#     return result

# print(my_function())


##functions with outputs

# def format_name(f_name, l_name):
#   fname = f_name.title()
#   lname = l_name.title()

#   return f"{fname} {lname}"

# print(format_name("tEsT", "nAmE"))


## functions with multiple return values

# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "No name provided"
#   else:
#     fname = f_name.title()
#     lname = l_name.title()

#   return f"{fname} {lname}"

# print(format_name(input("What is your firstname?"), input("What is your lastname?")))
# print(format_name())


#
# days in month
# with docstring
#

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   """ takes year and month and returns days in month.
#   also check for february if we have a leap year """
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#
#
# day 10 project - calculator
#
#

#add
def add(n1, n2):
  return n1 + n2

#subtract
def substract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

operations = {
"-": substract,
"+": add,
"*": multiply,
"/": divide
}

num1 = int(input("Whats the first number? "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick a symbol from the list above: ")
num2 = int(input("Whats the second number? "))

#example
#function = operations["*"]
#print(function(2,3))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer} ")


