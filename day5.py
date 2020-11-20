#!/usr/bin/python3

#
# today: loops, range and code blocks
#

#
# for loop
#

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)


#
# exercise - average height
#

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0

for student in student_heights:
  sum += int(student)

student_counter = len(student_heights)
print(round(sum / student_counter))


#
# exercise - highest score
#
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score

print("The highest student score is: " + str(highest_score))

#
# range in for loop
#

#begin end step
for number in range(1, 11, 3):
    print(number)
total = 0
for number in range(1, 101):
    total += number


#
# exercise - sum of all even numbers between 1 and 100
#
total = 0

for number in range(1, 101):
  if (number % 2) == 0:
    total += number

print(total)

#
# exercise - fizz buzz
#

for number in range(1,101):
  if (number % 3 == 0) and (number % 5 == 0):
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)


#
# 
#  project of the day - password generator
#

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

part_letter = ""
part_numbers = ""
part_symbols = ""

letters_length = int(len(letters))
numbers_length = int(len(numbers))
symbols_length = int(len(symbols))


for letter in range(0, nr_letters):
  letnum = random.randint(0, letters_length -1)
  part_letter += letters[letnum]

for number in range(0, nr_numbers):
  numnum = random.randint(0, numbers_length -1)
  part_numbers += numbers[numnum]

for number in range(0, nr_symbols):
  numsym = random.randint(0, symbols_length -1)
  part_symbols += symbols[numsym]

print(f"Your password is: {part_letter}{part_numbers}{part_symbols}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passw = part_letter + part_numbers + part_symbols
password = ""

print(passw)

lenpw = len(passw)
for num in range(0, len(passw)):
  r = random.randint(0, lenpw -1)
  password += passw[r]

print(f"Your better password is {password}")
