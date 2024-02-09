import random
from collections import Counter
from colorama import Fore, Back, Style

def generate_feedback(guess, random_word):
    # Count the occurrences of each letter in the random_word
    word_letter_count = Counter(random_word)

    # Create a list to hold the feedback for each letter
    feedback = []

    # First pass: Check for correct letters (green)
    for idx, letter in enumerate(guess):
        if letter == random_word[idx]:
            feedback.append(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{letter}{Style.RESET_ALL}")
            word_letter_count[letter] -= 1
        else:
            feedback.append(None)  # Placeholder for second pass

    # Second pass: Check for misplaced letters (yellow) and incorrect letters (red)
    for idx, letter in enumerate(guess):
        if feedback[idx] is None:  # Only process letters that weren't marked green
            if letter in random_word and word_letter_count[letter] > 0:
                feedback[idx] = f"{Fore.YELLOW}{Back.LIGHTYELLOW_EX}{letter}{Style.RESET_ALL}"
                word_letter_count[letter] -= 1
            else:
                feedback[idx] = f"{Fore.RED}{Back.LIGHTRED_EX}{letter}{Style.RESET_ALL}"

    return ''.join(feedback)

def wordle_game(word_list, word_length=6, max_tries=5):
    # Randomly choose a word from the word_list
    random_word = random.choice([word for word in word_list if len(word) == word_length]).lower()
    print(random_word)
    print("WORDLE GAME")
    print(f"You have {max_tries} tries to guess the {word_length} letter word. Good Luck!")

    tries = 0
    while tries < max_tries:
        guess = input(f"Guess the {word_length} letter word: ").lower().strip()

        if len(guess) != word_length:
            print(f"Please enter a {word_length} letter word.")
            continue

        if guess == random_word:
            print(f"Congratulations! You've guessed the word: {random_word.upper()}")
            return

        feedback = generate_feedback(guess, random_word)
        print(feedback)
        tries += 1
        print(f"Try Again\nTries left: {max_tries - tries}")

    print(f"Sorry, you've run out of tries. The word was: {random_word.upper()}.")

# Example usage with a predefined list of 6-letter words
word_list = ["banana", "cherry", "durian", "lemons", "nutmeg", "orange", "papaya", "tomato"]
wordle_game(word_list)