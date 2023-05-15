# main.py will host the main function for the program including the game loop and references to other files.

import random
import time
import os
import sys
import character_class

# introduction screen
def intro():
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
    print("Welcome to Battle Magi!")
    print("Battle Magi is a turn based text game with a complex battle system and modular magic system.")
    print("You will be able to create your own character and fight enemies in a turn based battle system.")
    print("You will be able to use a variety of weapons and magic spells to defeat your enemies.")
    print("When you are ready to begin, enter 'start' to begin the game.")
    print("Enter 'help' at any time to view the help menu.")
    print("Enter 'quit' at any time to quit the game.")
    print("Enter 'credits' at any time to view the credits.")

def main():
    intro()
    while True:
        command = input("Enter a command: ").lower()
        if command == "start":
            character_class.character_creation()
            break
        elif command == "help":
            print("Help menu")
        elif command == "quit":
            sys.exit()
        elif command == "credits":
            print("Credits")
        else:
            print("Invalid command. Please try again.")

main()
