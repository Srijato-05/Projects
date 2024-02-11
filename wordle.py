# Simple Wordle Game by Srijato Das
import random
from collections import Counter
from colorama import Fore, Back, Style

# Function to generate feedback for the user's guess compared to the actual word
def generate_feedback(guess, random_word):
    # Count the occurrences of each letter in the random_word
    word_letter_count = Counter(random_word)

    # Create a list to hold the feedback for each letter
    feedback = []

    # First pass: Check for correct letters in the correct positions (green)
    for idx, letter in enumerate(guess):
        if letter == random_word[idx]:
            # Correct letter and position: green color
            feedback.append(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{letter}{Style.RESET_ALL}")
            word_letter_count[letter] -= 1
        else:
            # Placeholder for second pass
            feedback.append(None)

    # Second pass: Check for misplaced letters (yellow) and incorrect letters (red)
    for idx, letter in enumerate(guess):
        if feedback[idx] is None: # Only process letters that weren't marked green
            if letter in random_word and word_letter_count[letter] > 0:
                # Correct letter but wrong position: yellow color
                feedback[idx] = f"{Fore.YELLOW}{Back.LIGHTYELLOW_EX}{letter}{Style.RESET_ALL}"
                word_letter_count[letter] -= 1
            else:
                # Incorrect letter: red color
                feedback[idx] = f"{Fore.RED}{Back.LIGHTRED_EX}{letter}{Style.RESET_ALL}"

    # Combine the feedback into a single string
    return ''.join(feedback)

# Main function to run the Wordle game
def wordle_game(word_list, word_length=6, max_tries=5):
    # Choose a random word of the correct length
    random_word = random.choice([word for word in word_list if len(word) == word_length]).lower()
    # Uncomment the next line for debugging to see the random word
    print(random_word)
    print("WORDLE GAME")
    print(f"You have {max_tries} tries to guess the {word_length} letter word. Good Luck!")

    tries = 0  # Initialize the number of tries
    while tries < max_tries:
        guess = input(f"Guess the {word_length} letter word: ").lower().strip()

        # Check if the guess is the correct length
        if len(guess) != word_length:
            print(f"Please enter a {word_length} letter word.")
            continue

        # Check if the guess is correct
        if guess == random_word:
            print(f"Congratulations! You've guessed the word: {random_word.upper()}")
            return

        # Generate and display feedback
        feedback = generate_feedback(guess, random_word)
        print(feedback)
        tries += 1  # Increment the number of tries
        print(f"Try Again\nTries left: {max_tries - tries}")

    # The user has run out of tries
    print(f"Sorry, you've run out of tries. The word was: {random_word.upper()}.")

# List of predefined 6-letter words for the game
word_list = ["banana", "cherry", "durian", "lemons", "nutmeg", "orange", "papaya", "tomato"]
# Uncomment the following line to start the game
wordle_game(word_list)