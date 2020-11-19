#!/usr/bin/python3
import random
import day4_module

#random integer
random_integer = random.randint(1,10)
print(random_integer)

#random float
print(random.random())
print(round(random.random(),2))
print(random.random() * 5)

#print var from imported module
print(day4_module.pi)

#seed
random.seed()

#
# head or tail
#

#import random

#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)


random_number = random.randint(0,1)

if random_number == 1:
  print("Heads")
else:
  print("Tails")


#
# lists
#

states_of_america = ["Florida", "Delaware", "Ohio", "Pennsylvania", "Oregon"]
print(states_of_america[1])
print(states_of_america[-1])

states_of_america[0] = "Florda"
print(states_of_america[0])

states_of_america[0] = "Florida"
print(states_of_america[0])

states_of_america.append("New York")
print(states_of_america)

states_of_america.extend(["Washington", "Texas"])
print(states_of_america)

#
# nested lists
#

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
#"Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches","Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


#
# coding challenge - who pays the bill
#

#import random

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

#random.choice(list_name) should do the same trick
random_user = random.randint(0,(len(names)-1))
print(f"{names[random_user]} is going to buy the meal today!")



#
# coding challenge - treasure map
#

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"

#shorter way
#map[vertical -1][horizontal -1] = "X"


print(f"{row1}\n{row2}\n{row3}")



#
# project of the day - rock paper scissors game
#

#import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("Your try: Choose 0 for rock, 1 for paper or 2 for scissors: "))
computer_choice = random.randint(0,2)

hands = [rock, paper, scissors]

# print(hands[user_choice])
# print([computer_choice])
#2 beats 1 and 1 beats 0

if user_choice >= 3 or user_choice < 0:
  print("You typed and invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
  print(hands[user_choice])
  print("Computer choose: \n")
  print(hands[computer_choice])
  print("You win!\n")
elif computer_choice == 0 and user_choice == 2:
  print(hands[user_choice])
  print("Computer choose: \n")
  print(hands[computer_choice])
  print("You lose!\n")
elif computer_choice > user_choice:
  print(hands[user_choice])
  print("Computer choose: \n")
  print(hands[computer_choice])
  print("You lose!\n")
elif user_choice > computer_choice:
  print(hands[user_choice])
  print("Computer choose: \n")
  print(hands[computer_choice])
  print("You win!\n")
elif computer_choice == user_choice:
  print(hands[user_choice])
  print("Computer choose: \n")
  print(hands[computer_choice])
  print("Its a draw\n")


