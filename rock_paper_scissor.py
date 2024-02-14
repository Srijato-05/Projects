# Stone Paper Scissors by Srijato

import random

choices  = ['stone', 'paper', 'scissors']
computer_choice =random.choice(choices) 

print("Welcome to the stone paper scissors game!") 
player_choice = input("Enter your choice (stone/paper/scissor): ").lower()  

if player_choice not in choices:
    print("Invalid choice. Please enter 'stone', 'paper', or 'scissors'.")
    exit()

# The following if-elif block compares the player's choice to the computer's choice and determines the winner
if player_choice == computer_choice:
   print("It's a tie!")
elif player_choice == 'stone':
   if computer_choice == 'paper':
       print("Computer wins!")
   else:
       print("Player wins!")
elif player_choice == 'paper':
   if computer_choice == 'scissors':
       print("Computer wins!")
   else:
       print("Player wins!")
elif player_choice == 'scissors':
   if computer_choice == 'stone':
       print("Computer wins!")
   else:
       print("Player wins!")