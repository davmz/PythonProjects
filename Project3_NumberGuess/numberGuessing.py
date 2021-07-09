"""
Name: David Montanez
Reason: Hello World
Created: July 7, 2021
Updated: July 7, 2021
"""

# Library Used for the Project
# https://docs.python.org/3/library/random.html
import random

### Program
## Have the user guess the random
def userGuess(x):
    randomNumber = random.randint(1, x)
    
    tries = 0
    guess = 0
    while(guess != randomNumber):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        tries += 1
        
        if(guess < randomNumber):
            print("Too Low! Please try again...\n")
        elif(guess > randomNumber):
            print("Too High! Please try again...\n")

    print(f"\nCongrats! You have guessed the number. It was {randomNumber}!")
    print(f"It took you {tries} tries to get the right number!")

## Have the computer guess your number
def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    tries = 0

    while(feedback != "c"):
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"\nIs {guess} too high (H), too low (L), or correct (C)?: ").lower()
        tries += 1

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"\nThe computer has guessed your number, {guess}, correctly!")
    print(f"It took the computer {tries} tries to get the right number!")

mode = ""
guessRange = ""
while(mode != "y" or mode != "c"):
    print("Welcome to Guess the Number! To exit press please press (E).")
    mode = input("Choose between who is guessing. You (Y) or Computer (C): ").lower()

    if(mode == "y"):
        guessRange = int(input("\nEnter a range of numbers to guess from: "))
        userGuess(guessRange)
    elif(mode == "c"):
        guessRange = int(input("\nEnter a range of numbers the computer has to guess from: "))
        computerGuess(guessRange)
    elif(mode == "e"):
        raise SystemExit