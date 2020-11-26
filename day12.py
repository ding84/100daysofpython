#!/usr/bin/python3


#
# day 12 namespaces, local and global scopes, constants
#

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

