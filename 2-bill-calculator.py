# Welcome message
print("Welcome to the bill calculator.")

# Get input for the total bill
bill = float(input("What was the total bill? $"))

# Get input for the tip percentage (10, 12, or 15)
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get input for the number of people to split the bill
num_people = int(input("How many people to split the bill? "))

# Calculate the share per person
tip_amount = bill * (tip_percentage / 100)
total_payment = bill + tip_amount
share_per_person = total_payment / num_people

# Display the result
print(f"Tip amount: ${round(tip_amount, 2)}")
print(f"Total payment: ${round(total_payment, 2)}")
print(f"Each person should pay: ${round(share_per_person, 2)}")
