"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 19, 2021
"""

import os
clear = lambda: os.system("cls")

## Program
def leapYear():
    clear()
    print("Welcome to Leap Year Checker!")
    print("Input a year and check if that year is a leap year or not.\n")
    userPrompt = "Y"

    try:
        while(userPrompt == "Y"):
            userYear = int(input("Input Year: "))
            leapYear = isLeapYear(userYear)

            if(leapYear == True):
                print(f"{userYear} is a Leap Year!")
            else:
                print(f"{userYear} is not Leap Year!!")

            userPrompt = input("\nDo you want to try another year? (Y/N): ").upper()
            clear()

    except:
        print("\nPlease input a valid year!!")

# Checks if the year is a leap year
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

if(__name__ == "__main__"):
    leapYear()