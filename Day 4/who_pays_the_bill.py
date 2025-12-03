# Find out who pays the bill at a restaurant

import random
print("Welcome to the Restaurant Bill Picker!")

print("I will select a random person from your group to pay the bill.")

friends = ['Harry', 'Hermione', 'Ron', 'Cho', 'Ginnie', 'Draco']

print()
print("List of friends :- ")
for i in friends:
    print(i)
print()
print("I have picked the person")
print()

index = random.randint(0,len(friends)-1)

person_who_pays = friends[index]

print(f"The person who will pay the bill is {person_who_pays}")
