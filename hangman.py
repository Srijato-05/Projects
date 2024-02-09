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
        print(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess}{Fore.RESET}{Back.RESET}", end=" ")
        print("You Win")
        break
    
    for letter in range (len(guess)):
        if len(guess) != len(random_word):
            print("Invalid Guess. Try Again")
            continue
        if guess[letter] == random_word[letter]:
            print(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess[letter]}{Fore.RESET}{Back.RESET}", end=" ")
            
        elif guess[letter] != random_word[letter] and guess[letter] in random_word:
            print(f"{Fore.YELLOW}{Back.LIGHTYELLOW_EX}{guess[letter]}{Fore.RESET}{Back.RESET}", end=" ")
        else: 
            print(f"{Fore.RED}{Back.LIGHTRED_EX}{guess[letter]}{Fore.RESET}{Back.RESET}", end=" ")
            
    print()
    print("Try Again")
    tries_left -= 1
    guess = input("Guess the word: ")
    if tries_left == 0:
        print("You Lose")
