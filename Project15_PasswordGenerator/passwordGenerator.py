"""
Name: David Montanez
Reason: Random Password Generator
Created: July 17, 2021
Updated: July 17, 2021
"""

import os
clear = lambda: os.system("cls")

import time
import string
import random

## Program
def main():
    clear()
    print("Welcome to Password Generator!!")
    print("Please enter in integer values (1 to 100) to generate your random password!")
    userPrompt = "Y"

    try:
        while(userPrompt == "Y"):
            while True:
                uppercase = int(input("\nNumber of UpperCase(s): "))

                if(uppercase in range(1, 100)):
                    break
            
            while True:
                lowercase = int(input("Number of LowerCase(s): "))

                if(lowercase in range(1, 100)):
                    break

            while True:
                digits = int(input("Number of Digit(s): "))

                if(digits in range(1, 100)):
                    break
            
            while True:
                punctuation = int(input("Number of Punctuation(s): "))

                if(punctuation in range(1, 100)):
                    break

            randomPassword(uppercase, lowercase, digits, punctuation)

            userPrompt = input("Generate another password? (Y/N): ").upper()
            clear()

        print("\nThank you for saving your accounts!")

    except:
        print("\nPlease enter in a integer value!!")

# Generates a random password with different number of characters specified by the user.
def randomPassword(uppercase, lowercase, digits, punctuations):
    alphabetUpperCase = "".join(random.choice(string.ascii_uppercase) for i in range(uppercase))
    alphabetLowerCase = "".join(random.choice(string.ascii_lowercase) for i in range(lowercase)) 
    digit = "".join(random.choice(string.digits) for i in range(digits)) 
    punctuation = "".join(random.choice(string.punctuation) for i in range(punctuations)) 

    passwordCharacters = alphabetLowerCase + alphabetUpperCase + digit + punctuation
    randomizedPassword = random.sample(passwordCharacters, len(passwordCharacters))
    password = "".join(randomizedPassword)

    print(f"\nRandom Password: {password}")

if(__name__ == "__main__"):
    main()