#!/usr/bin/python3

#print several strings with source code inside print
print("Day 1 - Python print Function")
print("The function is declared like this:")
print('print("what to print")')

#one print
print("Hello World")
#on print on three lines
print("Hello World\nHello World\nHello World\n")
print("Hello" + "" + "Dirk")
print("Hello " + "Dirk")

#coding exercise 2
print("Day 1 - String Manipulation")
print('String Concatenation is done with the '"+"' sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#print and input function
print("What is your name?")
input("What is your name?")
print("hello " + input("what is your name?") + "!")

#print length of users name given by input
print("Get lenght of user name")
s = input("What is your name? ")
print(len(s))

print(len(input("What is your name? ")))

#variables
name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)


#coding exercise on variables
#swap variables
a = 5
b = 10
a, b = b, a

#daily project: band name generator
print("Welcome to my Band Name Generator")
city = input("Name a city you grew up in:\n")
pet = input("Name a pet you had:\n")
print("Your Bandname could be: " + city + " " + pet)




