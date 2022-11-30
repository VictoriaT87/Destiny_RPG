"""
This is all the text used throughout the game.
"""


def introduction_text():
    """
    Introduction to the game to run first
    """

    print(
        '''
Welcome Guardian!
This is a text adventure game based on the video game Destiny!
\nYou are a New Light - a person newly re-awoken by a small
robot companion known as a Ghost.
You are now a Guardian, chosen to wield the Light
to defeat the Darkness.\n
Let's get your adventure started!\n
''')


def choose_name_text():
    """Ask player to choose their name"""

    print('''
- - - - - - -
Eyes up, Guardian.\n
I've finally found you.\n
I've been searching for you for centuries.\n
What should I call you?
''')


def choose_class_text():
    """Ask player to choose their class"""

    print('''
Let's try to figure out what kind of Guardian you are...\n
Do you think you're a Hunter, Warlock or Titan?\n
Hunter: Agile and daring, Hunters are quick on their feet
and quicker on the draw.\n
Warlock: Warlocks weaponize the mysteries of the universe
to sustain themselves and devastate their foes.\n
Titan: Disciplined and proud, Titans are capable of both
aggresive assaults and stalwart defenses.\n
''')


def choose_subclass_text():
    """Ask player to choose their subclass"""

    print('''
Each Lightbearer has a choice... \n
Your subclass defines your personality and skill.
You must choose now. Are you a... \n
''')


def first_scene_text():
    """first story choice for player"""

    print(
        '''
You look around and notice you're in a familiar place...\n
This is the Cosmodrome. The last thing you remember is
fighting here in a war against The Fallen.
But now everything is overgrown, it feels as if centuries
have passed.\n
You look around. Behind you is a cliff edge.
In front of you are some cars. Beyond them is an entrance
to a building.
What do you want to do?\n
1. Search the cars?
2. Go to the building entrance?
3. Run off the cliff behind you? This is all too weird!
''')


def entrance_text():
    """building entrance text"""

    print(
        '''
The building is long abandoned, rust covers the doors.
All the windows are broken.
In front of you, you see a chest...\n
Try to open the chest?
Yes or No?
''')


def hallway_text():
    """hallway story text"""

    print(
        '''
You enter into a long hallway inside the building.
Ahead you can see 2 open doorways.
You can enter one of them or continue down the hallway.
What do you want to do?\n
1. Enter door 1?
2. Enter door 2?
3. Continue down the hallway?
''')


def empty_room_text():
    """empty room story text"""

    print('''
You look around the room.
It seems completely empty, just dust.
You turn around and decide to pick a different option\n
You return to the hallway. Do you want to go to
1. Door 1?
or
2. Continue down the hall?
''')


def spaceship_room_text():
    """spaceship room story text"""

    print('''
Ahead of you, you see a giant open room ahead
with a spaceship in it!
You can see straight away that the ship
is missing it's engine.\n
As soon as you take a step back, you hear a sound.
A rumbling from the walls...\n
The roof cracks open and you see a Fallen Captain emerge!
He's carrying the engine!
If you want it, you'll have to take it from him.\n
Fight or Run?
''')


def captain_fight_win_text():
    """ Text for winning the captain fight """

    print('''
You feel the Light course through you!
You use your ultimate ability - your Super.
You wield the Light, you aim at the Captain
and hit him with the full force of your Super.\n
He staggers... and falls dead.\n
You grab the engine and Ghost installs it.
The ship rumbles to life and takes off.
Next destination - The Tower... Home.
[END]\n
Well done Guardian! You win!
Would you like to play again?
    ''')


def captain_fight_lose_text():
    """ Text for losing the captain fight """

    print('''
You feel the Light course through you!
You use your ultimate ability - your Super.
You wield the Light, you aim at the Captain
But you miss!\n
The Captain turns to you and aims his gun.
He hits you directly and you fall down... dead.\n
[END]\n
Your Ghost can resurrect you. Do you want him to?
    ''')


def captain_fight_run():
    """ Text if player chooses to run from the captain fight """

    print('''
This Captain is giant!\n
No way you want to take him on. You turn and run.
But behind you is an army of Dregs.\n
Within seconds you're swarmed...\nAnd your Light
fades.\n
[END]\n
Thanks for playing, Guardian!
Would you like to play again?
''')


def luck_roll_win():
    """ Text if player wins their luck roll against the Servitor """

    print('''
\nYou manage to hide behind some nearby crates
before the giant fallen Servitor sees you.\n
You wait for his eye to close before you turn and run
the down the hallway on the right!\nPhew!\n
''')


def luck_roll_lose():
    """ Text if player loses their luck roll against the Servitor """

    print('''
\nOh no, a Fallen Servitor! "
"You have no time to move before his giant Eye"
"turns it's gaze on you. Within seconds, his blast"
"hits you directly! You drop to the floor. Dead."
"[END]\nThanks for playing, Guardian!"
"Would you like to play again?
''')
