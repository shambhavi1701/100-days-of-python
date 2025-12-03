# Accessing items from the nested list

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
clean_fifteen = ["Avocados", "Sweet Corn", "Pineapples", "Cabbage", "Onions", "Sweet Peas", "Papayas", "Asparagus", "Mangoes", "Eggplants", "Honeydew Melons", "Kiwis", "Cantaloupes", "Cauliflower", "Broccoli"]

grocery_list = [dirty_dozen, clean_fifteen]

print("Grocery List:")
print(grocery_list)
print()

print("Dirty Dozen Items:")
for item in grocery_list[0]:
    print(item)
print()

print("Clean Fifteen Items:")
for item in grocery_list[1]:
    print(item)
print()

# Accessing specific items
first_dirty_item = grocery_list[0][0]   # "Strawberries"
first_clean_item = grocery_list[1][0]   # "Avocados"   

print(f"The first item in the Dirty Dozen is: {first_dirty_item}")
print(f"The first item in the Clean Fifteen is: {first_clean_item}")