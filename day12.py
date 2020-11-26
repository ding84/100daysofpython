#!/usr/bin/python3


#
# day 12 namespaces, local and global scopes, constants
#

################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

###### local scope #####

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()

##### global scope #####

#global variable
#player_health = 10

#def game():
  #local scope of drink_potion
#  def drink_potion():
    #local variable
  #   potion_strength = 2
  #   print(player_health)

  # drink_potion()
#undefined function because not in scope available
#drink_potion()


## there is no blockscope

#if 3 > 2:
  #available inside and outside of if
#  a_variable = 10

# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]
#     print(new_enemy)

#not available because out of scope of function 
#print(new_enemy)


#
# global constants
#

# PI = 3.1415

# def calc():
#   print(PI)




#
# project number guessing game
#


from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

