#!/usr/bin/python3

#
# Day 15 - Project: coffe-machine
#

#
# installing and use of pycharm for windows and mac
# first steps in pycharm and functions of pycharm
# 
#
#

# TODO List for project
# 1. print a report
# 2. resources sufficient?
# 3. process coins
# 4. check transaction successful?
# 5. make coffee

#!/usr/bin/python3.8

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. print a report of all resources
# TODO 2. check if resources valid to make the order
# TODO 3. process coins: check and give change or refund
# TODO 4. check if transaction is successful
# TODO 5. make coffee

#
# def create_report():
#     print(f'Water: {resources["water"]}')
#     print(f'Milk: {resources["milk"]}')
#     print(f'Coffee: {resources["coffee"]}')
#
#
# def make_coffee(drink):
#     request = MENU
#     print(f"Here is your {request}")
#
#
# def take_money(drink):
#     amount_to_pay = 0
#     request = MENU[drink]
#     request_value = request.get("cost")
#     while request_value != amount_to_pay:
#         amount_to_pay = float(input(f"Please pay: {request_value}"))
#         if amount_to_pay > request_value:
#             refund = amount_to_pay - request_value
#             print(f"Your refund is: {refund}")
#             return make_coffee(drink)
#         elif amount_to_pay == request_value:
#             return make_coffee(drink)
#         else:
#             reminding_cost = request_value - amount_to_pay
#             amount_to_pay += float(input(f"Please pay: {reminding_cost} more. Thanks"))
#
#
# def check_resources(drink, MENU, resources):
#     print(drink)
#     if drink in MENU:
#         request = MENU[drink]
#         request_values = request.get("ingredients")
#         water = int(request_values["water"])
#         coffee = int(request_values["coffee"])
#
#         if drink == "espresso":
#             if water > int(resources["water"]):
#                 print("not enough water")
#             elif coffee > int(resources["coffee"]):
#                 print("not enough coffee")
#             else:
#                 take_money(drink)
#         else:
#             milk = int(request_values["milk"])
#             if water > int(resources["water"]):
#                 print("not enough water")
#             elif coffee > int(resources["coffee"]):
#                 print("not enough coffee")
#             elif milk > int(resources["milk"]):
#                 print("not enough milk")
#             else:
#                 take_money(drink)
#
#
# machine_on = True
#
# while machine_on:
#     users_choice = input("What would you like? (espresso / latte / cappuccino): ")
#     if users_choice == "report":
#         create_report()
#     elif users_choice == "espresso" or users_choice == "latte" or users_choice == "cappuccino":
#         check_resources(users_choice, MENU, resources)
#     elif users_choice == "off":
#         machine_on = False
#     else:
#         print("Something went wrong, please try again")



#
# solution code by tutor
#


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

