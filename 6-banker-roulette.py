# Split the input string into an array, separating each name by a comma and space.
names = names_string.split(", ")

# Import the 'random' module for randomly selecting a payer.
import random

# Generate a random index to choose a payer from the list of names.
payer_index = random.randint(0, len(names) - 1)

# Print the selected payer for the meal.
print(f"{names[payer_index]} is going to buy the meal today!")
