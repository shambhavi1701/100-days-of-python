# LIST OPERATIONS 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original list:", fruits)
print("Reversed list:", fruits[::-1])
print()

# Slicing the list
print("First three fruits:", fruits[:3])
print()
# Accessing elements using negative indexing
print("Accessing element using negative indexing")
print("fruits[-1]",fruits[-1])
print("fruits[-5]",fruits[-5])
print()
# print(fruits[-6]) This will raise an IndexError since the list has only 5 elements.
# print(fruits[-7])  This will raise an IndexError since the list has only 5 elements./


# Adding an element to the list
# Using append() method
fruits.append("fig")
print("List after adding 'fig':", fruits)

# Using insert() method
fruits.insert(2, "blueberry")
print("List after inserting 'blueberry' at index 2:", fruits)

# Using extend() method
fruits.extend(["grape", "honeydew"])
print("List after extending with 'grape' and 'honeydew':", fruits)

print()
# Removing an element from the list
# Using pop() method
removed_fruit = fruits.pop()  # Removes the last element
print("List after popping the last element ('{}'): {}".format(removed_fruit, fruits))

# Using remove() method
fruits.remove("banana")
print("List after removing 'banana':", fruits)