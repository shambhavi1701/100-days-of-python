# Loops in Python

# For Loop
# A for loop is used when you have a specific range or a list of items to process. 
# It is "bounded," meaning it will automatically stop once it reaches the end of the specified range.
# Example of a for loop that prints numbers from 1 to 9:

print("For Loop Example:")
for i in range(1, 10):
    print(i)
print()

# While Loop
# A while loop is used when you want to repeat an action until a certain condition is no longer true. 
# It is "unbounded," meaning it will continue indefinitely until the condition is met.
# Example of a while loop that prints numbers from 1 to 9:

print("While Loop Example:")
count = 1
while count < 10:
    print(count)
    count += 1


# Loop Control Statements
# break: Terminates the loop prematurely.
# continue: Skips the current iteration and continues with the next one.

# Summary:
# - Use a for loop when you know in advance how many times you want to iterate.
# - Use a while loop when you want to continue looping until a specific condition changes.