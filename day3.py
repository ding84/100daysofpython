#control structures, data flow, 


number = int(input("Which number do you want to check? "))
result = number % 2

if number % 2 == 0:
  print(f"This is even {result}")
else:
  print(f"This is odd {result}")

#
# rollercoaster with elif
#
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Welcome, you can ride the rollercoaster")
  age = int(input("What is your age"))
  if age < 12:
    print("Please pay 5$")
  elif age <= 18:
    print("Please pay 7$")
  else:
    print("Please pay 12$")  
else:
  print("Sorry, you have to grow taller before you can ride.")

#
# bmi calculator 2.0
#

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")




