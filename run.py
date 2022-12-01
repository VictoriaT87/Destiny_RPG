"""
The main game file which imports the story.
"""

import os
import pyfiglet
import functions
import text
import character


def introduction():
    """
    First function to run on Start.
    Logo image, introduction text, luck roll and worksheet cleared
    """

    text1 = pyfiglet.figlet_format("DESTINY", justify="center")
    text2 = pyfiglet.figlet_format("RPG GAME", justify="center")
    print(text1)
    print(text2)

    text.introduction_text()

    while True:
        user_input = input("Press ENTER to begin: ")
        if user_input == "":
            print("The game will now begin!")
            start_game()
        else:
            print(f"You typed '{user_input}'. The game will not start yet.")
            continue


def start_game():
    """
    Begins game, collecting information such as player name, class, race and
    preferred weapons.
    """

    functions.GameFunctions.clear_worksheet("")
    functions.GameFunctions.inital_luck("")
    character.UserInputs.get_name("")
    os.system("clear")


if __name__ == "__main__":
    introduction()
