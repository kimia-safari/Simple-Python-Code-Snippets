# Welcome message
print("The Love Calculator is calculating your score...")

# Get names from user input
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# Combine names and convert to lowercase
names = name1 + name2
names_lower = names.lower()

# Count occurrences of each letter in the combined names
t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")

# Calculate the first and second digits of the love score
first_digit = t + r + u + e
second_digit = l + o + v + e

# Combine the digits to get the final love score
score = int(str(first_digit) + str(second_digit))

# Display the result based on the love score
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
