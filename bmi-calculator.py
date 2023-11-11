# Get user input for height in meters
height = float(input("Enter your height in meters (e.g., 1.55): "))

# Get user input for weight in kilograms
weight = int(input("Enter your weight in kilograms (e.g., 72): "))

# Calculate BMI
BMI = weight / (height ** 2)

# Determine BMI category and provide feedback
if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI:.2f}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI:.2f}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI:.2f}, you are obese.")
else:
    print(f"Your BMI is {BMI:.2f}, you are clinically obese.")
