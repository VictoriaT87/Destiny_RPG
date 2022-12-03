# Destiny Text Adventure Game

![Website responsiveness on multiple screen sizes](assets/documentation/DestinyRPG.png)

Welcome to a Destiny Text Adventure Game! This game is built purely using Python. It's designed to be a fun "Choose your own adventure" game, with random luck elements and items. Based on the very popular games [Destiny and Destiny 2](https://www.bungie.net/), this text adventure will bring you through the first mission in the game, from waking on the Cosmodrome to getting your ship's engine to fly to the Tower. If you get a high luck score and you choose the correct path, you'll make it out alive!

[Live link to The Destiny Text Adventure Gamecl](https://destiny-rpg.herokuapp.com/)


<br>

# Table of Contents

1. [Features](#features)
    * [Game Start](#game-start)
    * [Class and Subclasses](#classes-and-subclasses)
    * [Random Luck and Encounters](#random-luck-and-encounters)
    * [Inventory](#inventory)
    * [Play Again](#play-again)
    * [Future Features](#play-again)
2. [Project Goals](#project-goals)
3. [User Stories](#user-stories)
4. [Design](#design)
5. [Technologies](#technologies)
    * [Languages Used](#languages-used)
    * [Libraries And Frameworks](#libraries-and-frameworks)
    * [Tools and Resources](#tools-and-resources)
6. [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Other Testing](#other-testing)
7. [Bugs Found and Fixed](#bugs-found-and-fixed)
    * [Bugs Not Fixed](#bugs-not-fixed)
8. [Credits And Sources](#credits-and-sources)
9. [Deployment](#deployment)
10. [Acknowledgements](#acknowledgements)

# Features 

## Existing Features

### Game Start
![Start Screen Image](assets/documentation/start-screen.png)
- The first thing to load is a logo for the game, created with the [Pyfiglet Library](https://pypi.org/project/pyfiglet/). This is a large Ascii text image, saying "Destiny RPG Game".
- Along with this is a small paragraph explaining the game and the story for any users that have no prior knowledge of the Destiny games.

### Classes and Subclasses
- The player will be asked to enter their name first and then they are given a choice of which Destiny Class they would like to be, as well as their subclass. These choices are then stored in a Google Sheets Worksheet, allowing this data to be pulled later on in the game to reference the player.
- Depending on their choices here, the game will later on pick a grenade ability of the element selected in a fight scene. 

![Class Selection](assets/documentation/class-choice.png)
![Subclass Selection](assets/documentation/subclass-choice.png)
![Ability From Worksheet](assets/documentation/grenade-ability.png)

### Random Luck and Encounters
- When the game first loads, players will be given a random luck number between 1-100. This is chosen using the randint Method. This will effect the end game for the player as well as in certain fights.
- A random encounter can occur for the player. In certain rooms, an encounter will roll to either True or False. If this is True, the encounter with a Vandal will run and players will lose a certain amount of health, again chosen by the randint Method. 

![Random Encounter](assets/documentation/random-encounter.png)

### Inventory
- For their first choice, players can search some cars in front of them. If they're lucky, the can find a key, which will allow them to open a chest within the story. This chest has a chance of dropping a weapon, which will give them a greater advantage of winning the game.
- This item is stored in the Google Sheets Worksheet, allowing the name to be recalled later in the story.
- After all stats are added, the Player Stats sheet will look like this:

![Random Encounter](assets/documentation/google-sheets.png)

### Play Again
- At the end of the game or if the player dies, they have the option of playing again. This will trigger code to reset the workseet stats, reset the console and run the story from the beginning.

![Play Again](assets/documentation/play-again.png)

<br>

[Back to Top](#table-of-contents)

<br>

## Future Features

- I'd love to add either some animation or colour, if possible. I feel this would make the game more appealing to play, especially to younger generations who haven't played Text Adventure games before.
- The story and encounters could be fleshed out more, with different scenarios, more of an inventory and more randomness.
- Each subclass also has a unique "Super ability" in the actual Destiny games. I thought of implementing this but felt I would have more repetitive code. When I learn more Python, it would be fun to add this in without repeating myself.

<br>

[Back to Top](#table-of-contents)

<br>

## Project Goals

* I wanted to create an old school Choose Your Own Adventure type game but with the Destiny theme. As a kid, I played my fair share of text based Adventure games and the appeal of them has never left me. Bringing a new game into an old game was an idea I was very fond of.

* As a purely python game, I knew something that had multiple choices, as well as an inventory system, was going to be challenging to me for this project.

<br>

[Back to Top](#table-of-contents)

<br>

## User Stories

* Users will:

  * Play a Text Based Adventure Game with a story from Destiny The Game.
  * Have a different game experience every time they play, with random weapons, encounters and luck.
  * Be able to restart the game without needing to refresh or reload the link.

* Users expect:

  * A fun to play text adventure game in an old school style.
  * A Destiny themed game, with enemies, classes and weapons they recognize.
  * Replayability.
  * A fast paced game, playing through the first Destiny story mission.

<br>

[Back to Top](#table-of-contents)

<br>

## Design

- My starting point on this project was designing a flow chart based on the first story mission in Destiny The Game. To make the text adventure more fun, I added the random encounters and ability to choose ways to go and luck based weapons.

<img src="assets/documentation/flow-chart.png" alt="flow-chart" width="600"/>


<br>

[Back to Top](#table-of-contents)

<br>

# Technologies

## Languages Used
* [Python](https://www.python.org/)

## Libraries And Frameworks
* [Google Sheets](https://www.google.com/sheets/about/)
* [gspread](https://docs.gspread.org/en/v5.7.0/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/)
* [os](https://docs.python.org/3/library/os.html#os.system)
* [random](https://docs.python.org/3/library/random.html)
* [time](https://docs.python.org/3/library/time.html)

## Tools And Resources
* [GitPod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Heroku](https://heroku.com)
* [ReadMe Template](https://github.com/Code-Institute-Solutions/readme-template)
* [Lucid Chart](https://www.lucidchart.com/)
* [Stack Overflow](https://stackoverflow.com/)
* [Canva](https://www.canva.com/) for my README image.

<br>

[Back to Top](#table-of-contents)

<br>

# Testing 
### Validator Testing 

* All code passed through the CI Python Linter with no issues or warnings

![Linter Result](assets/documentation/linter.png)
 <br>


### Other Testing
 - For a list of all manual testing done and functions tested, please follow [this link](assets/documentation/testing.md).

 <br>


[Back to Top](#table-of-contents)

<br>

# Bugs Found and Fixed

 Below is a description of fixed bugs.

 ### get_name function - Length

  - #### Reason for fail:

    - User could input a name that was 1 or 2 characters long or an unlimited length.

  - #### Fix:

    - Add len(name.strip(" ")) to the function - user now needs to input a username between 3 characters and 8.

  ### get_subclass function - IndexError

  - #### Reason for fail:

    - Players need to enter a number - either 1, 2 or 3. However if they enter any other number, an error occurs "IndexError: list index out of range"

  - #### Fix:

    - I originally tried to use a range() for the input but I struggled with making this work because of the input containing an f-string. Upon further research, I realised I could add an if statement to my Try, to make sure the user input either 1, 2 or 3.

![Subclass Index](assets/documentation/subclass_index.png) 

  <br>

  ### get_subclass function - Invalid Literal

  - #### Reason for fail:

    - Entering a string in the Subclass input was giving the error "invalid literal for int() with base 10"

  - #### Fix:

    - Researching this took me a long time. As I was enumerating the list for Subclass choices with an index (that starts at 0), I needed the input to be an int. I asked for help on both Reddit.com/LearnPython and StackOverflow and eventually figured out that with a Try statement, I could add a ValueError and an if statement to make sure the player entered a number between 1 and 3 and it wasn't a string.
    ``` 
    try:
        choice = int(input(f"\nMake your choice, {chosen_class}."
                "\n1, 2 or 3?\n>"))
        if choice < 1 or choice > 3 or choice == str():
            raise ValueError
        except ValueError:
          print("Please enter number 1, 2 or 3.")
    ```

![Subclass Int Error](assets/documentation/subclass-int-error.png)

<br>

### get_subclass function - Choices Not From Spreadsheet

  - #### Reason for fail:

    - When calling get_subclass, it was choosing the last game's choice, instead of the current one. 

  - #### Fix:

    - To fix, I passed the chosen_class parameter to get_subclass:
        - if player_class == "Hunter":
        - if chosen_class == "Hunter":

  <br>

  ### Else statements

  - #### Reason for fail:

    - If a player entered a choice that wasn't listed for certain options, the error message would print to the terminal. However, instead of repeating the choices, the game would then print a different function's questions.

  - #### Fix:

    - For this, I realised I needed to add the word "continue" within my Else statement. This made the code loop again if an incorrect option was entered.

  <br>

![Else Statements](assets/documentation/else-statement.png)

  <br>

  ### Player Health not clearing each run

  - #### Reason for fail:

    - Everytime the health function would run, it would choose a randint between 1 and 100. This would be removed from the players starting health of 100. However, if a player chose to re-run the game, the players health would stay as the negative number. This meant the player would always die at the Dreg Fight function.

  - #### Fix:

    - Add the code "guardian.health = 100" to the play_again function. This would reset it every time.

![Player Health](assets/documentation/health_bug.png)

<br>

 ### dreg_fight() function not calling the correct values

  - #### Reason for fail:
  
    - The dreg_fight function was not calling the correct values.
    
  - #### Fix:
  
    - I had originally put the parameters in the function for the returned values of (chosen_class, chosen_subclass, abilities, weapon), however I realised that because of the different classes I have, this wasn't working. To fix it, I wrote local variables to pull the values from the spreadsheet instead.

![Dreg Fight Variables](assets/documentation/fight_error.png)

<br>

 ### Object has no Attribute

  - #### Reason for fail:
  
    - When going through the story, some of the functions failed to run with the error "object has no attribute".
    
  - #### Fix:
  
    - Instead of calling the class, I was calling a 'self.' method. This worked for some versions of the adventure that the player chose but if the adventure went to the GameFunctions class back to the Story functions class, it wouldn't be able to find the correct object. To fix this, I wrote "GameFunctions.object(self, )" or "Story.object(self, )". This worked to fix the issue.

![Dreg Fight Variables](assets/documentation/attribute_error.png)

<br>

 ### Error Code 400 on gspread

  - #### Reason for fail:
  
    - When running the player_abilites function, I would get an error saying "gspread.exceptions.APIError: {'code': 400,..."
    
  - #### Fix:
  
    - Researching lead to me to understand that I had my possible abilites in a [list] and the google spreadsheet couldn't understand that. Removing them from a list and putting them in a Tuple fixed this error.

<br>

 ### Potentially compromised credentials 

  - Not a bug necessarily but a lesson learned. When creating a 2nd Heroku deployment, I used the same creds.json file as this and was informed by an email from Google, Github and Heroku that my key was compromised. I had to remake the key for this project as a result and update it on Heroku.

![Potentially compromised credentials](assets/documentation/creds-comp.png)

<br>

# Separated Project
 - After looking at some other Text Adventure games and talking over it with my Mentor, I decided to split the run.py files in separate ones for the sake of easy readability. This project worked as intended, however on first run when all imports were added, I got the error message: "AttributeError: partially initialized module has no attribute (most likely due to a circular import)". This was because my functions file was importing the story file and vice versa. This was fixed by adding "from ... import ..." statements.
 - The project being split into multiple separate files worked, however the loading time for it was a little over 10 seconds when deployed to Heroku. This made it feel like the program was hanging or just not working when the "Run Program" button was clicked in Heroku. Because of this, I decided to revert all my changes back into the single run.py file, however I made a new repo with the old files, and have linked it here: [Destiny RPG Multi-File](https://github.com/VictoriaT87/Destiny_RPG_Multi_File), as well as the deployed version here: [Destiny RPG Mutli-File Deplyed](https://destiny-multifile.herokuapp.com/)
 - I understand this is not going to be assessed, I just would personally like to keep it so I can perhaps figure out why it was so slow to load. My research lead me to believe this was either because of a cache issue or just some bottleneck I have in the code.

# Bugs Not Fixed
 - I would like the printed enumarate list in the get_subclass function to print to the terminal as slowly as the rest of the text. However, when I try to add function.s_print (to call the slow typing), it tells me I can't have both (index, subclass) in the method - "Too many positional arguments in method call". I have not found a fix for this.

<br>

[Back to Top](#table-of-contents)

<br>

# Credits and Sources

- The Project is built using the foundation from the [Elijah Henderson youtube videos on "Let's Make a Text Adventure Game In Python"](https://www.youtube.com/watch?v=HzDcKq2NDwM)
- The classes, subclasses, abilites, weapons and enemies are based on the video game [Destiny by Bungie](https://www.bungie.net/)
- The slow typing code was found on [StackOverflow.com](https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out)
- Clearing the terminal when starting the game or replaying was based on code found on [StackOverflow.com](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
- Random choice code was found on [Pynative.com](https://pynative.com/python-random-choice/)
- Code for enumerating the index and text in get_subclass was made with help from [GeeksforGeeks.org](https://www.geeksforgeeks.org/enumerate-in-python/)
- Getting the value from individual cells was found at [StackOverflow.com](https://stackoverflow.com/questions/19480449/reading-particular-cell-value-from-excelsheet-in-python)
- Deleting a certain row from the Google spreadsheet was found in [pythoninoffice.com](https://pythoninoffice.com/use-python-to-delete-excel-rows-columns/)
- Object Oriented Programming and Classes were learned on the [Tech With Tim Youtube Channel](https://www.youtube.com/watch?v=JeznW_7DlB0)
- Validation for entering a number in the get_subclass function was found at [StackOverflow.com](https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers)
- The fix to add a Try statement into the get_subclass function int(input()): [StackOverflow.com](https://stackoverflow.com/questions/71374555/prevent-error-on-intinput-that-is-a-string-and-prevent-negative-number-input) and [Programiz.com](https://www.programiz.com/python-programming/exception-handling)
- Raising a ValueError if player entered a string or the incorrect number in the get_subclass function [DigitalOcean.com](https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples)

<br>

[Back to Top](#table-of-contents)

<br>

# Deployment

The following are the steps I went through to deploy my live site:

- The site was deployed using Heroku. The steps to deploy are as follows: 
1. Go to [Heroku](https://dashboard.heroku.com/apps)
2. Go to 'New' and select 'Create a new app'
3. Input your app name and create app.
4. Navigate to 'Settings'
5. Install the needed buildpacks. Select Python and install and then node.js and install and then click save. They must be in this order.
6. Navigate to the 'Deploy' section. 
7. Connect to GitHub, search for your repo and confirm. 
8. Choose branch to deploy.
9. Your app should now be available to see. You can choose whether to have your app automatically redeploy with every push or to keep it manual. 

- To Fork the repository:
  - On GitHub.com, navigate to the repository.
  - In the top-right corner of the page, click Fork.
  - Select an owner for the forked repository.
  - By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
  - Optionally, add a description of your fork.
  - Choose whether to copy only the default branch or all branches to the new fork.
  - Click Create fork.

- To Clone the repository:
  - On GitHub.com, navigate to the repository.
  - Above the list of files, click the Code button.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter. Your local clone will be created.

<br>

The live link can be found here - [Destiny RPG Game](https://destiny-rpg.herokuapp.com/)

<br>

[Back to Top](#table-of-contents)

<br>

# Acknowledgements
- To my amazing boyfriend Thomas. For listening to me worry about this project for months, for keeping me sane, for helping me switch off after a long day with a cup of coffee and a bar of chocolate :)
- My family and my cats for keeping my stress levels under control!
- My Mentor [Jubril Akolade](https://github.com/Jubrillionaire) for all the help. His guidance was invaluable.
- [Sean Finn](https://github.com/seanf316/) and [Sean Johnston](https://github.com/seanj06/), my fellow classmates on Slack. Your help with my many questions was super appreciated, thank you.

<br>

[Back to Top](#table-of-contents)