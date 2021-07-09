"""
Name: David Montanez
Reason: Hello World
Created: July 9, 2021
Updated: July 9, 2021
"""

# NEXT: User Prompt for playing the game again/exiting

import random
import string

# Where the words are stored in a .py file
from WordsDictionary import words

## Program
def getRandomWord(words):
    word = random.choice(words)

    return word.upper()

def hangman():
    word = getRandomWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessedLetters = set()
    lives = 6

    while len(wordLetters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: ", " ".join(guessedLetters))

        wordList = [letter if letter in guessedLetters else "_" for letter in word]
        print("\nCurrent word: ", " ".join(wordList))

        userLetter = input("\nGuess a letter: ").upper()

        if(userLetter in alphabet - guessedLetters):
            guessedLetters.add(userLetter)

            if(userLetter in wordLetters):
                wordLetters.remove(userLetter)
            else:
                lives -= 1
                print(f"{userLetter} is not in the word.")

        elif(userLetter in guessedLetters):
            print("You have already guessed that letter. Please try again...")
        else:
            print("Invalid Letter!")

    if(lives == 0):
        print("\nSorry, you have died!")
        print(f"The word was {word}")
    else:
        print("\nYou have guessed the word.")
        print(f"The word was {word}!!")

hangman()