import sys
import os
import random
import time

import gspread
from google.oauth2.service_account import Credentials

from character import guardian

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Destiny_RPG')

stats_worksheet = SHEET.worksheet('PlayerStats')


def reset_console():
    """
    Reset the console for a new game or continue.
    """
    print("\n")
    os.system('cls||clear')


def play_again():
    """
    Option to allow player to play again or exit
    """
    print("Yes or No?")
    user_input = ""
    user_input = input("\n> ").capitalize()
    if user_input == "Yes":
        reset_console()
        run.introduction()
    elif user_input == "No":
        print("Thank you for playing, Guardian!")
        clear_worksheet()
        sys.exit()
    else:
        print("Please enter Yes or No.")


def clear_worksheet():
    """
    Clear player spreadsheet at start of game
    """
    stats_worksheet.delete_rows(2)


def inital_luck():
    """Roll an Inital Luck number for the character"""
    character_luck = random.randint(0, 100)
    stats_worksheet.update_cell(2, 5, character_luck)
    return character_luck


def check_items():
    """
    Function to check if the player has an key in their inventory
    """
    item_find = random.choice([True, False])
    if item_find is True:
        guardian.items.append("key")
        print("You've found a key!")


def check_weapon():
    """
    Function to choose if the player gets a random weapoon from the chest
    """
    weapon_find = random.choice([True, False])
    if weapon_find is True:
        weapon = random.choice([
            "Zhalo Supercell",
            "The Last Word",
            "No Land Beyond",
            "Felwinter's Lie",
            "Gjallarhorn"
        ])
        stats_worksheet.update_cell(2, 4, weapon)
        print(f"You've found a {weapon}!")
        # if player finds a weapon, update their luck
        if stats_worksheet.cell(2, 5).value < "50":
            character_luck = random.randint(50, 100)
            stats_worksheet.update_cell(2, 5, character_luck)

    else:
        print("There was nothing in the chest, only dust...")

    return weapon


def handle_vandal():
    """
    function for random Vandal encounter
    """
    vandal_attack = random.choice([True, False])
    if vandal_attack is True:
        print("Out of nowhere, a Fallen Vandal attacks you!")
        print("You took some damage :(")
        guardian.health -= random.randint(1, 100)
        print(f"\nHealth: {guardian.health}")
        if guardian.health < 0:
            print("You are dead!")
            print("Your Ghost can ressurect you. Do you want him to?")
            play_again()


def slow_text(text):
    """
    Slows the speed of the text being printed.
    https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
    """
    text += "\n"
    for char in text:
        time.sleep(0.09)
        print(char, end="", flush=True)
