import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

words = ["aceola","aprium","banana","babaco","cherry","durian","feijoa","lemons","nutmeg","orange","papaya","tomato"]
random_word = random.choice(words)
guess_answer = ['_'] * len(random_word)
incorrect_letter_position = []
tries_left = 5
print("Random Word: ", random_word)

print("WORDLE GAME\nYou have 5 tries to guess the 6 letter word. Good Luck!")
guess = (input("Guess the 6 letter word: ")).lower()

while (tries_left > 0):
    if guess == random_word:
        print("You Win")
        break
    
    for letter in range (len(guess)):
        if len(guess) != len(random_word):
            print("Invalid Guess. Try Again")
            continue
        if guess[letter] == random_word[letter]:
            guess_answer[letter] = random_word[letter]
            
        if guess[letter] != random_word[letter] and guess[letter] in random_word:
            incorrect_letter_position.append(guess[letter])
    
    print("Incorrect Letter Positions: ", end="")
    for display_incorrect_position in incorrect_letter_position:
        print(f"{Fore.YELLOW}{display_incorrect_position}{Fore.WHITE}", end=" ")
    incorrect_letter_position.clear()
    
    print("\nGuess Result: ", end="")
    for display_correct_guess in guess_answer:
        if (display_correct_guess == '_'):
            print(f"{Fore.RED}{display_correct_guess}{Fore.WHITE}", end=" ")
        else:
            print(f"{Fore.GREEN}{display_correct_guess}{Fore.WHITE}", end=" ")
            
    print()
    print("Try Again")
    tries_left -= 1
    guess = input("Guess the word: ")
    if tries_left == 0:
        print("You Lose")
