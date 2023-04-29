import os


# Introduction and Rules
def intro():
    print("Welcome to Escape from ISS Ravana")
    print("Escape from ISS Ravana is a text based survival game.")
    print("You will have to collect all the items within the ship to take on.")
    print("Defeat the intruder and escape with your life!")
    
    input("Press any key to continue ")


def clear():

    os.system("cls" if os.name == "nt" else "clear")


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


intro()
clear()

name = input("Whats is your name ")

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
            print("As you enter the room you hear some noises")
            print("A giant creatue jumps out at you!!!")
            print("The giant Xenos rips you limb")
            print("GAME OVER !!!")
            break

        else:
            print("As you enter the room you hear some noises")
            print("A giant creatue jumps out at you!!!")
            print("You pull out the gun you found")
            print("You enter into battle with the creatue")
            print("You defeat the Xenos")
            print(f"Computer: Well Done {name}, You did it!")
            print("Computer: Please find the access code for the escape pod")
            print("that are hidden in this room!")

    player_movement = input("What is your next move? ").title()

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
        print(f"{name} You exit the Game")
        break

    elif action == "Restart":
        print(f"{name} You have restarted the game")
        clear()
        backpack.clear()
        current_deck = "Mid"
        computer = ' '
        intro()