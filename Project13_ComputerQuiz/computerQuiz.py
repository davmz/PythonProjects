"""
Name: David Montanez
Reason: YouTube MP4 Downloader
Created: July 12, 2021
Updated: July 16, 2021
"""

import random

## Program
print("Welcome to the Computer Quiz Game!!")
print("Answer these sets of questions and get your final grade at the end!")
score = 0

# Question #1
userAnswers = input(f"\nWhat does CPU stand for?: ")
if(userAnswers == "central processing unit"):
    print("You are correct!!")
    score += 1
else:
    print("You are incorrect!!")

# Question #2
userAnswers = input(f"\nWhat does RAM stand for?: ")
if(userAnswers == "random access memory"):
    print("You are correct!!")
    score += 1
else:
    print("You are incorrect!!")

# Question #3
userAnswers = input(f"\nWhat does GPU stand for?: ")
if(userAnswers == "graphic processing unit"):
    print("You are correct!!")
    score += 1
else:
    print("You are incorrect!!")

# Question #4
userAnswers = input(f"\nWhat does PSU stand for?: ")
if(userAnswers == "power supply unit"):
    print("You are correct!!")
    score += 1
else:
    print("You are incorrect!!")

print("\nCongratulations! You have finished the quiz!")
print(f"You scored {score} out of 4!!")