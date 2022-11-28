import sys
import os
import random
import time
import pyfiglet

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


class GameFunctions:
    """
    Class for all game functions
    """
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
        print("Yes or No?")
        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "Yes":
            GameFunctions.reset_console(self)
            new_story.introduction()
        elif user_input == "No":
            print("Thank you for playing, Guardian!")
            self.clear_worksheet()
            sys.exit()
        else:
            print("Please enter Yes or No.")

    def clear_worksheet(self):
        """
        Clear player spreadsheet at start of game
        """
        class_worksheet.delete_rows(2)
        stats_worksheet.delete_rows(2)

    def inital_luck(self):
        """Roll an Inital Luck number for the character"""
        character_luck = random.randint(0, 100)
        stats_worksheet.update_cell(2, 1, character_luck)
        return character_luck

    def check_items(self):
        """
        Function to check if the player has an key in their inventory
        """
        item_find = random.choice([True, False])
        if item_find is True:
            guardian.items.append("key")
            print("You've found a key!")

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
            class_worksheet.update_cell(2, 4, weapon)
            print(f"You've found a {weapon}!")
            return weapon

        elif weapon_find is False:
            print("There was nothing in the chest, only dust...")

    def handle_vandal(self):
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
                GameFunctions.play_again(self)

    def slow_text(self, text):
        """
        Slows the speed of the text being printed.
        https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
        """
        text += "\n"
        for char in text:
            time.sleep(0.09)
            print(char, end="", flush=True)


class Player:
    """
    Class for player inventory and weapon.
    """

    def __init__(self, items, health):
        self.items = items
        self.health = health


guardian = Player([], 100)


class RandomEncounter:
    """
    Class for NPC character and random encounter
    """

    def __init__(self, name):
        self.name = name

    def talk(self):
        """
        Text to print on random encounter trigger
        """
        print(f"A {self.name} emerges from the shadows.")
        print("He takes one lucky shot at you before he runs away.")


vandal = RandomEncounter("Vandal")


