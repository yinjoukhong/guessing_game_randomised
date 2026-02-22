# All functions for Number Guessing Game (Randomised) - Python version
# Created by: Khong Yin Jou
# Date: 22/02/2026
# Version: v1.0.0

import config
import sys

debug = config.debug

def debug_print(msg):
    """
    Function to print debug messages with specific format.
        Parameter(s):
            msg (str): message to be printed as part of the debug print
        Return(s):
            None
    """
    print(f"DEBUG: {msg}")

def set_random_limit():
    """
    Function to prompt user to set up the maximum limit for the randomly generated number to be guessed.
        Parameter(s):
            None
        Return(s):
            - maxLimit (int): the maximum limit for the random number generator
    """
    invalidInput = True
    while invalidInput:
        maxLimit = input(f"Please enter a non-negative integer up to {sys.maxsize*2+1:,} for the maximum limit for the randomly generated number to be guessed: ")
        try:
            maxLimit = int(maxLimit)
            if maxLimit < 0:
                print("Please enter only a non-negative integer. Please try again.")
                continue
            elif maxLimit > sys.maxsize*2+1:
                print("Please enter an integer within system limits. Please try again.")
                continue
            invalidInput = False
        except ValueError:
            print("Please enter an integer. Please try again.")
    if debug: debug_print(f"maxLimit = {maxLimit}")
    return maxLimit

def game_logic():
    """
    Function that contains the main logic of the game.
        Parameter(s):
            None
        Return(s):
            None
    """
    attemptIncorrect = True
    while attemptIncorrect:
        print(f'\nThe number is within the range: {config.gameParams["updatedMin"]} - {config.gameParams["updatedMax"]} (inclusive).')
        userAttempt = input("Enter your guess (a non-negative integer): ")
        try:
            userAttempt = int(userAttempt)
        except ValueError:
            print("Please enter only a non-negative integer. Please try again.")
            continue
        config.gameParams["attemptCount"] += 1 # increment (valid) user attempts
        if userAttempt == config.gameParams["numberToGuess"]:
            print(f'\nCONGRATULATIONS!\nYou\'ve guessed it correctly after {config.gameParams["attemptCount"]} tries.')
            attemptIncorrect = False
        else:
            if config.gameParams["updatedMin"] < userAttempt < config.gameParams["numberToGuess"]:
                config.gameParams["updatedMin"] = userAttempt
            elif config.gameParams["numberToGuess"] < userAttempt < config.gameParams["updatedMax"]:
                config.gameParams["updatedMax"] = userAttempt
            print(f'Incorrect guess. Attempts so far: {config.gameParams["attemptCount"]}.')

def reset_game_params():
    """
    Function to reset all the game parameters.
        Parameter(s):
            None
        Return(s):
            None
    """
    for key,param in config.gameParams.items():
        config.gameParams[key] = 0
        if debug: debug_print(f"Setting key {key} to value {config.gameParams[key]}.")