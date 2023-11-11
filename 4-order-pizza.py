# Welcome message
print("Thank you for choosing Python Pizza Deliveries!")

# Get user input for pizza size, pepperoni, and extra cheese
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the bill
bill = 0

# Calculate the base cost based on pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# Add cost for pepperoni based on size
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add cost for extra cheese
if extra_cheese == "Y":
    bill += 1

# Display the final bill
print(f"Your final bill is: ${bill}.")
