# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")
print()
print('R represents Rock, P represents Paper, S represents Scissors')
print()

import random

while True:
  # Get a choice from the user
  player_choice = input("Choose an option (R, P, or S?): ").title()
  
  if not (player_choice=="R" or player_choice=="P" or player_choice=="S"):
    print("You didn't enter a valid option. You have to enter R, P, or S")
    print()
    continue

  else:
    if player_choice == "R":
      player_choice = "Rock"
  
    elif player_choice == "P":
      player_choice = "Paper"

    elif player_choice == "S":
      player_choice = "Scissors"

  # Make a choice for the computer player
  options = ["Rock", "Paper", "Scissors"]
  computer = random.choice(options)
  
  # Compare the user and computer choice
  # Print the right message, based on the choices
  if player_choice == computer:
    print(f'Player ({player_choice}) : CPU ({computer})')
    print(f"{player_choice} and {computer}. It's a draw.")
    print('Go again!')
    print()
    continue

  elif player_choice == "Rock" and computer == "Paper":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Paper covers Rock. You lose!")
    print()
    break

  elif player_choice == "Rock" and computer == "Scissors":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Rock smashes Scissors. You win!")
    print()
    break

  elif player_choice == "Paper" and computer == "Rock":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Paper covers Rock. You win!")
    print()
    break

  elif player_choice == "Paper" and computer == "Scissors":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Scissors cut Paper. You lose!")
    print()
    break

  elif player_choice == "Scissors" and computer == "Rock":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Rock smashes Scissors. You lose!")
    print()
    break

  elif player_choice == "Scissors" and computer == "Paper":
    print(f'Player ({player_choice}) : CPU ({computer})')
    print("Scissors cut Paper. You win!")
    print()
    break
