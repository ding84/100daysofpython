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

#module
print(day4_module.pi)

#seed
random.seed()

#
# head or tail
#

#import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


random_number = random.randint(0,1)

if random_number == 1:
  print("Heads")
else:
  print("Tails")




