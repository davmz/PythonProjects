"""
Name: David Montanez
Reason: Hello World
Created: July 7, 2021
Updated: July 7, 2021
"""

import random

## Program
def play():
    print("Welcome to Rock Paper Scissors! What will be your choice?")
    user = input("(R) for rock - (P) for paper - (S) for scissors: ").upper().strip()
    computer = random.choice(["R", "P", "S"])

    print(f"\nYou: {user} VS. Computer: {computer}")

    if(user == computer):
        print(f"{user} is the same as {computer}! It's a draw!")
    
    if isWin(user, computer):
        print(f"{user} beats {computer}. You Win!")
    else:
        print(f"{computer} beats {user}. You Lost!")

def isWin(player, opponent):
    if(player == "R" and opponent == "S") or (player == "S" and opponent == "P") \
        or (player == "P" and opponent == "R"):
        return True
    else:
        return False

play()

# def play():
#     print("What's your choice?")
#     user = input("(R) for rock - (P) for paper - (S) for scissors: ").lower().strip()
#     computer = random.choice(["r", "p", "s"])

#     if(user == computer):
#         return "It's a Tie!"

#     # r > s, s > p, p > r
#     if isWin(user, computer):
#         return "You Won!"

#     return "You Lost!"

# def isWin(player, opponent):
#     # return true if player wins
#     # r > s, s > p, p > r
#     if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
#         or (player == "p" and opponent == "r"):
#         return True

# print(play())