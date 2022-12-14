import sys
import os
import random
import time
import pyfiglet

import gspread
from google.oauth2.service_account import Credentials

import story_text as story

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


# This Class contains functions that will run throughout the game
class GameFunctions:
    """
    Class for all game functions
    """

    def s_print(self, text):
        """
        Slows the speed of the text being printed.
        https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
        """
        text += "\n"
        for char in text:
            time.sleep(0.03)
            print(char, end="", flush=True)

    def reset_console(self):
        """
        Reset the console for a new game or continue.
        """
        print("\n")
        os.system('cls||clear')

    def play_again(self):
        """
        Option to allow player to play again or exit
        """
        GameFunctions.s_print(self, "Yes or No?")

        while True:
            user_input = input("\n> ").capitalize()
            if user_input == "Yes":
                GameFunctions.reset_console(self)
                guardian.health = 100
                stats_worksheet.update_cell(2, 4, "")
                GameFunctions.s_print(self, "Your ghost ressurects you in"
                                      " a safe place...")
                new_story.opening_scene()
            elif user_input == "No":
                self.s_print("Thank you for playing, Guardian!")
                self.clear_worksheet()
                sys.exit()
            else:
                print("Please enter Yes or No.")
                continue

    def clear_worksheet(self):
        """
        Clear player spreadsheet at start of game
        """
        stats_worksheet.delete_rows(2)

    def inital_luck(self):
        """Roll an Inital Luck number for the character"""
        character_luck = random.randint(0, 100)
        stats_worksheet.update_cell(2, 5, character_luck)
        return character_luck

    def check_items(self):
        """
        Function to check if the player has an key in their inventory
        """
        item_find = random.choice([True, False])
        if item_find is True:
            guardian.items.append("key")
            self.s_print("You've found a key!")

    def open_chest(self):
        """
        Function to open the chest
        """

        while True:
            action = input("\n> ").capitalize()
            if action == "Yes" and guardian.items == ["key"]:
                guardian.items.remove("key")
                GameFunctions.s_print(self, "You've used your key!")
                GameFunctions.check_weapon(self)
                Story.building_hallway(self)
            elif action == "Yes" and guardian.items == []:
                GameFunctions.s_print(
                    self, "You don't have a key and the lock"
                    " won't budge. You decide to move on.\n")
                Story.building_hallway(self)
            elif action == "No":
                GameFunctions.s_print(self, "The chest looks old and worn...")
                GameFunctions.s_print(self, "You don't think you'll find"
                                      " anything of value in it.\n"
                                      "You move into the building.")
                Story.building_hallway(self)
            else:
                print("Please enter Yes or No.")
                continue

    def check_weapon(self):
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
            GameFunctions.s_print(self, f"You've found a {weapon}!")
            # if player finds a weapon, update their luck
            if stats_worksheet.cell(2, 5).value < "50":
                character_luck = random.randint(50, 100)
                stats_worksheet.update_cell(2, 5, character_luck)
                return weapon

        else:
            GameFunctions.s_print(self, "There was nothing in the chest,"
                                  " only dust...")
            Story.building_hallway(self)

    def handle_vandal(self):
        """
        function for random Vandal encounter
        """
        vandal_attack = random.choice([True, False])
        if vandal_attack is True:
            self.s_print("Out of nowhere, a Fallen Vandal attacks you!")
            self.s_print("You took some damage :(")
            guardian.health -= random.randint(1, 50)
            print(f"\nHealth: {guardian.health}")
            if guardian.health < 0:
                self.s_print("You are dead!")
                self.s_print(
                    "Your Ghost can resurrect you. Do you want him to?")
                GameFunctions.play_again(self)


function = GameFunctions()


# This Class contains the player health and inventory system
class Player:
    """
    Class for player inventory and weapon.
    """

    def __init__(self, items, health):
        self.items = items
        self.health = health


guardian = Player([], 100)


