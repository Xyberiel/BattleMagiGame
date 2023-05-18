# main.py will host the main function for the program including the game loop and references to other files.

import random
import time
import os
import sys
import character_classes
from character_classes import Enemy
from character_classes import Player
from error_handling import validate_input
import name_generator
from name_generator import races
from name_generator import generate_name



# Print introduction and welcome screen for Battle Magi
def intro():
    print("Welcome to Battle Magi!")
    print("A text-based RPG adventure game.")
    print("Created by: Anthony Hoganson")
    print("\n")
    print("You are a young mage, just beginning your journey to become a Battle Magi.")
    print("You will face many challenges and enemies along the way.")
    print("Do you have what it takes to become a Battle Magi?\n")
    print("Let's find out!\n")

def start_screen():

    start_screen_options = ["start", "quit"]
    start_screen_input = validate_input("Enter your choice: \n'start' or 'quit'\n", str, start_screen_options)
    
    if start_screen_input == "start":
        player_name = validate_input("What is your name:\n", str)
        player_race = validate_input("What is your race:\n", str)
        player = Player(player_name, player_race)
        print(f"\nWelcome, {player.race} {player.name}!")
        game_loop(player)
    elif start_screen_input == "quit":
        quit_menu()


# main function
def game_loop():
    while True:
        # create the player character
        player = Player("")
        # create the enemy
        enemy = Enemy("")

        # get the player's name
        player.name = validate_input("What is your name:\n", str)
        print("\nWelcome, " + player.name + "!")

        # assign random type to enemy
        enemy.race = random.choice(races)
        if enemy.race[0] in ["A", "E", "I", "O", "U"]:
            print("\nYou will be fighting an " + enemy.race + "!")
        else:
            print("\nYou will be fighting a " + enemy.race + "!")

        # assign random name to enemy
        generate_name(enemy)
        print("\nThe " + enemy.race + "'s name is " + enemy.name + "!")

        # thank the player for playing and inform them that the game is not finished yet
        print("""
Thank you for playing Battle Magi!
This game is still in development, so there is not much to do yet.""")

        # ask the player to press enter to return to start screen
        input("\nPress enter to return to start screen...\n")

        # return to the start screen
        start_screen()


start_screen()

# quit menu
def quit_menu():
    print("Are you sure you want to quit?")
    quit_menu_options = ["yes", "no"]
    quit_menu_input = validate_input("Enter your choice:\n'yes' or 'no'\n", str, quit_menu_options)
    if quit_menu_input == "yes":
        sys.exit()
    elif quit_menu_input == "no":
        return
