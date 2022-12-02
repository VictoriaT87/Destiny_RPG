## Manual Testing

This table is all the manual testing done for each function, if it worked as expected or not.

 ### Features

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Press 'enter' on intro screen | The first story text should run | As expected | Pass
Type a name into terminal when prompted | Receive message "It's nice to meet you, {name}." | As expected | Pass
Pick a class from the options | Receive message "Welcome, {chosen_class}." | As expected | Pass
Pick a subclass from the options | Receive message "A {subclasses[choice-1]}?" | As expected | Pass
Player class, subclass and luck are uploaded to spreadsheet | Should be visible on spreadsheet | As expected | Pass
Chooses story option 1 to search cars | Function to search cars runs | As expected | Pass
Chooses story option 2 to enter building | Function to enter building runs | As expected | Pass
Chooses story option 3 to exit game | Message "You run towards the cliff and jump! This is all too much to take.[END]" prints | As expected | Pass
Searching the cars either finds a key or not | Receive message "You've found a key!" or "But you didn't find anything" | As expected | Pass
Function runs automatically to enter the building | Building story text will print | As expected | Pass
Pick yes to open the chest with key in inventory | Message "You've used your key" received | As expected | Pass
Pick yes to open the chest without key in inventory | Message "You don't have a key and the lock won't budge." | As expected | Pass
Pick no to open the chest | Message "The chest looks old and worn..." | As expected | Pass
If chest is opened, random roll for a weapon | Message "You've found a {weapon}!, spreadsheet updated | As expected | Pass
If chest is opened, random roll for a weapon | Message "There was nothing in the chest, only dust..." | As expected | Pass
Building hallway function runs | Story text to choose a path runs | As expected | Pass
Player chooses room 1 | Dreg attacks player for random health amount | As expected | Pass
Player chooses room 1 | Player character attacks back with no weapon, text to show "You're a {player_class}. A {player_subclass}. You can use your {player_ability}." | As expected | Pass
Player chooses room 1 | Player character attacks back with a weapon, text to show "You pull out your {stored_weapon}" | As expected | Pass
Hallway choice function automatically runs | Story text for Hallway choices runs and shows player options | As expected | Pass
Player chooses room 2 in Hallway | Empty room text prints, player is given the other 2 options for the Hallway | As expected | Pass
Random Vandal attack occurs | Message "Out of nowhere, a Fallen Vandal attacks you!", player loses a random amount of health. | As expected | Pass
Player chooses left from hallway options | SpaceShip function story prints | As expected | Pass
Player chooses right from hallway options | LuckEscape function text prints | As expected | Pass
Player has high luck number | Message "You manage to hide behind some nearby crates" prints | As expected | Pass
Player has low luck number | Message "Oh no, a Fallen Servitor!" prints, game ends | As expected | Pass
Player chooses back from hallway options | Game Ends | As expected | Pass
Spaceship room function with high luck roll | Message "you aim at the Captain and hit him with the full force of your Super." prints | As expected | Pass
Spaceship room function with low luck roll | Message "You wield the Light, you aim at the Captain But you miss" prints | As expected | Pass
Player is asked if they want to play again | Message "Would you like to play again?" prints | As expected | Pass
Player is asked if they want to be resurrected | Message "Please enter yes or no" prints | As expected | Pass

### Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Press something before 'enter' on intro screen | Receive message "You typed '{start}'. When you're ready to begin. press ENTER." and should remain on Introduction screen | As expected | Pass
Player enters something other than letters when asked for name | Receive message "Please enter letters only." | As expected | Pass
Type less than 3 characters when asked for name | Receive message "Please enter a name at least 3 letters long." | As expected | Pass
Player enters anything other than the 3 possible Classes | Receive message "Please type one of the classes listed." | As expected | Pass
Player enters anything other than the numbers 1, 2 or 3 when option arises | Receive message "Please enter number 1, 2 or 3." | As expected | Pass
Search function runs, awards a key to player inventory if True | Player inventory is updated or not, player receives message to inform them | As expected | Pass
Player types anything other than Yes or No when question arises | Receive message "Please enter yes or no" | As expected | Pass
Player receives a weapon | Receive message "You've found a {weapon}!" | As expected | Pass
Players don't enter either Fight or Run during Captain fight | Receive message "Please enter Yes or No." | As expected | Pass
Players don't enter either Yes or No when asked to be resurrected | Receive message "Please enter either fight or run." | As expected | Pass
