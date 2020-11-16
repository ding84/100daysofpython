#!/usr/bin/python3

#datatypes and string manipulation

#strings
print("Hello"[4])

print("123" + "456")

#integer
print(123 + 456)

print(123_456_789)

#float
3.14159

#Boolean
True
False

#Data Types

#strings
print("Hello"[4])

print("123" + "456")

#integer
print(123 + 456)

print(123_456_789)

#float
3.14159

#Boolean
True
False

print(len(str(123)))
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("your name hast " + new_num_char + " characters")

#type checking function
print(type(num_char))

print(70 + float(100.52))
print(str(70) + str(100))


##
##
#first challenge

#addition of two digit number with type check
print(int(two_digit_number[0]) + int(two_digit_number[1]))


#mathmatical operators
3+5
7 - 4
4*5
8 / 2
2**3

print(3 * 3 + 3 / 3 - 3)
print(3 / 3 * 3 + 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#
# bmi calculator
#
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = (float(weight) / (float(height) ** 2))

print(round(bmi,2))
print(int(bmi))


#
# f strings
#

score = 1
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height} and your Winning true{isWinning}")

#
# challenge - life in weeks
#

age = input("What is your current age?")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {months_remaining} months, {weeks_remaining} weeks and {days_remaining} days remaining"
print(message)

#
# tip calculator
#

bill = float(input("What was your total bill? $"))
tip = int(input("How much tip do you want? 10, 12, 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

print(total_bill)

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}")

