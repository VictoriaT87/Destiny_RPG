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


def first_choice():
    """first story choice for player"""
    print(
        '''
You look around and notice you're in a familiar place...
This is the Cosmodrome. The last thing you remember is
fighting here in a war against The Fallen.
But now everything is overgrown, it feels as if centuries
have passed.\nYou look around. Behind you is a cliff edge.
In front of you are some cars. Beyond them is an entrance
to a building.
What do you want to do?\n
1. Search the cars?
2. Go to the building entrance?
3. Run off the cliff behind you? This is all too weird!
'''
    )


def entrance():
    """entrance text"""
    print(
        '''
The building is long abandoned, rust covers the doors.
All the windows are broken.
In front of you, you see a chest...\n
Try to open the chest?"
Yes or No
        '''
    )


def hallway():
    """hallway story text"""
    print(
        '''
\n"
You enter into a long hallway inside the building.
Ahead you can see 2 open doorways.
You can enter one of them or continue down the hallway.
What do you want to do?
1. Enter door 1?\n
2. Enter door 2?\n
3. Continue down the hallway?
    ''')
