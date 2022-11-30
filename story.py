import sys
import random
import pyfiglet

import gspread
from google.oauth2.service_account import Credentials

import functions
import text
import character


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


class Story:
    """
    Functions for the story and player choices
    """

    def introduction(self):
        """
        First function to run on Start.
        Logo image, introduction text, luck roll and worksheet cleared
        """

        text1 = pyfiglet.figlet_format("DESTINY", justify="center")
        text2 = pyfiglet.figlet_format("RPG GAME", justify="center")
        print(text1)
        print(text2)

        text.introduction_text()

        functions.GameFunctions.clear_worksheet(self)
        functions.GameFunctions.inital_luck(self)
        character.UserInputs.get_name(self)

    def opening_scene(self):
        """
        First scene to play after choosing a name and class
        """

        text.first_scene_text()

        user_input = ""

        while True:
            user_input = input("\n> ")
            if user_input == "1":
                self.search_cars()
            elif user_input == "2":
                self.building_entrance()
            elif user_input == "3":
                print("You run towards the cliff and jump! This is all "
                      "too much to take. [END]")
                functions.GameFunctions.clear_worksheet(self)
                sys.exit()
            else:
                print("Please enter a valid option.")
                continue

    def search_cars(self):
        """
        Function to search the cars
        """

        print("You decide to search through some of the abandoned cars.")
        functions.GameFunctions.check_items(self)

        if character.guardian.items == ["key"]:
            print("You put your key away and walk towards the building.")
            self.building_entrance()
        else:
            print("But you didn't find anything")
            self.building_entrance()

    def building_entrance(self):
        """
        Function to enter the building and try to open a chest
        """

        text.entrance_text()
        functions.GameFunctions.open_chest(self)
        self.building_hallway()

    def building_hallway(self):
        """
        Function to play scene on entering the building hallway,
        call fight scene or end
        """
        text.hallway_text()

        user_input = ""

        while True:
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
                continue

    def empty_room(self):
        """
        Empty room, player must turn around and choose another option
        from building_hallway
        """
        functions.GameFunctions.handle_vandal(self)

        text.empty_room_text()

        user_input = ""

        while True:
            user_input = input("\n> ")
            if user_input == "1":
                print("You enter door 1. It's a small room with a Fallen Dreg"
                      " inside!")
                self.dreg_fight()
            if user_input == "2":
                self.spaceship_room()
            else:
                print("Please enter a valid option.")
                continue

    def dreg_fight(self):
        """
        fight scene function, checks for weapon from random roll
        or else use abilities
        """
        player_class = stats_worksheet.cell(2, 1).value
        player_subclass = stats_worksheet.cell(2, 2).value
        player_ability = stats_worksheet.cell(2, 3).value
        stored_weapon = stats_worksheet.cell(2, 4).value

        # Health system from Elijah Henderson
        # https://www.youtube.com/watch?v=n17Hkgi8rt4
        character.guardian.health -= random.randint(1, 100)
        print("Before you can make a move, the Dreg takes one shot with "
              "his weapon.\nIt hits you on the arm!"
              )
        print(f"\nHealth: {character.guardian.health}")
        if character.guardian.health < 0:
            print("You are dead!")
            print("Would you like to play again?")
            functions.GameFunctions.play_again(self)

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
        functions.GameFunctions.handle_vandal(self)

        print("\n ")
        print("Ahead, you see 2 corridors.")
        print("Do you want to go left, right or back?")

        user_input = ""

        while True:
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
                functions.GameFunctions.clear_worksheet(self)
                sys.exit()
            else:
                print("Please enter either left, right or back.")
                continue

    def spaceship_room(self):
        """
        Spaceship room choice function
        """
        text.spaceship_room_text()

        user_input = ""

        while True:
            luck = stats_worksheet.cell(2, 5).value

            user_input = input("\n> ").capitalize()
            if user_input == "Fight":
                if luck >= "50":
                    text.captain_fight_win_text()
                    functions.GameFunctions.play_again(self)

                elif luck <= "49":
                    text.captain_fight_lose_text()
                    functions.GameFunctions.play_again(self)

            elif user_input == "Run":
                text.captain_fight_run()
                functions.GameFunctions.play_again(self)
            else:
                print("Please enter either fight or run.")
                continue

    def luck_escape(self):
        """
        Function to check whether the player escapes from the ambush
        """
        if functions.GameFunctions.inital_luck(self) > 50:
            text.luck_roll_win()
            self.spaceship_room()
        else:
            text.luck_roll_lose()
            functions.GameFunctions.play_again(self)


def main():
    """Start the game"""

    new_story = Story()

    new_story.introduction()
