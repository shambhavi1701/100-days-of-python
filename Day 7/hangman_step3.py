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