# This Class contains the story of the game, printed to the terminal
class Story:
    """
    Functions for the story and player choices
    """

    def introduction(self):
        """
        Introduction to the game - runs the logo, clears the worksheet,
        asks the player to press Enter to start
        """

        text1 = pyfiglet.figlet_format("DESTINY", justify="center")
        text2 = pyfiglet.figlet_format("RPG GAME", justify="center")
        print(text1)
        print(text2)

        function.s_print(story.INTRODUCTION_TEXT)
        function.clear_worksheet()
        function.inital_luck()

        while True:
            start = input("Press the ENTER key to begin!\n")
            if start == "":
                function.reset_console()
                self.get_name()
            else:
                print(f"You typed '{start}'. When you're ready to"
                      " begin. press ENTER.")
                continue

    def get_name(self):
        """
        Get the name of the player.
        """
        function.s_print(story.CHOOSE_NAME_TEXT)

        while True:
            name = input("\n> ").capitalize()
            # https://www.w3schools.com/python/ref_string_isalpha.asp
            if not name.isalpha():
                print("Please enter letters only.")
            elif len(name.strip(" ")) < 3 or len(name.strip(" ")) > 8:
                print("Please enter a name between 3 and 8 letters long.")
            else:
                function.s_print(f"It's nice to meet you, {name}."
                                 " I'm your Ghost.")
                self.get_class()
        return name

    def get_class(self):
        """
        Player chooses their class. 3 available based on Destiny lore.
        """
        function.s_print(story.CHOOSE_CLASS_TEXT)

        while True:
            chosen_class = input("My class is: \n> ").capitalize()
            classes = ["Hunter", "Warlock", "Titan"]
            if chosen_class in classes:
                function.s_print(f"Welcome, {chosen_class}.")
                stats_worksheet.update_cell(2, 1, chosen_class)
                self.get_subclass(chosen_class)
            else:
                print("Please type either Hunter, Warlock or Titan.")
                continue

    def get_subclass(self, chosen_class):
        """
        Players choose their subclass - each class has 3.
        """
        function.s_print(story.CHOOSE_SUBCLASS_TEXT)

        if chosen_class == "Hunter":
            subclasses = ['Nightstalker', 'Blade Dancer', 'Gunslinger']

        elif chosen_class == "Warlock":
            subclasses = ['Voidwalker', 'Sunsinger', 'Stormcaller']

        elif chosen_class == "Titan":
            subclasses = ['Striker', 'Defender', 'Sunbreaker']

        for index, subclass in enumerate(subclasses, 1):
            print(index, subclass)

        while True:

            try:
                choice = int(input(f"\nMake your choice, {chosen_class}."
                                   "\n1, 2 or 3?\n>"))
                if choice < 1 or choice > 3 or choice == str():
                    raise ValueError
            except ValueError:
                print("Please enter number 1, 2 or 3.")
            else:
                function.s_print(f"A {subclasses[choice-1]}?")
                function.s_print("The Darkness doesn't stand a chance. \n")
                chosen_subclass = subclasses[choice-1]
                stats_worksheet.update_cell(2, 2, chosen_subclass)
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

        stats_worksheet.update_cell(2, 3, ability)
        return ability

    def opening_scene(self):
        """
        First scene to play after choosing a name and class
        """
        function.s_print(story.FIRST_SCENE_TEXT)

        while True:
            user_input = input("\n> ")
            if user_input == "1":
                self.search_cars()
            elif user_input == "2":
                self.building_entrance()
            elif user_input == "3":
                function.s_print("You run towards the cliff and jump!"
                                 " This is all too much to take.[END]"
                                 )

                function.s_print("\nThanks for playing, Guardian!")
                function.clear_worksheet()
                sys.exit()
            else:
                print("Please choose number 1, 2 or 3.")
                continue

    def search_cars(self):
        """
        Function to search the cars
        """
        function.s_print("You decide to search through some of the abandoned"
                         " cars.")
        function.check_items()

        if guardian.items == ["key"]:
            function.s_print("You put your key away and walk towards the"
                             " building.")
        else:
            function.s_print("But you didn't find anything")

        self.building_entrance()

    def building_entrance(self):
        """
        Enter the building and try to open a chest
        """
        function.s_print(story.ENTRANCE_TEXT)
        GameFunctions.open_chest(self)

    def building_hallway(self):
        """
        Function to play scene on entering the building hallway -
        players choose a room
        """
        function.s_print(story.HALLWAY_TEXT)

        while True:
            user_input = input("\n> ")
            if user_input == "1":
                function.s_print("You enter door 1. It's a small"
                                 " room with a Fallen Dreg inside!")
                self.dreg_fight()
            if user_input == "2":
                function.s_print("You decide to enter the 2nd door."
                                 " It's a small room.")
                self.empty_room()
            if user_input == "3":
                self.spaceship_room()
            else:
                print("Please choose number 1, 2 or 3.")
                continue

    def empty_room(self):
        """
        Empty room, player must turn around and choose another option
        from building_hallway
        """
        function.handle_vandal()
        function.s_print(story.EMPTY_ROOM_TEXT)

        while True:
            user_input = input("\n> ")
            if user_input == "1":
                function.s_print("You enter door 1. It's a small"
                                 " room with a Fallen Dreg inside!")
                self.dreg_fight()
            if user_input == "2":
                self.spaceship_room()
            else:
                print("Please choose number 1 or 2.")
                continue

    def dreg_fight(self):
        """
        Fight scene function, checks for weapon from random roll
        or else use abilities
        """
        player_class = stats_worksheet.cell(2, 1).value
        player_subclass = stats_worksheet.cell(2, 2).value
        player_ability = stats_worksheet.cell(2, 3).value
        stored_weapon = stats_worksheet.cell(2, 4).value

        # Health system from Elijah Henderson
        # https://www.youtube.com/watch?v=n17Hkgi8rt4
        guardian.health -= random.randint(1, 100)
        function.s_print("Before you can make a move, the Dreg"
                         " takes one shot with his weapon."
                         "\nIt hits you on the arm!"
                         )

        print(f"\nHealth: {guardian.health}")
        if guardian.health <= 0:
            function.s_print("You are dead!")
            function.s_print("Would you like to play again?")
            function.play_again()

        if stored_weapon is not None:
            function.s_print("\nNow it's your turn!")
            function.s_print(f"You pull out your {stored_weapon}.")
            function.s_print("Line up on the Dreg's head...")
            function.s_print("and pull the trigger. Nice work!")
            self.hallway_choice()
        else:
            abilites_text = (f"You're a {player_class}. A {player_subclass}."
                             f" You can use your {player_ability}.")

            function.s_print("\nNow it's your turn!")
            function.s_print("You don't have a gun... but you do have"
                             " your abilities.\n")
            function.s_print(abilites_text)
            function.s_print(story.DREG_FIGHT_WEAPON_TEXT)
            self.hallway_choice()

    def hallway_choice(self):
        """
        User chooses between 2 paths
        """
        function.handle_vandal()

        function.s_print("\nAhead, you see 2 corridors.")
        function.s_print("Do you want to go left, right or back?")

        while True:
            user_input = input("\n> ").capitalize()
            if user_input == "Left":
                self.spaceship_room()
            elif user_input == "Right":
                function.s_print(
                    "You go right. It's very hard to see.")
                function.s_print("In the darkness, you can make out"
                                 " something large with a glowing"
                                 " purple eye.")
                self.luck_escape()
            elif user_input == "Back":
                function.s_print("'I'm done fighting these Dregs,"
                                 " I'm out of here!'[END]\n"
                                 "Thanks for playing Guardian!\n"
                                 "Would you like to play again?")
                GameFunctions.play_again(self)
            else:
                print("Please enter either left, right or back.")
                continue

    def spaceship_room(self):
        """
        Final fight scene, ending depends on the players Luck score
        """
        function.s_print(story.SPACESHIP_ROOM_TEXT)

        while True:
            luck = stats_worksheet.cell(2, 5).value

            user_input = input("\n> ").capitalize()
            if user_input == "Fight":
                if luck >= "50":
                    function.s_print(story.CAPTAIN_FIGHT_WIN_TEXT)
                    function.play_again()

                elif luck <= "49":
                    function.s_print(story.CAPTAIN_FIGHT_LOSE_TEXT)
                    function.play_again()

            elif user_input == "Run":
                function.s_print(story.CAPTAIN_FIGHT_RUN)
                function.play_again()
            else:
                print("Please enter either Fight or Run.")
                continue

    def luck_escape(self):
        """
        Function to check whether the player escapes from the ambush
        """
        if function.inital_luck() > 50:
            function.s_print(story.LUCK_ROLL_WIN)
            self.spaceship_room()
        else:
            function.s_print(story.LUCK_ROLL_LOSE)
            function.play_again()


# Run the game
new_story = Story()
new_story.introduction()
