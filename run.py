import os
import time


def clear():

    os.system("cls" if os.name == "nt" else "clear")


# Introduction and Rules
def home():
    print("###############################################################")
    print("#                                                             #")
    print("#            Welcome to Escape from the ISS Ravana            #")
    print("#-------------------------------------------------------------#")
    print("#                                                             #")
    print("#     Escape from ISS Ravana is a text based survival game    #")
    print("#     Where the aim of the game is to escape from the ship    #")
    print("#     But keep your witts about you as you explore the ship   #")
    print("#            As you may not be the only one left!             #")
    print("#                                                             #")
    print("###############################################################")
    print("#                                                             #")
    print("#                      Instructions                           #")
    print("#-------------------------------------------------------------#")
    print("#                                                             #")
    print("#                     Type Commands :                         #")
    print("#       To Move between rooms type go and the direction:      #")
    print("#                 'Go' - 'Left', 'Right', 'Up', 'Down'        #")
    print("#       To Move between rooms type go and the direction       #")
    print("#             Type 'Restart' to Restart the game              #")
    print("#             Type 'Exit' to exit the game                    #")
    print("#                                                             #")
    print("###############################################################")
    input("#                  Press any key to continue                  #")
    clear()


def intro():
    print("###############################################################")
    print("#                                                             #")
    print("#                Escape from the ISS Ravana                   #")
    print("#-------------------------------------------------------------#")
    print("#                                                             #")
    print("#     Explosions and and the smell of and electrical fire     #")
    print("#     engulfs your senses, you struggle to open your eyes     #")
    print("#     after such a long sleep.                                #")
    print("#     Your cryo chamber door opens and you fall to the floor. #")
    print("#     As you get to your feet you see your friend Codys       #")
    print("#     body hanging out of their cryo chamber.                 #")
    print("#     You rush to cody to see if he is alive but he's dead!   #")
    print("#     You here a strange noise you have never heard before.   #")
    print("#     Your rush towards the sound but you trip and fall.      #")
    print("#     You get to you feet and tell yourself                   #")
    print("#     'I need to get of this ship....'                        #")
    print("#                                                             #")
    print("###############################################################")
    input("#                  Press any key to continue                  #")


# Play Area
areas = {
    'Mid': {'Left': 'Lower', 'Right': 'Recreation'},
    'Lower': {'Left': 'Engine', 'Right': 'Mid', 'Up': 'landing', 'Down': '2'},
    'Engine': {'Right': 'Lower', 'Item': 'Magazine'},
    'Bridge': {'Left': 'Recreation', 'Intruder': 'Xenos', 'Item': 'Pin'},
    'landing': {'Right': 'Med', 'Up': 'Escape Pod', 'Down': 'Lower'},
    '2': {'Right': 'Armory', 'Up': 'Lower', 'Item': 'Torch'},
    'Armory': {'Left': '2', 'Up': 'Mid', 'Item': 'Bullets'},
    'Med': {'Left': '1', 'Down': 'Mid', 'right': 'office', 'Item': 'Bandages'},
    'Recreation': {'Left': 'Mid', 'Right': 'Bridge', 'Item': 'Grenade'},
    'Officer': {'Left': 'Med', 'Item': 'Gun'},
    'Crew': {'Up': 'Recreation', 'Item': 'Armour'},
    'Escape Pod': {'Down': '1', 'Escape': 'Use Pod'}
    }


backpack = []

current_deck = "Mid"
computer = " "

home()
intro()
clear()
print("AI initating ...")
print("Hi Im Titan your ships AI,")
print("Welcome Aboard the ISS Ravana ")
name = input("Please confirm your name?\n")
clear()

while True:
    
    # Hud
    print(f"{name} you are in the {current_deck} deck. \nBackpack: {backpack}")
    
    print(computer)
    # Find Item
    if "Item" in areas[current_deck].keys():

        close_item = areas[current_deck]["Item"]

        if close_item not in backpack:

            print(f"You see a {close_item}")
        
    # Esacpe The ship Function
    if "Escape" in areas[current_deck].keys():

        if len(backpack) < 7:
            print(f"{name} You need to find the code to activate!")

        else:
            print(f"Well Done {name}, You escaped with your life!")
            break
    
    # Intruder interaction
    if "Intruder" in areas[current_deck].keys():

        if len(backpack) < 6:
            clear()
            print("As you enter the room you hear some noises")
            print("A giant creatue jumps out at you!!!")
            print("The giant Xenos rips you limb")
            print("GAME OVER !!!")
            break

        else:
            clear()
            print("As you enter the room you hear some noises")
            print("A giant creatue jumps out at you!!!")
            print("You pull out the gun you found")
            print("You enter into battle with the creatue")
            print("You defeat the Xenos")
            print(f"Titan: Well Done {name}, You did it!")
            print("Titan: Please find the access code for the escape pod")
            print("that are hidden in this room!")

    player_movement = input("What is your next move? ").title()
    clear()
    new_movement = player_movement.split(' ')

    action = new_movement[0].title()

    if len(new_movement) > 1:
        item = new_movement[1:]
        direction = new_movement[1].title()

        item = ' '.join(item).title()

# Movement
    if action == 'Go':

        try:
            current_deck = areas[current_deck][direction]
            computer = f"you've gone {direction}"
            clear()

        except Exception:
            computer = "You cant go that way"
            clear()
# Collect Items    
    if action == "Get":

        try:
            if item == areas[current_deck]["Item"]:

                if item not in backpack:

                    backpack.append(areas[current_deck]["Item"])
                    computer = f"you picked up the {item}"
                    clear()
                else:
                    computer = f"You already have {item}"
                    clear()
            else:
                computer = "The deck was empty"
                clear()
        except Exception:
            computer = "The deck was empty"
            clear()

    elif action == "Help":
        clear()
        print("Game Instructions!\n")
        print("To move enter:")
        print("'Go' and enter the direction 'Left, Right, Up, Down\n ")
        print("To pick up item enter:")
        print("'Get' and the items name 'Spanner'\n")
        print("To Exit the game type:\n'Exit'\n")
        print("To Restart the game type:\n'Restart'\n")
    
    elif action == "Exit":
        clear()
        print(f"{name} You have decided to quit you loose....")
        break

    elif action == "Restart":
        print(f"{name} You have restarted the game")
        clear()
        backpack.clear()
        current_deck = "Mid"
        computer = ' '
        intro()
