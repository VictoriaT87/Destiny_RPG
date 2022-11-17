# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import random
import time


def slow_text(text):
    """
    Slows the speed of the text being printed.
    https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
    """
    text += "\n"
    for char in text:
        time.sleep(0.04)
        print(char, end="", flush=True)


class Player:
    """
    Class for player health and inventory.
    """
    def __init__(self, health, items):
        self.health = health
        self.items = items


guardian = Player(100, [])


def get_name():
    """
    Get the name of the player.
    """
    slow_text("Eyes up, Guardian.\n")
    slow_text("I've finally found you.\n")
    slow_text("I've been searching for you for centuries.\n")
    slow_text("What should I call you?")
    while True:
        name = input("\n> ").capitalize()
        # https://www.w3schools.com/python/ref_string_isalpha.asp
        if not name.isalpha():
            slow_text("Please enter letters only.")
            continue
        else:
            slow_text(f"It's nice to meet you, {name}. I'm your Ghost.")
            break
    return name


def get_class():
    """
    Player chooses their class. 3 available based on Destiny lore.
    """
    slow_text("Let's try to figure out what kind of Guardian you are... \n")
    slow_text("Do you think you're a Hunter, Warlock or Titan?\n")
    slow_text("Hunter: Agile and daring, Hunters are quick on their feet")
    slow_text("and quicker on the draw.\n")
    slow_text("Warlock: Warlocks weaponize the mysteries of the universe")
    slow_text("to sustain themselves and devastate their foes.\n")
    slow_text("Titan: Disciplined and proud, Titans are capable of both ")
    slow_text("aggresive assaults and stalwart defenses.\n")
    while True:
        chosen_class = input("My class is: \n> ").capitalize()
        classes = ["Hunter", "Warlock", "Titan"]
        if chosen_class in classes:
            slow_text(f"Welcome, {chosen_class}.")
            slow_text("\n")
            break
        else:
            slow_text("Please type one of the classes listed.")
            continue
    return chosen_class


def get_subclass(chosen_class):
    """
    Players choose their subclass - each class has 3.
    """
    slow_text("Each Lightbearer has a choice... \n")
    slow_text("Your subclass defines your personality and skill.")
    slow_text("You must choose now. Are you a... \n")

    if chosen_class == "Hunter":
        slow_text("1. Nightstalker?")
        slow_text("2. Blade Dancer?")
        slow_text("3. Gunslinger?")

        while True:
            subclasses = {'1': 'Nightstalker',
                               '2': 'Blade Dancer',
                               '3': 'Gunslinger'}
            subclass = input("\n> ")
            if subclass in subclasses:
                # https://stackoverflow.com/questions/66484472/check-python-list-dict-based-on-user-input-display-from-the-same-index-value-i
                slow_text(f"A {subclasses[subclass]}?")
                slow_text("The Darkness doesn't stand a chance.\n")
                break
            else:
                slow_text(
                    """
                    Please choose either 1, 2 or 3.
                    """
                )
                continue

    return subclass


def opening_scene():
    """
    First scene to play after choosing a name and class
    """

    slow_text("You look around and notice you're in a familiar place...")
    slow_text("This is the Cosmodrome. The last thing you remember is fighting")
    slow_text("here in a war against The Fallen.")
    slow_text("But now everything is overgrown, it feels as if centuries")
    slow_text("have passed.\n")
    slow_text("You look around. Behind you is a cliff edge.")
    slow_text("In front of you are some cars. Beyond them is an entrance")
    slow_text("to a building.")
    slow_text("What do you want to do?\n")
    slow_text("1. Search the cars?")
    slow_text("2. Go to the building entrance?")
    slow_text("3. Run off the cliff behind you? This is all too weird!")

    user_input = ""

    user_input = input("\n> ")
    if user_input == "1":
        search_cars()
    elif user_input == "2":
        building_entrance()
    elif user_input == "3":
        slow_text("You run towards the cliff and jump! This is all too much")
        slow_text("to take. [END]")
        sys.exit()
    else:
        slow_text("Please enter a valid option.")


def search_cars():
    """
    Function to search the cars
    """
    slow_text("You decide to search through some of the abandoned cars.")
    check_items()
    slow_text(guardian.items)

    if guardian.items == ["key"]:
        slow_text("You put your key away and walk towards the building.")
    else:
        slow_text("But you didn't find anything")

    building_entrance()


def building_entrance():
    """
    Function to enter the building and try to open a chest
    """

    slow_text("The building is long abandoned, rust covers the doors")
    slow_text("All the windows are broken.")
    slow_text("In front of you, you see a chest...\n")
    slow_text("Try to open the chest?")
    slow_text("Yes or No")

    while True:
        action = input("\n> ")
        if action == "yes" and guardian.items == ["key"]:
            guardian.items.remove("key")
            slow_text("You've used your key!")
            check_weapon()
        elif action == "yes" and guardian.items == []:
            slow_text("You don't have a key and the lock won't budge.")
            slow_text("You decide to move on")
        elif action == "no":
            slow_text("The chest looks old and worn...")
            slow_text("You don't think you'll find anything of value in there.")
            slow_text("You move into the building.")
        else:
            slow_text("Please enter Yes or No.")


def check_items():
    """
    Function to check if the player has an key in their inventory
    """
    item_find = random.choice([True, False])
    if item_find is True:
        guardian.items.append("key")
        slow_text("You've found a key!")


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
        guardian.items.append(weapon)
        slow_text(f"You've found a {weapon}!")
    if weapon_find is False:
        slow_text("There was nothing in the chest, only dust...")


def main():
    """
    Introduction to the game to run first
    """

    slow_text("Welcome Guardian!")
    slow_text("This is a text adventure game based on the video game Destiny!\n")
    slow_text("You are a New Light - a person newly re-awoken by a small")
    slow_text("robot companion known as a Ghost.")
    slow_text("You are now a Guardian, chosen to wield the Light")
    slow_text("to defeat the Darkness.\n")

    slow_text("Let's get your adventure started!\n")
    slow_text("\n")

    get_name()
    get_subclass(get_class())
    opening_scene()


main()
