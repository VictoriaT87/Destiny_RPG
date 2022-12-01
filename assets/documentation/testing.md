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
Choose story option 1, 2 or 3 | Player must enter one of these options or options are repeated | As expected | Pass
Chooses story option 1 to search cars | Function to search cars runs | As expected | Pass
Chooses story option 2 to enter building | Function to enter building runs | As expected | Pass
Chooses story option 3 to exit game | You run towards the cliff and jump! This is all too much to take.[END] | As expected | Pass
Searching the cars either finds a key or not | Receive message "You've found a key!" or "But you didn't find anything" | As expected | Pass
Function runs automatically to enter the building | Building story text will print | As expected | Pass
Pick yes or no to search the chest | If another option is entered, receive message "Please enter Yes or No." | As expected | Pass
Pick yes to open the chest with key | Message "You've used your key" received | As expected | Pass
Pick yes to open the chest without key | Message "You don't have a key and the lock won't budge." | As expected | Pass
Pick no to open the chest | Message "The chest looks old and worn...\n" | As expected | Pass
If chest is opened, random roll for a weapon | Message "You've found a {weapon}!, spreadsheet updated | As expected | Pass
If chest is opened, random roll for a weapon | Message "There was nothing in the chest, only dust..." | As expected | Pass
Building hallway function runs | Story text to choose a path runs | As expected | Pass
Player must choose 1, 2 or 3 in Hallway function | If anything other than 1, 2 or 3, receive message "Please choose number 1, 2 or 3." | As expected | Pass
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
Spaceship room function with high luck roll | Message "you aim at the Captain
and hit him with the full force of your Super." prints | As expected | Pass
Spaceship room function with low luck roll | Message "You wield the Light, you aim at the Captain But you miss" prints | As expected | Pass
Player is asked if they want to play again | Message "Would you like to play again?" prints | As expected | Pass
### Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Press something before 'enter' on intro screen | Receive message ""You typed '{input}'. The game will not start yet." and should remain on intro screen | As expected | Pass
Type something other than letters when asked for name | Receive message "Please enter letters only." | As expected | Pass
Type something other than races listed or with capital letters | Receive message "Please type one of the races listed and ensure to use lowercase." | As expected | Pass
Type something other than class listed or with capital letters | Receive message "Please type one of the classes listed and ensure to use lowercase." | As expected | Pass
Type something other than weapons listed or with capital letters | Receive message "Please type one of the weapons listed and ensure to use lowercase. | As expected | Pass
Type something other than yes/Yes or no/No during exit game | Receive message "Please type either yes/Yes or no/No" | As expected | Pass
Type something other than 1, 2 or 3 during decision stages | Receive message "Please type either '1', '2', or '3'." | As expected | Pass
Type something other than 1 or 2 during option to play again after winning | Receive message "Please type either '1', or '2'." | As expected | Pass
Type something other than 1 or 2 during option to play again losing| Receive message "Please type either '1', or '2'." | As expected | Pass


## Fixed bugs

 Below is a description of fixed bugs from unit test fails.

 ### get_name()

  - #### Reason for fail:

    - User could input a name that was 1 or 2 characters long.

  - #### Fix:

    - Add len(name.strip(" ")) to the function - user now needs to input a username 3 characters or longer.
    
  ![Hand Value Solution](README-images/hand_value.png) 

  ### get_subclass()

  - #### Reason for fail:

    - Players need to enter a number - either 1, 2 or 3. However if they enter any other number, an error occurs "IndexError: list index out of range"

  - #### Fix:

    - I originally tried to use a range() for the input but with I struggled with making this work. Upon further research, I realised I could add an if statement to my Try, to make sure the user input either 1, 2 or 3.

   ![Name Input Solution](README-images/name-input.png)   

  ### instructions()

  - #### Reason for fail:

    - When testing my instruction screen text I noticed that the text was not lining up correctly when deployed on Heroku.

  - #### Fix:

    - After some more testing and research I concluded that the new line method I was using was incorrect. I had been using \ (backslashes) to enter a new line of text but I found if i simply used inverted commas and lined up the text in a block along with \n, the text would line up as I wanted. See below code snippet for function solution.

   ![Instruction text solution](README-images/instruction-solution.png)   
