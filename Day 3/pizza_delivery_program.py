# Write a program that calculates the final bill for a pizza order based on size and additional toppings.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if add_pepperoni == 'Y':
    bill+=2

if extra_cheese == 'Y':
    bill+=1

if (size == 'S'):
    bill += 15
elif (size == 'M'):
    bill += 20
elif (size == 'L'):
    bill += 25
else:
    bill = 0

print(f"Your final bill is: ${bill}")
