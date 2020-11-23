#!/usr/bin/python3

#
# day9 - dictionarys and nesting
#

# # name = {"key":"Value"}
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])

# #add items to a dict
# programming_dictionary["loop"] = "The action is goind again and again"
# print(programming_dictionary)

# #empty dict
# empty_dictionary = {}

# # clear a dicts content
# programming_dictionary = {}
# print(programming_dictionary)

# #loop through
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])


#
# students grades - excercise
#
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# for key in student_scores:
#     print(key)
#     print(student_scores[key])

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] < 100 and student_scores[key] > 91:
#         student_grades[key] = "Outstanding"         
#     elif student_scores[key] <= 90 and student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] <= 80 and student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

#
# nested dict and lists
#

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"my cities": ["Hamburg", "Stuttgart", "Munich"], "visits": 30}
# }
# print(travel_log["France"])
# print(travel_log["Germany"])

#
# nesting dict in list
#

# travel_log = [
#     {
#         "country":"France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "my cities": ["Hamburg", "Stuttgart", "Munich"], 
#         "visits": 30
#     }
# ]

#
# challenge - travel log
#

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

#my solution
#def add_new_country(country, times_of_visit, city):
#  travel_log.append(
#  {
#    "Country": country,
#    "visits": times_of_visit, 
#    "cities": city})

# def add_new_country(name, visit_count, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


#
# secret auction bid - project
#

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  

