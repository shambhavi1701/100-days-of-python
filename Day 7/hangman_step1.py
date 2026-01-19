# Hangman Game - Step 1
# In this step, we will set up the basic structure of the Hangman game.
# This code selects a random word from a predefined list and prompts the user to guess a letter.
# It also reveals the chosen word for testing purposes.
# Next steps could include checking if the guessed letter is in the word and providing feedback to the user.

import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

print(f"The word is {word}.")

guess_letter = input("Choose a letter: ").lower()
print("You guessed:", guess_letter)

# This loop iterates through each letter in the chosen word and compares it to the user's input.
# If the letter matches, it prints "Right"; otherwise, it prints "Wrong".
for i in word:
    if i == guess_letter.lower():
        print("Right")
    else:
        print("Wrong")
