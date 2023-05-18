# error_handling.py is a file that will contain all of the error handling functions for the program.
# validate_input() will validate the user input based on the parameters passed to it, including the prompt, the expected type, and the valid options.
# prompt is the string that will be displayed to the user when asking for input.
# expected_type is the type that the user input is expected to be. For example, if the user is expected to enter an integer, expected_type should be int.
# valid_options is a list of valid options that the user can enter. If valid_options is not None, the user input must be in the list of valid options.
def validate_input(prompt, expected_type=None, valid_options=None):
    while True:
        user_input = input(prompt) # prompt the user for input, prompt variable will contain the prompt string
        # if the expected type is not None, try to convert the user input to the expected type
        if expected_type is not None:
            try:
                user_input = expected_type(user_input)
            except ValueError:
                # print out the error message for the user
                print("Invalid input. Please try again.")
                # print out the error message for the developer
                print(f"Debug Info: Expected a {expected_type.__name__}, but received {type(user_input).__name__}.")
                continue
        # if valid options are passed to the function, check if the user input is in the list of valid options
        if valid_options is not None and user_input not in valid_options:
            print("Invalid input. Please try again.")
            continue

        return user_input