import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to Rock, Paper, Scissors game!")

moves = [rock,paper,scissors]
print("Here are the moves:")
for move in moves:
    print(move)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print("You chose")
print(moves[user_choice])
print()
print("Computer chose")
print(moves[computer_choice])
print()

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == computer_choice-1 or user_choice == computer_choice+2:
    print("User looses the game!")
else:
    print("User wins the game!")