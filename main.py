# main.py will host the main function for the program including the game loop and references to other files.

import random
import time
import os
import sys
import character_class
from error_handling import validate_input
from quit_screen import quit_menu

# introduction screen
def start_screen():
    # ASCII art for the title screen
    print("""
    
     ______   _______ __________________ _        _______    _______  _______  _______ _________
    (  ___ \ (  ___  )\__   __/\__   __/( \      (  ____ \  (       )(  ___  )(  ____ \\__   __/
    | (   ) )| (   ) |   ) (      ) (   | (      | (    \/  | () () || (   ) || (    \/   ) (   
    | (__/ / | (___) |   | |      | |   | |      | (__      | || || || (___) || |         | |   
    |  __ (  |  ___  |   | |      | |   | |      |  __)     | |(_)| ||  ___  || | ____    | |   
    | (  \ \ | (   ) |   | |      | |   | |      | (        | |   | || (   ) || | \_  )   | |   
    | )___) )| )   ( |   | |      | |   | (____/\| (____/\  | )   ( || )   ( || (___) |___) (___
    |/ \___/ |/     \|   )_(      )_(   (_______/(_______/  |/     \||/     \|(_______)\_______/
                                                                                            

    """)
    # Brief description of the game
    print("""
    Welcome to Battle Magi!
    Battle Magi is a turn based text game with a complex battle system and modular magic system.
    You will be able to create your own character and fight enemies in a turn based battle system.
    You will be able to use a variety of weapons and magic spells to defeat your enemies.
    """)
    # ask the user if they are ready to begin the game
    print("""
    When you are ready to begin, enter 'start' to begin the game.
    Enter 'quit' to quit the game.
    """)

    start_screen_options = ["start", "quit"]
    start_screen_input = validate_input("Enter your choice: \n'start' or 'quit'\n", str, start_screen_options)
    
    if start_screen_input == "start":
        game_loop()
    elif start_screen_input == "quit":
        quit_menu()


# main function
def game_loop():
    while True:
        # create the player character
        player = character_class.Character()
        # create the enemy
        enemy = character_class.Character()

        # get the player's name
        player.name = validate_input("What is your name:\n", str)
        print("\nWelcome, " + player.name + "!")

        # assign random type to enemy
        enemy.mob_type = random.choice(["Goblin", "Orc", "Troll", "Dragon"])
        if enemy.mob_type[0] in ["A", "E", "I", "O", "U"]:
            print("\nYou will be fighting an " + enemy.mob_type + "!")
        else:
            print("\nYou will be fighting a " + enemy.mob_type + "!")

        # assign one of ten random monster names to enemy
        enemy.name = random.choice(["Gnarltooth", "Grimtooth", "Goretooth", "Gorebelly", "Grimbelly", "Gnarlbane", "Gorebane", "Grimbane", "Gnarlfang", "Gorefang", "Grimfang",
                                   "Gnarlsnarl", "Goresnarl", "Grimsnarl", "Gnarlscale", "Gorescale","Grimscale", "Gnarlpelt", "Gorepelt", "Grimpelt", "Gnarlskin", "Goreskin",
                                  "Grimskin", "Gnarlblood", "Goreblood", "Grimblood", "Gnarlfist", "Gorefist", "Grimfist", "Gnarlbasher", "Gorebasher", "Grimbasher"])
        print("\nThe " + enemy.mob_type + "'s name is " + enemy.name + "!")

        # thank the player for playing and inform them that the game is not finished yet
        print("""
Thank you for playing Battle Magi!
This game is still in development, so there is not much to do yet.""")

        # ask the player to press enter to return to start screen
        input("\nPress enter to return to start screen...\n")

        # return to the start screen
        start_screen()


start_screen()
