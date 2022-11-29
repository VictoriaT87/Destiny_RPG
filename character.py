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

stats_worksheet = SHEET.worksheet('PlayerStats')


class Player:
    """
    Class for player inventory and weapon.
    """

    def __init__(self, items, health):
        self.items = items
        self.health = health


guardian = Player([], 100)


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
            stats_worksheet.update_cell(2, 1, chosen_class)
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

    while True:
        try:
            choice = int(input(f"\nMake your choice, {chosen_class}. \n"
                               "1, 2 or 3?\n>"))
        except ValueError:
            print('Please enter number 1, 2 or 3.')

        else:
            print(f"A {subclasses[choice-1]}?")
            print("The darkness doesn't stand a chance \n")
            chosen_subclass = subclasses[choice-1]
            stats_worksheet.update_cell(2, 2, chosen_subclass)
            self.player_abilites(chosen_subclass)
            self.opening_scene()

        # if choice != int(1, 2, 3):
        #     raise ValueError('Please enter number 1, 2 or 3')

        # chosen_subclass = subclasses[choice-1]
        # stats_worksheet.update_cell(2, 2, chosen_subclass)
        # self.player_abilites(chosen_subclass)
        # self.opening_scene()


def player_abilites(chosen_subclass):
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
