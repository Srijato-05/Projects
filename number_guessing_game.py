# Simple Number Guessing Game by Srijato Das

import random 

# Generate a random integer between 1 and 250
number = random.rand(1, 250)

# Get the user's name and greet them
name = input("Enter your name: ")
print("Hello, ", name)

# Get the user's first guess
guess = int(input("Enter an integer from 1 to 250: "))

# Set the number of tries left to 10
tries_left = 10

# Loop until the user's guess is equal to the random number
while number != guess:
   
    # Check if the user has no tries left
    if tries_left == 0:
        # Print a message and break the loop
        print("You lost !!")
        print("You have no more tries left. The number was ", number)
        break

    # Check if the user's guess is less than the random number
    if guess < number:
        # Print a message and decrement the number of tries left
        print("Guess is too Low")
        tries_left -= 1
        # Get the user's next guess
        guess = int(input("Enter an integer from 1 to 250: "))

    # Check if the user's guess is greater than the random number
    elif guess > number:
        # Print a message and decrement the number of tries left
        print("Guess is too High")
        tries_left -= 1
        # Get the user's next guess
        guess = int(input("Enter an integer from 1 to 250: "))

    # Check if the user's guess is equal to the random number
    else:
        # Print a message, decrement the number of tries left, and break the loop
        tries_left -= 1
        print("Congratulations, ", name, "!! You guessed it!")
        print("It took you ", 10 - tries_left, " tries")
        break