# file = open("my_file.txt", 'r')
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="a") as file:
    # contents = file.read()
    file.write("\nMy favorite food is pizza")
    # print(contents)