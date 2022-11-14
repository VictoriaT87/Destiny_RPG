# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import random


class player:
    def __init__(self, location, health, items):
        self.location = location
        self.health = health
        self.items = items


guardian = player("opening_scene", 100, [])


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
        chosen_class = input("My class is: ").capitalize()
        classes = ["Hunter", "Warlock", "Titan"]
        if chosen_class in classes:
            print(f"Welcome, {chosen_class}.")
            break
        else:
            print("Please type one of the classes listed.")
            continue
    return chosen_class


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
        print("You didn't find anything")

    building_entrance()


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
        elif action == "no":
            print("The chest looks old and worn...")
            print("You don't think you'll find anything of value in there.")
            print("You move into the building.")
        else:
            print("Please enter Yes or No.")


def check_items():
    item_find = random.choice([True, False])
    if item_find is True:
        guardian.items.append("key")
        print("You've found a key!")


def check_weapon():
    weapon_find = random.choice([True, False])
    if weapon_find is True:
        weapon = random.choice([
                                "Zhalo Supercell",
                               "The Last Word",
                               "No Land Beyond",
                               "Felwinter's Lie",
                               "Gjallarhorn"
                               ])
        guardian.items.append(weapon)
        print(f"You've found a {weapon}!")


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
    get_class()
    opening_scene()


main()
