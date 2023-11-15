# Import the 'random' module for generating random choices.
import random

# ASCII art representations for Rock, Paper, and Scissors.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get user input for their choice (Rock: 0, Paper: 1, Scissors: 2).
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

# Generate a random choice for the computer (Rock: 0, Paper: 1, Scissors: 2).
computer_choice = str(random.randint(0, 2))

# Display the user's choice using ASCII art.
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
else:
    print(scissors)

# Display the computer's choice using ASCII art.
if computer_choice == "0":
    print("Computer chose:", rock)
elif computer_choice == "1":
    print("Computer chose:", paper)
else:
    print("Computer chose:", scissors)

# Determine the winner based on user and computer choices.
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "0" and computer_choice == "1":
    print("You lose!")
elif user_choice == "0" and computer_choice == "2":
    print("You win!")

elif user_choice == "1" and computer_choice == "0":
    print("You win!")
elif user_choice == "1" and computer_choice == "2":
    print("You lose!")

elif user_choice == "2" and computer_choice == "0":
    print("You lose!")
elif user_choice == "2" and computer_choice == "1":
    print("You win!")
