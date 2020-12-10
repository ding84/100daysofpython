#
# list comprehension
#

numbers = [1, 2, 3, 4]

new_list = [n + 1 for n in numbers]
print(numbers)
print(new_list)

newlist = [i * i for i in numbers]
print(newlist)

name = "Angela"
new_name = [letter for letter in name]
print(new_name)

new_num = [a * 2 for a in range(1, 5)]
print(new_num)

# put all names shorter than 5 characters in a new list
# my_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names_list = [a for a in my_names if len(a) < 5]
# print(new_names_list)

my_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names_list = [a.upper() for a in my_names if len(a) > 5]
print(new_names_list)


# challenge - square all numbers
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_number_list = [c**2 for c in number_list]
print(new_number_list)
