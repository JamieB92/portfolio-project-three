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
    'Escape Pod': {'Down': 'Bay 1', 'Escape':'Use Pod'}
    }


backpack = []

current_deck = "Mid Deck"

msg = ""


intro()
clear()


while True:
        
    clear()

    print(f"You are in the {current_deck}:\nBackpack : {backpack}\n{'-'* 27}")

    print(msg)

    if "Item" in areas[current_deck].keys():

        close_item = areas[current_deck]["Item"]

        if close_item not in backpack:

            print(f"You see a {close_item}")