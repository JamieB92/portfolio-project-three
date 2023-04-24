import os


# Introduction and Rules 
def intro():
    print("Welcome to Escape from ISS Ravana")
    print("Escape from ISS Ravana is a text based survival game.")
    print("You will have to collect all the items within the ship to take on.")
    print("Defeat the intruder and escape with your life!")
    
    input("Press any key to continue ")


def clear():

    os.system('cls')


# Play Area
areas = {
    'Mid Deck': {'Left': 'Lower Deck', 'Right': 'Recreation', 'Up': 'Medical Deck', 'Down': 'Armory'},
    'Lower Deck': {'Left': 'Engineering', 'Right': 'Mid Deck', 'Up': 'Bay 1', 'Down': 'Bay 2'},
    'Engineering': {'Right': 'Lower Deck', 'Item': 'Magazine'},
    'Bridge': {'Left': 'Recreation Deck', 'Intruder': 'Xenos', 'Item': 'Pin'},
    'Bay 1': {'Right': 'Medical', 'Up': 'Escape Pod', 'Down': 'Lower Deck'},
    'Bay 2': {'Right': 'Weapon Deck', 'Up': 'Lower Deck', 'Item': 'Torch'},
    'Armory': {'Left': 'Bay 2', 'Up': 'Mid Deck', 'Item': 'Bullets'},
    'Medical': {'Left': 'Bay1', 'Down': 'Mid Deck', 'Item': 'Bandages'},
    'Recreation': {'Left': 'Mid Deck', 'Right': 'Bridge', 'Up': 'Officers', 'Down': 'Crew Deck', 'Item': 'Grenade'},
    'Officer': {'Down': 'Recreation', 'Item': 'Gun'},
    'Crew': {'Up': 'Recreation', 'Item': 'Armour'},
    'Escape Pod': {'Down': 'Bay 1', 'Escape': 'Use Pod'}
    }


backpack = []

current_deck = "Mid Deck"

msg = ""


intro()
clear()

name = input("Whats is your name ")

while True:
        
    # Hud 
    print(f"{name} you are in the {current_deck} \nBackpack : {backpack}\n{'-'* 27}")
    
    print(msg)
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

    player_movement = input("Enter Direction")

    new_movement = player_movement.split(' ')

    action = new_movement[1].title()

    if len(new_movement) > 1:
        item = new_movement[1]
        direction = new_movement[1].title()

    if action[0] == 'Go ':
        current_deck = areas[current_deck][direction]
        print(f"you've gone {direction}")
    else:
        print("You walked into a wall")

    if action == "Get":

       