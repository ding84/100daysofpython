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
