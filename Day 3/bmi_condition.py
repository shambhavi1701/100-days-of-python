# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

print("Welcome to the BMI calculator.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")