class Story:
    """
    Functions for the story and player choices
    """

    def introduction(self):
        """
        Introduction to the game to run first
        """

        text1 = pyfiglet.figlet_format("DESTINY", justify="center")
        text2 = pyfiglet.figlet_format("RPG GAME", justify="center")
        print(text1)
        print(text2)

        print("Welcome Guardian!")
        print("This is a text adventure game based on the video game"
              " Destiny!")
        print("\n ")
        print("You are a New Light - a person newly re-awoken by a small")
        print("robot companion known as a Ghost.")
        print("You are now a Guardian, chosen to wield the Light")
        print("to defeat the Darkness.\n")

        print("Let's get your adventure started!\n")
        print("\n")

        GameFunctions.clear_worksheet(self)
        GameFunctions.inital_luck(self)
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
        print("Let's try to figure out what kind of Guardian you are...\n")
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
                self.get_subclass(chosen_class)
            else:
                print("Please type one of the classes listed.")
                continue

    def get_subclass(self, chosen_class):
        """Players choose their subclass - each class has 3."""

        print("Each Lightbearer has a choice... \n")
        print("Your subclass defines your personality and skill.")
        print("You must choose now. Are you a... \n")

        if chosen_class == "Hunter":
            subclasses = ['Nightstalker', 'Blade Dancer', 'Gunslinger']

        elif chosen_class == "Warlock":
            subclasses = ['Voidwalker', 'Sunsinger', 'Stormcaller']

        elif chosen_class == "Titan":
            subclasses = ['Striker', 'Defender', 'Sunbreaker']

        for index, subclass in enumerate(subclasses, 1):
            print(index, subclass)

        choice = int(input(f"Make your choice, {chosen_class} \n> "))
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
            print("You run towards the cliff and jump! This is all "
                  "too much to take. [END]")
            GameFunctions.clear_worksheet(self)
            sys.exit()
        else:
            print("Please enter a valid option.")

    def search_cars(self):
        """
        Function to search the cars
        """
        print("You decide to search through some of the abandoned cars.")
        GameFunctions.check_items(self)

        if guardian.items == ["key"]:
            print("You put your key away and walk towards the building.")
        else:
            print("But you didn't find anything")

        self.building_entrance()

    def building_entrance(self):
        """
        Function to enter the building and try to open a chest
        """

        print("The building is long abandoned, rust covers the doors.")
        print("All the windows are broken.")
        print("In front of you, you see a chest...\n")
        print("Try to open the chest?")
        print("Yes or No")

        while True:
            action = input("\n> ")
            if action == "yes" and guardian.items == ["key"]:
                guardian.items.remove("key")
                print("You've used your key!")
                GameFunctions.check_weapon(self)
                self.building_hallway()
            elif action == "yes" and guardian.items == []:
                print("You don't have a key and the lock won't budge.")
                print("You decide to move on.\n")
                self.building_hallway()
            elif action == "no":
                print("The chest looks old and worn...\n")
                print("You don't think you'll find anything of value "
                      "in it.\nYou move into the building.")
                self.building_hallway()
            else:
                print("Please enter Yes or No.")

    def building_hallway(self):
        """
        Function to play scene on entering the building hallway,
        call fight scene or end
        """
        print("\n")
        print("You enter into a long hallway inside the building.")
        print("Ahead you can see 2 open doorways.")
        print("You can enter one of "
              "them or continue down the hallway.")
        print("What do you want to do?")
        print("1. Enter door 1?\n"
              "2. Enter door 2?\n"
              "3. Continue down the hallway?")

        user_input = ""

        user_input = input("\n> ")
        if user_input == "1":
            print("You enter door 1. It's a small room with a Fallen Dreg"
                  " inside!")
            self.dreg_fight()
        if user_input == "2":
            print("You decide to enter the 2nd door. It's a small room.")
            self.empty_room()
        if user_input == "3":

            self.spaceship_room()
        else:
            print("Please enter a valid option.")

    def empty_room(self):
        """
        Empty room, player must turn around and choose another option
        from building_hallway
        """
        GameFunctions.handle_vandal(self)

        print("You look around the room.\n"
              "It seems completely empty, just dust.\n"
              "You turn around and decide to pick a different option")

        print("You return to the hallway. Do you want to go to")
        print("1. Door 1? or 2. Continue down the hall?")

        user_input = ""

        user_input = input("\n> ")
        if user_input == "1":
            print("You enter door 1. It's a small room with a Fallen Dreg"
                  " inside!")
            self.dreg_fight()
        if user_input == "2":
            self.spaceship_room()
        else:
            print("Please enter a valid option.")

    def dreg_fight(self):
        """
        fight scene function, checks for weapon from random roll
        or else use abilities
        """
        player_class = class_worksheet.cell(2, 1).value
        player_subclass = class_worksheet.cell(2, 2).value
        player_ability = class_worksheet.cell(2, 3).value
        stored_weapon = class_worksheet.cell(2, 4).value

        # Health system from Elijah Henderson
        # https://www.youtube.com/watch?v=n17Hkgi8rt4
        guardian.health -= random.randint(1, 100)
        print("Before you can make a move, the Dreg takes one shot with "
              "his weapon.\nIt hits you on the arm!"
              )
        print(f"\nHealth: {guardian.health}")
        if guardian.health < 0:
            print("You are dead!")
            print("Would you like to play again?")
            GameFunctions.play_again(self)

        if stored_weapon is not None:
            print("\n")
            print("Now it's your turn!")
            print(f"You pull out your {stored_weapon}")
            print("line up on the Dreg's head...")
            print("and pull the trigger.")
            print("Nice work!")
            self.hallway_choice()
        else:
            print("\n")
            print("Now it's your turn!")
            print("You don't have a gun... but you do have your abilities.\n")
            print(f"You're a {player_class}. A {player_subclass}.")
            print(f"You can use your {player_ability}")
            print("You throw it and it sticks to the Dreg")
            print("and explodes in a burst of Light!\n")
            print("Nice work! The Dreg is dust.")
            self.hallway_choice()

    def hallway_choice(self):
        """
        User chooses between 2 paths
        """
        GameFunctions.handle_vandal(self)

        print("\n ")
        print("Ahead, you see 2 corridors.")
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
            GameFunctions.clear_worksheet(self)
            sys.exit()
        else:
            print("Please enter either left or right.")

    def spaceship_room(self):
        """
        Spaceship room choice function
        """
        print("Ahead of you, you see a giant open room ahead "
              "with a spaceship in it!")
        print("You can see straight away that the ship")
        print("is missing it's engine.\n")
        print("As soon as you take a step back, you hear a sound.")
        print("A rumbling from the walls...")
        print("The roof cracks open and you see a Fallen Captain emerge!")
        print("He's carrying the engine!")
        print("If you want it, you'll have to take it from him.")
        print("\n ")
        print("Fight or Run?")
        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "Fight":
            if GameFunctions.inital_luck(self) > 50:
                print("You feel the Light course through you!")
                print("You use your ultimate ability - your Super.\n")
                print("You wield the Light, you aim at the Captain")
                print("and hit him with the full force of your Super.")
                print("He staggers... and falls dead.")
                print("\n ")
                print("You grab the engine and Ghost installs it.")
                print("The ship rumbles to life and takes off.")
                print("Next destination - The Tower... Home.")
                print("[END]")
                print("\n ")
                print("Well done Guardian! You win!")
                print("Would you like to play again?")
                GameFunctions.play_again(self)

            elif GameFunctions.inital_luck(self) < 50:
                print("You feel the Light course through you!")
                print("You use your ultimate ability - your Super.")
                print("You wield the Light, you aim at the Captain")
                print("But you miss!")
                print("The Captain turns to you and aims his gun.")
                print("He hits you directly and you fall down... dead.")
                print("[END]")
                print("Your Ghost can resurrect you. Do you want him to?")
                GameFunctions.play_again(self)

        elif user_input == "Run":
            print("This Captain is giant!")
            print("No way you want to take him on. You turn and run.")
            print("But behind you is an army of Dregs.")
            print("Within seconds you're swarmed...")
            print("And your Light fades.")
            print("[END]")
            print("\n ")
            print("Thanks for playing, Guardian!")
            print("Would you like to play again?")
            GameFunctions.play_again(self)
        else:
            print("Please enter either fight or run.")

    def luck_escape(self):
        """
        Function to check whether the player escapes from the ambush
        """
        if GameFunctions.inital_luck(self) > 50:
            print("\n ")
            print("You manage to hide behind some nearby crates")
            print("before the giant fallen Servitor sees you.")
            print("You wait for his eye to close before you turn and run")
            print("the down the hallway on the right!")
            print("Phew!\n")
            self.spaceship_room()
        else:
            print("\n ")
            print("Oh no, a Fallen Servitor!")
            print("You have no time to move before his giant Eye")
            print("turns it's gaze on you.")
            print("Within seconds, his blast hits you directly!")
            print("You drop to the floor. Dead.")
            print("[END]")
            print("\n ")
            print("Thanks for playing, Guardian!")
            print("Would you like to play again?")
            GameFunctions.play_again(self)


new_story = Story()

new_story.introduction()
