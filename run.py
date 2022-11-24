import sys
import random
# import time

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Destiny_RPG')

class_worksheet = SHEET.worksheet('PlayerClass')
stats_worksheet = SHEET.worksheet('PlayerStats')

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

    def __init__(self, items, health):
        self.items = items
        self.health = health

    def weapons(self, worksheet_weapon):
        """
        Connect to weapon cell in spreadsheet
        """
        worksheet_weapon = class_worksheet.cell(2, 4).value
        return worksheet_weapon


guardian = Player([], 100)
stored_weapon = class_worksheet.cell(2, 4).value
player_class = class_worksheet.cell(2, 1).value
player_subclass = class_worksheet.cell(2, 2).value
player_ability = class_worksheet.cell(2, 3).value


class Story:
    """
    Functions for the story and player choices
    """

    def introduction(self):
        """
        Introduction to the game to run first
        """

        print("Welcome Guardian!")
        print("This is a text adventure game based on the video game Destiny!")
        print("\n ")
        print("You are a New Light - a person newly re-awoken by a small")
        print("robot companion known as a Ghost.")
        print("You are now a Guardian, chosen to wield the Light")
        print("to defeat the Darkness.\n")

        print("Let's get your adventure started!\n")
        print("\n")

        clear_worksheet()
        inital_luck()
        self.get_name()

    def get_name(self):
        """
        Get the name of the player.
        """
        print("- - - - - - -")
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
                self.get_class()
        return name

    def get_class(self):
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
                class_worksheet.update_cell(2, 1, chosen_class)
                self.get_subclass()
            else:
                print("Please type one of the classes listed.")
                continue

    def get_subclass(self):
        """Players choose their subclass - each class has 3."""

        print("Each Lightbearer has a choice... \n")
        print("Your subclass defines your personality and skill.")
        print("You must choose now. Are you a... \n")

        if player_class == "Hunter":
            subclasses = ['Nightstalker', 'Blade Dancer', 'Gunslinger']

        elif player_class == "Warlock":
            subclasses = ['Voidwalker', 'Sunsinger', 'Stormcaller']

        elif player_class == "Titan":
            subclasses = ['Striker', 'Defender', 'Sunbreaker']

        for index, subclass in enumerate(subclasses, 1):
            print(index, subclass)

        choice = int(input(f"Make your choice, {player_class} \n> "))
        print(f"A {subclasses[choice-1]}?")
        print("The darkness doesn't stand a chance \n")

        chosen_subclass = subclasses[choice-1]
        class_worksheet.update_cell(2, 2, chosen_subclass)
        self.player_abilites(chosen_subclass)
        self.opening_scene()

    def player_abilites(self, chosen_subclass):
        """
        Gives the player an ability, based on their choice of subclass
        """

        if chosen_subclass in ('Nightstalker', 'Voidwalker', 'Defender'):
            ability = 'Vortex Grenade'

        elif chosen_subclass in ("Blade Dancer", "Stormcaller", "Striker"):
            ability = 'Lightning Grenade'

        elif chosen_subclass in ("Gunslinger", "Sunsinger", "Sunbreaker"):
            ability = 'Solar Grenade'

        class_worksheet.update_cell(2, 3, ability)
        return ability

    def opening_scene(self):
        """
        First scene to play after choosing a name and class
        """

        print("You look around and notice you're in a familiar place...")
        print("This is the Cosmodrome. The last thing you remember is")
        print("fighting here in a war against The Fallen.")
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
            self.search_cars()
        elif user_input == "2":
            self.building_entrance()
        elif user_input == "3":
            print("You run towards the cliff and jump! This is all too much")
            print("to take. [END]")
            clear_worksheet()
            sys.exit()
        else:
            print("Please enter a valid option.")

    def search_cars(self):
        """
        Function to search the cars
        """
        print("You decide to search through some of the abandoned cars.")
        check_items()

        if guardian.items == ["key"]:
            print("You put your key away and walk towards the building.")
        else:
            print("But you didn't find anything")

        self.building_entrance()

    def building_entrance(self):
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
                self.building_hallway()
            elif action == "yes" and guardian.items == []:
                print("You don't have a key and the lock won't budge.")
                print("You decide to move on")
                self.building_hallway()
            elif action == "no":
                print("The chest looks old and worn...")
                print("You don't think you'll find anything of value in it.")
                print("You move into the building.")
                self.building_hallway()
            else:
                print("Please enter Yes or No.")

    def building_hallway(self):
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
            self.dreg_fight()
        elif user_input == "Run":
            print("You've alerady died once fighting Dregs")
            print("You're not doing it again.")
            print("You flee and run back to the cliff...")
            print("And jump!")
            print("[END]")
            clear_worksheet()
            sys.exit()
        else:
            print("Please enter a valid option.")

    def dreg_fight(self):
        """
        fight scene function, checks for weapon from random roll
        or else use abilities
        """
        if stored_weapon is not None:
            print(f"You pull out your {stored_weapon}")
            print("line up on the Dreg's head...")
            print("and pull the trigger.")
            print("Nice work!")
            self.hallway_choice()
        else:
            print("You don't have a gun... but you do have your abilities")
            print(f"You're a {player_class}. A {player_subclass}.")
            print(f"You can use your {player_ability}")
            print("You throw it and it sticks to the Dreg")
            print("and explodes in a burst of Light!")
            print("Nice work! The Dreg is dust.")
            self.hallway_choice()

    def hallway_choice(self):
        """
        User chooses between 2 paths"""
        print("\n ")
        print("Ahead, you see 2 corridors")
        print("Do you want to go left, right or back?")

        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "Left":
            print("You go left and ahead of you see a giant room")
            print("with a spaceship. You check it out.")
            self.spaceship_room()
        elif user_input == "Right":
            print("You go right. It's very hard to see.")
            print("In the darkness, you can make out something large...")
            print("with a glowing purple eye!")
            self.luck_escape()
        elif user_input == "Back":
            print("'I'm done fighting these Dregs, I'm out of here!'[END]")
            clear_worksheet()
            sys.exit()
        else:
            print("Please enter either left or right.")

    def spaceship_room(self):
        """
        Spaceship room choice function
        """
        print("You can see straight away that the ship")
        print("is missing it's engine.")
        print("As soon as you take a step back, you hear a sound.")
        print("A rumbling from the walls...")
        print("The roof cracks open and you see a Fallen Captain emerge!")
        print("He's carrying the engine!")
        print("If you want it, you'll have to take it from him.")
        print("\n ")
        print("1. Fight or 2. Run?")
        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "1":
            if inital_luck() > 50:
                print("You feel the Light course through you!")
                print("You use your ultimate ability - your Super.")
                print("You wield the Light, you aim and the Captain")
                print("and hit him with the full force of your Super.")
                print("He staggers... and falls. Dead.")
                print("\n ")
                print("You grab the engine and Ghost installs it.")
                print("The ship rumbles to life and takes off.")
                print("Next destination - The Tower... home.")
                print("END")

            elif inital_luck() < 50:
                print("You feel the Light course through you!")
                print("You use your ultimate ability - your Super.")
                print("You wield the Light, you aim and the Captain")
                print("But you miss!")
                print("The Captain turns to you and aims his gun.")
                print("He hits you directly and you fall down... dead.")
                print("Your Ghost can ressurect you. Do you want him to?")
                print("Yes or No?")
                user_input = ""
                user_input = input("\n> ").capitalize()
                if user_input == "Yes":
                    new_story.introduction()
                elif user_input == "No":
                    print("Thank you for playing, Guardian!")
                    clear_worksheet()
                    sys.exit()
                else:
                    print("Please enter Yes or No.")

        elif user_input == "2":
            print("This Captain is giant!")
            print("No way you want to take him on. You turn and run.")
            print("But behind you is an army of Dregs.")
            print("Within seconds you're swarmed...")
            print("And your Light fades.")
            print("[END]")
            print("\n ")
            print("Thanks for playing, Guardian!")
            clear_worksheet()
            sys.exit()
        else:
            print("Please enter either fight or run.")

    def luck_escape(self):
        """
        Function to check whether the player escapes from the ambush
        """
        if inital_luck() > 50:
            print("You manage to hide behind some nearby crates")
            print("before the giant fallen Servitar sees you.")
            print("You wait for his eye to close before you turn and run")
            print("the down the hallway on the right!")
            print("Phew!")
            self.spaceship_room()
        else:
            print("Oh no, a Fallen Servitar!")
            print("You have no time to move before his giant Eye")
            print("turns it's gaze on you.")
            print("Within seconds, his blast hits you directly!")
            print("You drop to the floor. Dead.")
            print("END")
            print("\n ")
            print("Thanks for playing, Guardian!")
            clear_worksheet()
            sys.exit()


def clear_worksheet():
    """
    Clear player spreadsheet at start of game
    """
    class_worksheet.delete_rows(2)
    stats_worksheet.delete_rows(2)


def inital_luck():
    """Roll an Inital Luck number for the character"""
    character_luck = random.randint(0, 100)
    stats_worksheet.update_cell(2, 1, character_luck)
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
        class_worksheet.update_cell(2, 4, weapon)
        print(f"You've found a {weapon}!")
        return weapon

    elif weapon_find is False:
        print("There was nothing in the chest, only dust...")


new_story = Story()

new_story.introduction()
