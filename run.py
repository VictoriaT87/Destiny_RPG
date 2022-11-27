import sys
import random
import time

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
        slow_text(f"A {self.name} emerges from the shadows.")
        slow_text("He takes one lucky shot at you before he runs away.")


vandal = RandomEncounter("Vandal")


class Story:
    """
    Functions for the story and player choices
    """

    def introduction(self):
        """
        Introduction to the game to run first
        """

        slow_text("Welcome Guardian!")
        slow_text("This is a text adventure game based on the video game Destiny!")
        slow_text("\n ")
        slow_text("You are a New Light - a person newly re-awoken by a small")
        slow_text("robot companion known as a Ghost.")
        slow_text("You are now a Guardian, chosen to wield the Light")
        slow_text("to defeat the Darkness.\n")

        slow_text("Let's get your adventure started!\n")
        slow_text("\n")

        clear_worksheet()
        inital_luck()
        self.get_name()

    def get_name(self):
        """
        Get the name of the player.
        """
        slow_text("- - - - - - -")
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
                self.get_class()
        return name

    def get_class(self):
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
                class_worksheet.update_cell(2, 1, chosen_class)
                self.get_subclass(chosen_class)
            else:
                slow_text("Please type one of the classes listed.")
                continue

    def get_subclass(self, chosen_class):
        """Players choose their subclass - each class has 3."""

        slow_text("Each Lightbearer has a choice... \n")
        slow_text("Your subclass defines your personality and skill.")
        slow_text("You must choose now. Are you a... \n")

        if chosen_class == "Hunter":
            subclasses = ['Nightstalker', 'Blade Dancer', 'Gunslinger']

        elif chosen_class == "Warlock":
            subclasses = ['Voidwalker', 'Sunsinger', 'Stormcaller']

        elif chosen_class == "Titan":
            subclasses = ['Striker', 'Defender', 'Sunbreaker']

        for index, subclass in enumerate(subclasses, 1):
            print(index, subclass)

        choice = int(input(f"Make your choice, {chosen_class} \n> "))
        slow_text(f"A {subclasses[choice-1]}?")
        slow_text("The darkness doesn't stand a chance \n")

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

        slow_text("You look around and notice you're in a familiar place...")
        slow_text("This is the Cosmodrome. The last thing you remember is")
        slow_text("fighting here in a war against The Fallen.")
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
            self.search_cars()
        elif user_input == "2":
            self.building_entrance()
        elif user_input == "3":
            slow_text("You run towards the cliff and jump! This is all too much")
            slow_text("to take. [END]")
            clear_worksheet()
            sys.exit()
        else:
            slow_text("Please enter a valid option.")

    def search_cars(self):
        """
        Function to search the cars
        """
        slow_text("You decide to search through some of the abandoned cars.")
        check_items()

        if guardian.items == ["key"]:
            slow_text("You put your key away and walk towards the building.")
        else:
            slow_text("But you didn't find anything")

        self.building_entrance()

    def building_entrance(self):
        """
        Function to enter the building and try to open a chest
        """

        slow_text("The building is long abandoned, rust covers the doors.")
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
                self.building_hallway()
            elif action == "yes" and guardian.items == []:
                slow_text("You don't have a key and the lock won't budge.")
                slow_text("You decide to move on")
                self.building_hallway()
            elif action == "no":
                slow_text("The chest looks old and worn...")
                slow_text("You don't think you'll find anything of value in it.")
                slow_text("You move into the building.")
                self.building_hallway()
            else:
                slow_text("Please enter Yes or No.")

    def building_hallway(self):
        """
        Function to play scene on entering the building hallway,
        call fight scene or end
        """
        handle_vandal()

        slow_text("You enter into a long hallway inside the building.")
        slow_text("Ahead you can see 2 open doorways. You can enter one of"
                  " them or continue down the hallway.")
        slow_text("What do you want to do?")
        slow_text("1. Enter door 1?\n"
                  "2. Enter door 2?\n"
                  "3. Continue down the hallway?")

        user_input = ""

        user_input = input("\n> ")
        if user_input == "1":
            slow_text("You enter door 1. It's a small room with a Fallen Dreg"
                      " inside!")
            self.dreg_fight()
        if user_input == "2":
            slow_text("You decide to enter the 2nd door. It's a small room.")
            self.empty_room()
        if user_input == "3":
            slow_text("You continue until you see a giant open room ahead"
                      "with a spaceship in it!")
            self.spaceship_room()
        else:
            slow_text("Please enter a valid option.")

    def empty_room(self):
        """
        Empty room, player must turn around and choose another option
        from building_hallway
        """
        handle_vandal()

        slow_text("You look around the room.\n"
                  "It seems completely empty, just dust.\n"
                  "You turn around and decide to pick a different option")

        slow_text("You return to the hallway. Do you want to go to 1. Door 1?"
                  "or 2. Continue down the hall?")

        user_input = ""

        user_input = input("\n> ")
        if user_input == "1":
            slow_text("You enter door 1. It's a small room with a Fallen Dreg"
                      " inside!")
            self.dreg_fight()
        if user_input == "2":
            slow_text("You continue until you see a giant open room ahead"
                      "with a spaceship in it!")
            self.spaceship_room()
        else:
            slow_text("Please enter a valid option.")

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
        slow_text("Before you can make a move, the Dreg takes one shot with his\n"
                  "weapon. It hits you on the arm!"
                  )
        slow_text(f"\nHealth: {guardian.health}")
        if guardian.health < 0:
            slow_text("You are dead!")
            slow_text("Would you like to play again?")
            play_again()

        if stored_weapon is not None:
            slow_text("Now it's your turn!")
            slow_text(f"You pull out your {stored_weapon}")
            slow_text("line up on the Dreg's head...")
            slow_text("and pull the trigger.")
            slow_text("Nice work!")
            self.hallway_choice()
        else:
            slow_text("Now it's your turn!")
            slow_text("You don't have a gun... but you do have your abilities")
            slow_text(f"You're a {player_class}. A {player_subclass}.")
            slow_text(f"You can use your {player_ability}")
            slow_text("You throw it and it sticks to the Dreg")
            slow_text("and explodes in a burst of Light!")
            slow_text("Nice work! The Dreg is dust.")
            self.hallway_choice()

    def hallway_choice(self):
        """
        User chooses between 2 paths
        """
        handle_vandal()

        slow_text("\n ")
        slow_text("Ahead, you see 2 corridors")
        slow_text("Do you want to go left, right or back?")

        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "Left":
            slow_text("You go left and ahead of you see a giant room")
            slow_text("with a spaceship. You check it out.")
            self.spaceship_room()
        elif user_input == "Right":
            slow_text("You go right. It's very hard to see.")
            slow_text("In the darkness, you can make out something large...")
            slow_text("with a glowing purple eye!")
            self.luck_escape()
        elif user_input == "Back":
            slow_text("'I'm done fighting these Dregs, I'm out of here!'[END]")
            clear_worksheet()
            sys.exit()
        else:
            slow_text("Please enter either left or right.")

    def spaceship_room(self):
        """
        Spaceship room choice function
        """
        slow_text("You can see straight away that the ship")
        slow_text("is missing it's engine.")
        slow_text("As soon as you take a step back, you hear a sound.")
        slow_text("A rumbling from the walls...")
        slow_text("The roof cracks open and you see a Fallen Captain emerge!")
        slow_text("He's carrying the engine!")
        slow_text("If you want it, you'll have to take it from him.")
        slow_text("\n ")
        slow_text("1. Fight or 2. Run?")
        user_input = ""
        user_input = input("\n> ").capitalize()
        if user_input == "1":
            if inital_luck() > 50:
                slow_text("You feel the Light course through you!")
                slow_text("You use your ultimate ability - your Super.")
                slow_text("You wield the Light, you aim and the Captain")
                slow_text("and hit him with the full force of your Super.")
                slow_text("He staggers... and falls. Dead.")
                slow_text("\n ")
                slow_text("You grab the engine and Ghost installs it.")
                slow_text("The ship rumbles to life and takes off.")
                slow_text("Next destination - The Tower... home.")
                slow_text("END")
                slow_text("\n ")
                slow_text("Well done Guardian! You win!")
                slow_text("Would you like to play again?")
                play_again()

            elif inital_luck() < 50:
                slow_text("You feel the Light course through you!")
                slow_text("You use your ultimate ability - your Super.")
                slow_text("You wield the Light, you aim and the Captain")
                slow_text("But you miss!")
                slow_text("The Captain turns to you and aims his gun.")
                slow_text("He hits you directly and you fall down... dead.")
                slow_text("Your Ghost can ressurect you. Do you want him to?")
                play_again()

        elif user_input == "2":
            slow_text("This Captain is giant!")
            slow_text("No way you want to take him on. You turn and run.")
            slow_text("But behind you is an army of Dregs.")
            slow_text("Within seconds you're swarmed...")
            slow_text("And your Light fades.")
            slow_text("[END]")
            slow_text("\n ")
            slow_text("Thanks for playing, Guardian!")
            slow_text("Would you like to play again?")
            play_again()
        else:
            slow_text("Please enter either fight or run.")

    def luck_escape(self):
        """
        Function to check whether the player escapes from the ambush
        """
        if inital_luck() > 50:
            slow_text("\n ")
            slow_text("You manage to hide behind some nearby crates")
            slow_text("before the giant fallen Servitor sees you.")
            slow_text("You wait for his eye to close before you turn and run")
            slow_text("the down the hallway on the right!")
            slow_text("Phew!")
            self.spaceship_room()
        else:
            slow_text("\n ")
            slow_text("Oh no, a Fallen Servitor!")
            slow_text("You have no time to move before his giant Eye")
            slow_text("turns it's gaze on you.")
            slow_text("Within seconds, his blast hits you directly!")
            slow_text("You drop to the floor. Dead.")
            slow_text("END")
            slow_text("\n ")
            slow_text("Thanks for playing, Guardian!")
            slow_text("Would you like to play again?")
            play_again()


def play_again():
    """
    Option to allow player to play again or exit
    """
    slow_text("Yes or No?")
    user_input = ""
    user_input = input("\n> ").capitalize()
    if user_input == "Yes":
        new_story.introduction()
    elif user_input == "No":
        slow_text("Thank you for playing, Guardian!")
        clear_worksheet()
        sys.exit()
    else:
        slow_text("Please enter Yes or No.")


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
        class_worksheet.update_cell(2, 4, weapon)
        slow_text(f"You've found a {weapon}!")
        return weapon

    elif weapon_find is False:
        slow_text("There was nothing in the chest, only dust...")


def handle_vandal():
    """
    function for random Vandal encounter
    """
    vandal_attack = random.choice([True, False])
    if vandal_attack is True:
        slow_text("Out of nowhere, a Fallen Vandal attacks you!")
        slow_text("You took some damage :(")
        guardian.health -= random.randint(1, 100)
        slow_text(f"\nHealth: {guardian.health}")
        if guardian.health < 0:
            slow_text("You are dead!")
            slow_text("Your Ghost can ressurect you. Do you want him to?")
            play_again()


new_story = Story()

new_story.introduction()
