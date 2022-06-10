# Write your solution below the starter code
# Follow the instructions in the tab to the right

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Make a choice for the computer player
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices

player_input = input("Rock, Paper, or Scissors? ")
player_choice = player_input.title()

import random
options = ["Rock", "Paper", "Scissors"]
computer = random.choice(options)
print(f"The computer chooses {computer}")

if not (player_choice == "Rock" or player_choice == "Paper" or player_choice == "Scissors"):
  print("You have to enter Rock, Paper, or Scissors")
elif player_choice == computer:
  print(f"{player_choice} and {computer}. It's a draw.")
elif player_choice == "Rock" and computer == "Paper":
  print("Paper covers Rock. You lose!")
elif player_choice == "Rock" and computer == "Scissors":
  print("Rock smashes Scissors. You win!")
elif player_choice == "Paper" and computer == "Rock":
  print("Paper covers Rock. You win!")
elif player_choice == "Paper" and computer == "Scissors":
  print("Scissors cut Paper. You lose!")
elif player_choice == "Scissors" and computer == "Rock":
  print("Rock smashes Scissors. You lose!")
elif player_choice == "Scissors" and computer == "Paper":
  print("Scissors cut Paper. You win!")
