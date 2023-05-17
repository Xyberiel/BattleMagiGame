import sys
#from error_handling import validate_input


# quit menu
def quit_menu():
    print("Are you sure you want to quit?")
    quit_menu_options = ["yes", "no"]
    quit_menu_input = validate_input("Enter your choice:\n'yes' or 'no'\n", str, quit_menu_options)
    if quit_menu_input == "yes":
        sys.exit()
    elif quit_menu_input == "no":
        return
