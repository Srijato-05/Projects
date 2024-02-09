import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

words = ["aceola", "aprium", "banana", "babaco", "cherry", "durian", "feijoa", "lemons", "nutmeg", "orange", "papaya", "tomato"]
random_word = random.choice(words)

print("WORDLE GAME\nYou have 5 tries to guess the 6 letter word. Good Luck!")
tries_left = 5
print(random_word)
while tries_left > 0:
    guess = input("Guess the 6 letter word: ").lower()

    if len(guess) != len(random_word):
        print("Invalid Guess. Try Again")
        tries_left -= 1
        print("Tries left: ", tries_left)
        if tries_left == 0:
            print("You Lose")
            print("The word was: ", random_word)
        continue

    if guess == random_word:
        print(f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess}{Fore.RESET}{Back.RESET}\nYou Win!")
        break

    feedback = ""
    for letter in range(len(guess)):
        if guess[letter] == random_word[letter]:
            feedback += f"{Fore.GREEN}{Back.LIGHTGREEN_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"
        elif guess[letter] in random_word:
            feedback += f"{Fore.YELLOW}{Back.LIGHTYELLOW_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"
        else:
            feedback += f"{Fore.RED}{Back.LIGHTRED_EX}{guess[letter]}{Fore.RESET}{Back.RESET}"

    print(feedback)
    
    if guess != random_word:
        tries_left -= 1
        print("Try Again")
        print("Tries left: ", tries_left)

    if tries_left == 0:
        print("You Lose")
        print("The word was: ", random_word)