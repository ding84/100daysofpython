#!/usr/bin/python3

#
# day 8 - functions with parameters
#

# def greet():
#   print("Hello")
#   print("How do you do")
#   print("Isn't the weather nice today?")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do, {name}?")

# greet_with_name("Dirk")

#
# function with multiple inputs / positional arguments
#

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"Your location is: {location}")

#positional arguments
#greet_with("Dirk", "London")
#greet_with("Nowhere", "Jack")

#greeting with functional parameter
# greet_with(location = "London", name = "Jack")

#
# prime checker
#

# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number - 1):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It is a prime number")
#   else:
#     print("It is not a prime number")

# n = int(input("Check this number: "))
# prime_checker(number=n)

#
# caesar encrypter
#
import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
print(caesar_art.logo)

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 25
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
