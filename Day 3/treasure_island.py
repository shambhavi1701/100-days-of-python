
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')


# --- CHOICE 1 ---
print("You started sailing toward the legendary Land of Aurum Isle.")
print("Suddenly, an enemy ship fires blazing fireballs at your deck!")
choice1 = input("Do you 1) Jump out of the ship or 2) Fight back?  ")

if choice1 != "1":
    print("You tried to fight back, but your ship sank. Game Over.")
    exit()

# --- CHOICE 2 ---
print("\nYou jump into the sea just before the ship collapses.")
print("You’re in deep pain but still swimming.")
print("A small wooden boat approaches with an old man inside.")
choice2 = input("Do you 1) Ask him for help or 2) Swim to the coast?  ")

if choice2 != "2":
    print("The old man helps you aboard, but pirates attack the boat. Game Over.")
    exit()

# --- CHOICE 3 ---
print("\nYou reach the coast, exhausted and starving.")
print("On the beach, you see bananas and a coconut.")
choice3 = input("Do you 1) Eat the bananas or 2) Drink the coconut?  ")

if choice3 != "2":
    print("A monkey saw you eating its bananas and attacks you. Game Over.")
    exit()

# --- CHOICE 4 ---
print("\nYou feel refreshed and explore deeper into the island.")
print("Suddenly, a huge lion charges toward you!")
choice4 = input("Do you 1) Run away or 2) Hide in the bushes ?")

if choice4 != "1":
    print("The lion finds you easily. Game Over.")
    exit()

# --- CHOICE 5 ---
print("\nYou run desperately and fall into a hidden stone well.")
print("Inside, you find three ancient doors:")
print("1) A wand symbol")
print("2) A sun symbol")
print("3) A fish symbol")
choice5 = input("Which door do you choose? 1, 2, or 3?  ")

if choice5 == "1":
    print("You fall into a magical world and everyone bullies you. Game Over.")
elif choice5 == "3":
    print("You enter an underwater world and can't breathe. Sharks attack! Game Over.")
elif choice5 == "2":
    print("\nWarm sunlight fills the room as the door opens.")
    print("You discover beautiful nature and the legendary treasure:")
    print("Gold, coins, statues, a boat, a monkey, a ship, and even the old man — all as golden ornaments.")
    print("YOU WIN!")
else:
    print("Invalid choice. Game Over.")
