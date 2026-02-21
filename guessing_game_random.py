# Number Guessing Game (Randomised) - Python version
# Created by: Khong Yin Jou
# Date: 21/02/2026
# Version: v1.0.0

import random
import sys

debug = False # debug flag

try:
    repeat = True
    while repeat:
        print("\n\nWelcome to the Number Guessing Game (Randomised).\nAuthor: Khong Yin Jou.\n")
        print("GAME START")
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
        if debug: print(f"maxLimit = {maxLimit}")
        gameParams = {
            "numberToGuess": random.randint(0,maxLimit),
            "attemptCount": 0,
            "updatedMin": 0,
            "updatedMax": maxLimit
        }
        if debug: print(f'gameParams["numberToGuess"] = {gameParams["numberToGuess"]}')

        attemptIncorrect = True
        while attemptIncorrect:
            print(f'\nThe number is within the range: {gameParams["updatedMin"]} - {gameParams["updatedMax"]} (inclusive).')
            userAttempt = input("Enter your guess (a non-negative integer): ")
            try:
                userAttempt = int(userAttempt)
            except ValueError:
                print("Please enter only a non-negative integer. Please try again.")
                continue
            gameParams["attemptCount"] += 1 # increment (valid) user attempts
            if userAttempt == gameParams["numberToGuess"]:
                print(f'\nCONGRATULATIONS!\nYou\'ve guessed it correctly after {gameParams["attemptCount"]} tries.')
                attemptIncorrect = False
            else:
                if gameParams["updatedMin"] < userAttempt < gameParams["numberToGuess"]:
                    gameParams["updatedMin"] = userAttempt
                elif gameParams["numberToGuess"] < userAttempt < gameParams["updatedMax"]:
                    gameParams["updatedMax"] = userAttempt
                print(f'Incorrect guess. Attempts so far: {gameParams["attemptCount"]}.')
        repeat = input("Do you want to start a new game? Y/(N): ")
        if repeat == "Y" or repeat == "y":
            repeat = True
        else:
            repeat = False
except KeyboardInterrupt:
    print("Ctrl+C\nKeyboardInterrupt detected. ", end="")
print("Ending program.")