#!/usr/bin/python3

import random
import archer_art

#
# todo: new game or old game? same users as before?
#
def game_settings():
    """Function for settings like player names, number of players and so on"""
    settings = []
    number_of_shots = str(5)
    player_one = input("Name of Player1: ")
    player_two = input("Name of Player2: ")
    settings.append(number_of_shots)
    settings.append(player_one)
    settings.append(player_two)
    
    return settings


def shoot_arrow(player_number):
    """Function to create a random int for a target"""


def count_players_score(player_number, score_to_add):
    """Function for saving players score"""


def compare_score(player_one_score, player_two_score):
    """Function for comparing players scores"""


game_ends = False

print(archer_art.logo)

while not game_ends:

    print("Welcome to archers game")

    game_settings()


    if input("Play another round? 'y' for yes 'n' for no: ") == "n":
        print("Thanks for playing")
        game_ends = True






