#!/usr/bin/python3

#
#
# day6: functions, while loops
# stuff takes part on reeborg.ca
#

def my_function():
  print("Hello")
  print("Bye")

my_function()

#
# robot hurdle race
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# for step in range(6):
#     jump()

# or

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1


#robot hurdle race with different end points

# while at_goal != True:
#     jump()

#or

# while not at_goal:
#   jump()


#
# hurdles with variable positions
#

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()



#
# hurdles with variable positions and height
#

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#
# project - escape the maze
#

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

#
# following while is used to prevent getting stuck
#

# while front_is_clear():
#     move()
# turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


