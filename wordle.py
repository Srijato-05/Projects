# Importing the 'random' module to enable the selection of a random word from a list
import random
# Importing colorama to add colored output in terminal; 'init' is called to enable colorama in Windows
from colorama import Fore, Back, Style, init
init(autoreset=True)  # Ensures that each print statement only temporarily changes the text style

# List of potential words to be guessed in the game
words = ["aceola", "aprium", "banana", "babaco", "cherry", "durian", "feijoa", "lemons", "nutmeg", "orange", "papaya", "tomato"]
# Randomly selecting a word from the list to be the answer
random_word = random.choice(words)

# Displaying the game's introduction and instructions
print("WORDLE GAME\nYou have 5 tries to guess the 6 letter word. Good Luck!")
# Initializing the number of tries the player has
tries_left = 5
# For debugging purposes, printing the selected word (you would normally comment this out)
print(random_word)

# Starting the game loop, which continues as long as the player has tries left
while tries_left > 0:
    # Prompting the player for their guess
    guess = input("Guess the 6 letter word: ").lower()

    # Checking if the entered guess is the correct length
    if len(guess) != len(random_word):
        # Informing the player their guess was the wrong length and prompting them to try again
        print("Invalid Guess. Try Again")
        # Reducing the number of tries left
        tries_left -= 1
        # Showing the player how many tries they have left
        print("Tries left: ", tries_left)
        # If the player runs out of tries, the game ends and reveals the correct word
        if tries_left == 0:
            print("You Lose")
            print("The word was: ", random_word)
        # Skipping the rest of the loop to ask for a new guess
        continue

    # Checking if the player's guess is correct
    if guess == random_word:
        # Congratulating the player for guessing correctly with green colored text
        print(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess}{Fore.RESET}{Back.RESET}\nYou Win!")
        # Breaking out of the loop as the player has won
        break

    # Initializing a string to provide feedback on the player's guess
    feedback = ""
    # Iterating over each letter in the player's guess
    for letter in range(len(guess)):
        # If the letter is in the correct position, it's added to the feedback string in green
        if guess[letter] == random_word[letter]:
            feedback += f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"
        # If the letter is in the word but the wrong position, it's added in yellow
        elif guess[letter] in random_word:
            feedback += f"{Fore.YELLOW}{Back.LIGHTYELLOW_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"
        # If the letter is not in the word, it's added in red
        else:
            feedback += f"{Fore.RED}{Back.LIGHTRED_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"

    # Displaying the feedback for the player's guess
    print(feedback)
    
    # If the guess is incorrect, reduce the number of tries and prompt to try again
    if guess != random_word:
        tries_left -= 1
        print("Try Again")
        print("Tries left: ", tries_left)

    # If the player has no more tries left, the game ends and the correct word is revealed
    if tries_left == 0:
        print("You Lose")
        print("The word was: ", random_word)