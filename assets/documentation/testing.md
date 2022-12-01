## Manual Testing

This table is all the manual testing done for each function, if it worked as expected or not.

 ### Features

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Press 'enter' on intro screen | The first story text should run | As expected | Pass
Type a name into terminal when prompted | Receive message "It's nice to meet you, {name}." | As expected | Pass
Pick a class from the options | Receive message "Welcome, {chosen_class}." | As expected | Pass
Pick a class from the options | Receive message "Ah, a {player_class}." | As expected | Pass
Pick weapon from the options | Receive message "The mighty {weapon}, of course... of course." | As expected | Pass
Player name, race, class and weapon upload to spreadsheet and stats alter | Should be visible on spreadsheet and stats should be updated depending on player choices | As expected | Pass
Player picks exit game option | Receive message "You close your eyes and fall asleep. The game is over. You will never know what could have been. Want to start again? Please type yes or no." | As expected | Pass
Player types yes during exit game | Restart game at enter name stage | As expected | Pass
Player types no during exit game | Receive message "GAME OVER. THANK YOU FOR PLAYING." | As expected | Pass
Player type option number during decisions | Should progress to next stage | As expected | Pass
Game checks google sheet if certain items are in inventory | Should trigger specific events | As expected | Pass
Player wins game | Give option to play again | As expected | Pass
Player chooses to play again after winning | Restart at name section | As expected | Pass
Player chooses not to play again after winning | Receive message "Thank you again for playing!" | As expected | Pass
Player dies | Receive message "YOU HAVE DIED. GAME OVER" and option to play again | As expected | Pass
Player chooses to play again after losing | Restart at name section | As expected | Pass
Player chooses not to play again after losing | Receive message "Thank you for playing!" | As expected | Pass

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

    - After some more testing and research I concluded that I need to add the .strip() method at the end of my name input to get rid of any whitespace, I also need to add the .isalpha() method to make sure any input was a letter. See below code snippet for function solution.

   ![Name Input Solution](README-images/name-input.png)   

  ### instructions()

  - #### Reason for fail:

    - When testing my instruction screen text I noticed that the text was not lining up correctly when deployed on Heroku.

  - #### Fix:

    - After some more testing and research I concluded that the new line method I was using was incorrect. I had been using \ (backslashes) to enter a new line of text but I found if i simply used inverted commas and lined up the text in a block along with \n, the text would line up as I wanted. See below code snippet for function solution.

   ![Instruction text solution](README-images/instruction-solution.png)   
