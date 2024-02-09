import random 

number = random.randint(1, 250)
name=input("Enter your name: ")
print("Hello, ",name)
guess = int(input("Enter an integer from 1 to 250: "))
tries_left=10
while number != "guess":
    if tries_left==0:
        print("You have no more tries left. The number was ",number)
        break
    if guess < number:
        print("Guess is too Low")
        tries_left-=1
        guess = int(input("Enter an integer from 1 to 250: "))
    elif guess > number:
        print("Guess is too High")
        tries_left-=1
        guess = int(input("Enter an integer from 1 to 250: "))
    else:
        tries_left-=1
        print("Congratulations, ", name, "!! You guessed it!")
        print("It took you ",10-tries_left," tries")
        break