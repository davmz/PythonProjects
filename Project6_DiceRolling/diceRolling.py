"""
Name: David Montanez
Reason: Hello World
Created: July 7, 2021
Updated: July 9, 2021
"""

# possible feature of chooosing how many dices the user wants to roll

import random
import time

## Program
userChoice = "y"

def roll(sides, dices):
    if(dices == 1):
        diceOne = random.randint(1, sides)

        print(f"\nDice #1: {diceOne}")

    elif(dices == 2):
        diceOne = random.randint(1, sides)
        diceTwo = random.randint(1, sides)

        print(f"\nDice #1: {diceOne}\nDice #2: {diceTwo}")
        print(f"You rolled an {diceOne + diceTwo}!!")

while userChoice == "y":

    diceSides = int(input("Number of Faces/Sides (4, 6, 8, 10, 12, 20): "))
    numberOfDices = int(input("Number of Dices (1 or 2): "))

    print("Dice is rolling...")
    time.sleep(1)

    roll(diceSides, numberOfDices)
    time.sleep(2)

    userChoice = input("\nDo you want to roll again? (y/n): ").lower().strip()

print("Thank you for playing :)")