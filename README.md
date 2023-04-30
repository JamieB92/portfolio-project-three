# Escape from the ISS Ravana
Escape from the ISS Ravana is a terminal text-based horror survival game where you wake up from an intergalactic slumber to find your crew mates all dead around you.<br> 
The aim of the game is to explore the ship to discover what has killed your crew. Along the way, the player will need collect items to be able to escape and defeat the mysterious intruder.<br>
The game has been built to test the players short term memory whilst telling a story along the way.<br>
Click <a href="https://escape-from-the-iss-ravana.herokuapp.com/" target=" _blank">here</a> to play the game. 

<img src="./images/intro.png">


# User Experience
## Home Page
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

## User controls:
The user is able to control the game by entering certain commands.<br> 
If the user wants to move between rooms they need to type "go" followed by a direction which is either left, right, up, or down, and then hit enter.<br>
Within the hud this will inform the user which direction they have gone, whilst changing the name of the room to reflect the room the user has moved to.

<img src="./images/movement.png">

When the user sees an item they will have to type "get" followed by the items name, which will then be added to the backpack.<br>
The hud will inform the user that they have picked the item up and the user will be able to see the item in the backpack.

See item:<br>
<img src="./images/item-see.png">

Get item:<br>
<img src="./images/item-get.png">

The user also has other commands in the game as well.<br>
If the user types in "Restart" the game will restart which will reset everything bar the users name:<br>
### Enter Restart
<img src="./images/restart-begin.png">

### Middle 
<img src="./images/restart-middle.png">

### End
<img src="./images/restart-end.png">



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