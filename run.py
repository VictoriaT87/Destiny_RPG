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
        name = input("\n> ")
        # https://www.w3schools.com/python/ref_string_isalpha.asp
        if not name.isalpha():
            print("Please enter letters only.")
            continue
        else:
            print(f"Hello {name}. Welcome to your Destiny.")
            break
    return name

get_name()