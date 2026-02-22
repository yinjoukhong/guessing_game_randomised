# Number Guessing Game (Randomised) - Python version
# Created by: Khong Yin Jou
# Date: 22/02/2026
# Version: v1.0.0

import random
import config
import functions

debug = config.debug

def main():
    """
    Main function of the number guessing game program.
        Parameter(s):
            None
        Return(s):
            None
    """
    try:
        repeat = True
        while repeat:
            print("\n\nWelcome to the Number Guessing Game (Randomised).\nAuthor: Khong Yin Jou.\n")
            print("GAME START")
            functions.reset_game_params()
            if debug: functions.debug_print(f'After reset: gameParams["updatedMin"] = {config.gameParams["updatedMin"]}')
            maxLimit = functions.set_random_limit()
            config.gameParams["numberToGuess"] = random.randint(0,maxLimit)
            config.gameParams["updatedMax"] = maxLimit
            if debug: functions.debug_print(f'gameParams["numberToGuess"] = {config.gameParams["numberToGuess"]}')
            functions.game_logic()
            repeat = input("Do you want to start a new game? Y/(N): ")
            repeat = repeat=="Y" or repeat=="y"
    except KeyboardInterrupt:
        print("Ctrl+C\nKeyboardInterrupt detected. ", end="")
    print("Ending program.")

if __name__ == "__main__":
    main()