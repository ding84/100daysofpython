#!/usr/bin/python3

#
# files and project in procjet_coffee_machine folder
#


#import turtle
#from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.color('brown3', 'chartreuse4')
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)

#my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
# table.align["Pokemon"] = "l"
#table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align["Type"] = "l"
# table.align = "l"
# print(table)

#
# project - OOP coffee machine
#

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        print("Shutting down...bye")
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        # is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        # print(f"Please pay: {drink.cost}")
        # is_payment_successful = money_machine.make_payment(drink.cost)
        # if is_enough_ingredients and is_payment_successful:
        #     coffee_maker.make_coffee(drink)
        print(f"Please pay: {drink.cost}")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
