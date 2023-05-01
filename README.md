# Escape from the ISS Ravana
Escape from the ISS Ravana is a terminal text-based horror survival game where you wake up from an intergalactic slumber to find your crew mates all dead around you.<br> 
The aim of the game is to explore the ship to discover what has killed your crew. Along the way, the player will need collect items to be able to escape and defeat the mysterious intruder.<br>
The game has been built to test the players short term memory whilst telling a story along the way.<br>
Click <a href="https://escape-from-the-iss-ravana.herokuapp.com/" target=" _blank">here</a> to play the game. 

<img src="./images/intro.png">


# User Experience
## Home Screen
When the user first comes to the game they will be presented with a welcome screen.<br>
The welcome screen gives the user a brief introduction on the game and how the user is able to complete the game.<br>
Within the welcome screen the user is given instructions on how to play the game by providing a list of the commands they can use in game.<br>
Once the user is ready to play, the screen prompts the user to press enter to play.

<img src="./images/intro.png"><br>
<img src="./images/instructions.png">

## Intro story 
After the user has hit enter on the previous screen, they will be brought to the prologue of the game.<br>
Here the user is given a story before they enter into the game. <br>
For the user to continue, they must hit enter.

<img src="./images/story.png">

## AI introduction
Once the user arrives at this screen, the ships AI will introduce itself and ask for the users name.<br>
Giving the user the ability to choose their name makes the game more interactive and personal.<br>
Once the user has entered their name, they will be taken to the next screen.<br>

<img src="./images/name.png">

## Game Screen
Now the user has arrived at the game screen they will be able to see their hud.<br>
In the hud it tells the user what deck they are on, it will show them their backpack which will be empty and will ask the user to enter their next move.<br>

<img src="./images/main.png">

## User controls - The user is able to control the game by entering certain commands:<br>

## Move
If the user wants to move between rooms they need to type "go" followed by a direction which is either left, right, up, or down, and then hit enter.<br>
Within the hud this will inform the user which direction they have gone, whilst changing the name of the room to reflect the room the user has moved to.

<img src="./images/movement.png">

If the user is unable to go that direction there will be a message telling them they cant go that way.

<img src="./images/wrong-way.png">

## Get Item
When the user sees an item they will have to type "get" followed by the items name, which will then be added to the backpack.<br>
The hud will inform the user that they have picked the item up and the user will be able to see the item in the backpack.

See item:<br>
<img src="./images/item-see.png">

Get item:<br>
<img src="./images/item-get.png">

If the user enters an item that is not in the room or if the room is empty the user will get a prompt telling them that the item doesnt exisist.<br>
<img src="./images/doesnt-exisit.png">

If the user enters an item they already have it will prompt them saying they already have the armour:
<img src="./images/already-have-armour.png">


## Restart
If the user types in "Restart" the game will restart which will reset everything bar the users name:<br>
### Enter Restart
<img src="./images/restart-begin.png">

### Middle 
<img src="./images/restart-middle.png">

### End
<img src="./images/restart-end.png">

## Help
When the user enters in "Help" they will be presented with a list of directions on how to play the game:
<img src="./images/help.png">

## Exit
When the user wants to exit the game before finishing they need to type in exit which will stop the game and will present this message:
<img src="images/exit.png">

## Alien interaction
### Beat
When the user comes into contact with an intruder, the user will have to have collected a certain number of items to be able to defeat the intruders.<br> 
There are three intruders in the game, each requiring different amount of items to defeat them as they increase in difficulty as the game goes on.<br> 
If the user has the required amount of items, the screen will inform the user that they have defeated the intruder and also if there is an item in the room.<br>

<img src="./images/win.png">

### Loose
If the user does not have the correct amount of items, the game will end and the user will be informed that they have lost the game.<br> 
Within this screen it will also give the user a hint at how many items they need to defeat the intruder.<Br>

<img src="./images/loose.png">

## Completing the game
Once the user has defeated all three intruders the user needs to make their way to the escape pods to be able to complete the game.<br>
When the user arrives at the escape pod and has all the correct items they will be presented with this message:<br>
<img src="./images/game-win.png">

If the user hasnt got enough items they will be presented with this message: 
<img src="./images/escape-no.png">

# User Experience Feedback

## Shannon White - 30/04/2023
The overall game experience was very positive. The game provides plenty of challenges to overcome while you work your way around the ship. The game has an extra dimension of having to remember the route you take, so it is highly recommended that you make a note of the places you've been so you can create the map as you play the game. The game is logical and easy to follow, and with the added objective of defeating the boss to obtain the pin before being able to escape the ship, it is complex yet enjoyable.

# Testing

## CI Python Linter

I have tested my code through the CI Python Linter provided:
<img src="./images/ci_pylinter_pass.png">

## Home Screen 

* Is the user able to access the Intro Story by only hitting enter? 
    * Yes, I have tested this by hitting enter which takes the user to the Intro Story.
    * I have been able to test this by pressing other keys which doesnt take the user to the next screen.

* Once Enter has been hit does the user see the correct screen load? 
    * Yes, it loads the correct screen for the user.

*  Are the instructions & controls easy to read and take in for the user? 
    *  Yes, the intructions & controls are easy to read and understand.

## Intro Story

* Is the user able to access the AI Introduction by only hitting enter? 
    * Yes, I have tested this by hitting enter which takes the user to the AI Introduction.
    * I have been able to test this by pressing other keys which doesnt take the user to the next screen.

* Once Enter has been hit does the user see the correct screen load? 
    * Yes, it loads the correct screen for the user.

## AI Introduction

* Is the user able to access the Game Screen once a name has been entered? 
    * Yes, I have tested this by entering a name and then hitting enter which takes the user to the Game Screen.

* Is the user able to enter the game screen with out entering a name? 
    * Yes, The user is able to do this.
    * I have tested this by hitting enter before entering a name.

* Once Enter has been hit does the user see the correct screen load? 
    * Yes, it loads the correct screen for the user.

* Is the user able to create a username style name e.g with numbers and symbols?
    * Yes, I have been able to test this by adding numbers and symbols to the name and hitting enter.

## Game Screen 

### Movement

* Is the user able to move between rooms? 
    * Yes, the user is able to move between rooms.
    * I have tested this by entering go and the direction of choice

* Does the hud tell the user which room they are in? 
    * Yes, the user is able to see which room they are in.
    * I have tested this by changing rooms which changes the room in the hud

* Is the user able to use an incorrect movement? 
    * No, they are unable to and causes no effect to the game. 
    * I have tested this by entering incorrect commands 

* If the user cant move that way does the game tell them ?
    * Yes, the user is informed that they cant go that way 
    * I have tested this by entering a direction that leads to a wall







