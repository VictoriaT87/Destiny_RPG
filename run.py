# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



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
            print(f"Hello {name}. Welcome to your Destiny.")
            break
    return name

    
def get_class():
    """
    Player chooses their class. 3 available based on Destiny lore.
    """
    print("Let's try to figure out what kind of Guardian you are... \n")
    print("Do you think you're a Hunter, Warlock or Titan?\n")
    print("Hunter: Agile and daring, Hunters are quick on their feet and quicker on the draw.\n")
    print("Warlock: Warlocks weaponize the mysteries of the universe to sustain themselves and devastate their foes.\n")
    print("Titan: Disciplined and proud, Titans are capable of both aggresive assaults and stalwart defenses.\n")
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


if __name__ == "__main__":
  while True:
    """
    Introduction to the game to run first
    """

    print("Welcome Guardian!")
    print("This is a text adventure game based on the video game Destiny!\n")
    print("You are a New Light - a person newly re-awoken by a small robot companion")
    print("known as a Ghost. You are now a Guardian, chosen to wield the Light")
    print("to defeat the Darkness.\n")

    print("Let's get your adventure started!\n")
    print("\n")
    
    get_name()
    get_class()
    break
