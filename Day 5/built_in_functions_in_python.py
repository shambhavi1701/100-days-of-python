# Built in Functions in Python

fruits = ["Apple","Mango","Orange"]
for fruit in fruits:
	print(fruit)


marks = [85, 90, 78, 92, 88]

#sum()
print("Total Marks:", sum(marks))

# Using loop to calculate sum
sum = 0
for mark in marks:
    sum+=mark
print("Total Marks using loop:", sum)


#max()
print("Highest Mark:", max(marks))

# Using loop to find max
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest Mark using loop:", highest)



#min()
print("Lowest Mark:", min(marks))

# Using loop to find min
lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark
print("Lowest Mark using loop:", lowest)


#len()
print("Number of Marks:", len(marks))

# Using loop to count length
count = 0
for mark in marks:
    count += 1
print("Number of Marks using loop:", count)


#sorted()
print("Sorted Marks:", sorted(marks))

# Using loop to sort (Bubble Sort)
sorted_marks = marks[:]
for i in range(len(sorted_marks)):
    for j in range(0, len(sorted_marks)-i-1):
        if sorted_marks[j] > sorted_marks[j+1]:
            sorted_marks[j], sorted_marks[j+1] = sorted_marks[j+1], sorted_marks[j]
print("Sorted Marks using loop:", sorted_marks)


#range()
print("Range of numbers from 0 to 4:", list(range(5)))

# Using loop to create range
range_list = []
for i in range(5):
    range_list.append(i)
print("Range of numbers from 0 to 4 using loop:", range_list)

