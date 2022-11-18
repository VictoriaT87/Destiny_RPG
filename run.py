import gspread
from google.oauth2.service_account import Credentials

import sys
import random
# import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Destiny_RPG')

worksheet = SHEET.worksheet('Stats')

# def slow_text(text):
#     """
#     Slows the speed of the text being printed.
#     https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
#     """
#     text += "\n"
#     for char in text:
#         time.sleep(0.04)
#         print(char, end="", flush=True)


class Player:
    """
    Class for player inventory and weapon.
    """

    def __init__(self, items):
        self.items = items

    def weapons(self):
        """
        Connect to weapon cell in spreadsheet
        """
        worksheet_weapon = worksheet.cell(2, 4).value
        return worksheet_weapon


guardian = Player([])
stored_weapon = Player.weapons('')


def get_name():
    """
    Get the name of the player.
    """
    print("Eyes up, Guardian.\n")
    print("I've finally found you.\n")
    print("I've been searching for you for centuries.\n")
    print("What should I call you?")
    while True:
        name = input("\n> ").capitalize()
        # https://www.w3schools.com/python/ref_string_isalpha.asp
        if not name.isalpha():
            print("Please enter letters only.")
            continue
        else:
            print(f"It's nice to meet you, {name}. I'm your Ghost.")
            break
    return name


def get_class():
    """
    Player chooses their class. 3 available based on Destiny lore.
    """
    print("Let's try to figure out what kind of Guardian you are... \n")
    print("Do you think you're a Hunter, Warlock or Titan?\n")
    print("Hunter: Agile and daring, Hunters are quick on their feet")
    print("and quicker on the draw.\n")
    print("Warlock: Warlocks weaponize the mysteries of the universe")
    print("to sustain themselves and devastate their foes.\n")
    print("Titan: Disciplined and proud, Titans are capable of both ")
    print("aggresive assaults and stalwart defenses.\n")
    while True:
        chosen_class = input("My class is: \n> ").capitalize()
        classes = ["Hunter", "Warlock", "Titan"]
        if chosen_class in classes:
            print(f"Welcome, {chosen_class}.")
            print("\n")
            break
        else:
            print("Please type one of the classes listed.")
            continue
    return chosen_class


def get_subclass(chosen_class):
    """Players choose their subclass - each class has 3."""

    print("Each Lightbearer has a choice... \n")
    print("Your subclass defines your personality and skill.")
    print("You must choose now. Are you a... \n")

    if chosen_class == "Hunter":
        subclasses = ['Nightstalker?', 'Blade Dancer?', 'Gunslinger?']

    elif chosen_class == "Warlock":
        subclasses = ['Voidwalker?', 'Sunsinger?', 'Stormcaller?']

    elif chosen_class == "Titan":
        subclasses = ['Striker?', 'Defender?', 'Sunbreaker?']

    for index, subclass in enumerate(subclasses, 1):
        print(index, subclass)
    choice = int(input(f"Make your choice, {chosen_class} \n> "))
    print(f"A {subclasses[choice-1]} The darkness doesn't stand a chance \n")

    chosen_subclass = subclasses[choice-1]
    return chosen_subclass


def opening_scene():
    """
    First scene to play after choosing a name and class
    """

    print("You look around and notice you're in a familiar place...")
    print("This is the Cosmodrome. The last thing you remember is fighting")
    print("here in a war against The Fallen.")
    print("But now everything is overgrown, it feels as if centuries")
    print("have passed.\n")
    print("You look around. Behind you is a cliff edge.")
    print("In front of you are some cars. Beyond them is an entrance")
    print("to a building.")
    print("What do you want to do?\n")
    print("1. Search the cars?")
    print("2. Go to the building entrance?")
    print("3. Run off the cliff behind you? This is all too weird!")

    user_input = ""

    user_input = input("\n> ")
    if user_input == "1":
        search_cars()
    elif user_input == "2":
        building_entrance()
    elif user_input == "3":
        print("You run towards the cliff and jump! This is all too much")
        print("to take. [END]")
        sys.exit()
    else:
        print("Please enter a valid option.")


def search_cars():
    """
    Function to search the cars
    """
    print("You decide to search through some of the abandoned cars.")
    check_items()
    print(guardian.items)

    if guardian.items == ["key"]:
        print("You put your key away and walk towards the building.")
    else:
        print("But you didn't find anything")


def building_entrance():
    """
    Function to enter the building and try to open a chest
    """

    print("The building is long abandoned, rust covers the doors")
    print("All the windows are broken.")
    print("In front of you, you see a chest...\n")
    print("Try to open the chest?")
    print("Yes or No")

    while True:
        action = input("\n> ")
        if action == "yes" and guardian.items == ["key"]:
            guardian.items.remove("key")
            print("You've used your key!")
            check_weapon()
        elif action == "yes" and guardian.items == []:
            print("You don't have a key and the lock won't budge.")
            print("You decide to move on")
            building_hallway()
        elif action == "no":
            print("The chest looks old and worn...")
            print("You don't think you'll find anything of value in there.")
            print("You move into the building.")
            building_hallway()
        else:
            print("Please enter Yes or No.")


def building_hallway():
    """
    Function to play scene on entering the building hallway,
    call fight scene or end
    """
    print("You enter into a long hallway inside the building")
    print("Everything seems eerily quiet...")
    print("Suddenly, a loud bang!")
    print("You peer into the darkness ahead")
    print("and slowly make out a shape...\n")
    print("You see a Dreg! A soldier of the Fallen!")
    print("He runs at you, holding a weapon.")
    print("What do you do?")
    print("Fight or Run [END]?")

    user_input = ""

    user_input = input("\n> ").capitalize()
    if user_input == "Fight":
        dreg_fight(check_weapon)
    elif user_input == "Run":
        print("You've alerady died once fighting Dregs")
        print("You're not doing it again.")
        print("You flee and run back to the cliff...")
        print("And jump!")
        print("[END]")

        sys.exit()
    else:
        print("Please enter a valid option.")


def dreg_fight(weapon):
    """
    fight scene function, checks for weapon from random roll
    or else use abilities
    """

    if stored_weapon:
        print(f"You pull out your {weapon}")
        print("line up on the Dreg's head...")
        print("and pull the trigger.")
        print("Nice work!")
    else:
        print("You don't have a gun... but you do have your abilities")
        print(f"You're a {get_class}. A {get_subclass}.")
        print("You throw your grenade!")
        print("It sticks to the Dreg")
        print("and explodes in a burst of Light!")
        print("Nice work! The Dreg is dust.")


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
        worksheet.update_cell(2, 4, weapon)
        print(f"You've found a {weapon}!")
        return weapon

    elif weapon_find is False:
        print("There was nothing in the chest, only dust...")  
    building_hallway()


def main():
    """
    Introduction to the game to run first
    """

    print("Welcome Guardian!")
    print("This is a text adventure game based on the video game Destiny!\n")
    print("You are a New Light - a person newly re-awoken by a small")
    print("robot companion known as a Ghost.")
    print("You are now a Guardian, chosen to wield the Light")
    print("to defeat the Darkness.\n")

    print("Let's get your adventure started!\n")
    print("\n")

    get_name()
    get_subclass(get_class())
    opening_scene()
    building_entrance()
    building_hallway()
    check_weapon()


main()
