# Simple Python Code Snippets

Welcome to the Simple Python Code Snippets repository! This collection consists of small Python scripts demonstrating various concepts and applications for beginners. Each script is designed to be easy to understand and serves as a practical example for learning Python.

## Scripts

### 1. BMI Calculator

#### Overview
The BMI Calculator script calculates Body Mass Index (BMI) based on user-provided height and weight inputs. BMI is a measure of body fat and is commonly used to classify individuals into different weight categories.

#### Instructions
1. Run the script by executing the command: `python bmi_calculator.py`.
2. Enter your height when prompted (in meters).
3. Enter your weight when prompted (in kilograms).

#### Output
The script will calculate your BMI and provide feedback on your weight category.

#### BMI Categories
- **Underweight:** BMI < 18.5
- **Normal Weight:** 18.5 <= BMI < 25
- **Slightly Overweight:** 25 <= BMI < 30
- **Obese:** 30 <= BMI < 35
- **Clinically Obese:** BMI >= 35

### 2. Bill Calculator

#### Overview
The Bill Calculator script calculates the total payment and share per person for a bill, including a customizable tip percentage. It helps in splitting the bill evenly among a specified number of people.

#### Instructions
1. Run the script by executing the command: `python bill_calculator.py`.
2. Enter the total bill amount when prompted.
3. Choose the tip percentage from the options: 10, 12, or 15.
4. Enter the number of people to split the bill.

#### Output
The script will display the calculated tip amount, total payment, and the share each person should pay.

#### Example
```bash
$ python bill_calculator.py
What was the total bill? $100
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 4
Tip amount: $12.00
Total payment: $112.00
Each person should pay: $28.00


#### Example
```bash
$ python bmi_calculator.py
Enter your height in meters (e.g., 1.75): 1.75
Enter your weight in kilograms (e.g., 72): 65
Your BMI is 21.22, you have a normal weight.
