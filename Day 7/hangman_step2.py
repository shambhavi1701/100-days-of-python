# Hangman Game - Step 2
# In this step, we will randomly select a word from a predefined list,
# create a placeholder for the word, and allow the user to guess a letter.
# We will then display the correctly guessed letters in their respective positions.

import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
print("The word is :")
print(word)

placeholder = ""
for letter in word:
    placeholder += "_"
print(placeholder)

guess_letter = input("Choose a letter: ").lower()
print("You guessed:", guess_letter)


display = ""
for i in word:
    if i == guess_letter.lower():
        display += i
    else:
        display += "_"
print(display)