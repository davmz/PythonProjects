"""
Name: David Montanez
Reason: Login System
Created: July 16, 2021
Updated: July 16, 2021
"""

import time
import hashlib
import os
clear = lambda: os.system("cls")

## Program
# Displays the Main Menu of the Login System page
def mainMenu():
    clear()
    print("Welcome to the Main Menu of the Login System! :)\n")
    print("A) Register a new account")
    print("B) Login to your account")

    while True:
        userChoice = input("What would you like to do? (A/B): ").upper()

        if userChoice in ["A", "B"]:
            break
    
    if(userChoice == "A"):
        register()
    else:
        login()

# Displays the Register page with its attributes and functions
def register():
    clear()
    print("Register Your Account!\n")

    while True:
        userName = input("Enter a Username: ")

        if(userName != ""):
            break

    userName = sanitizeName(userName)

    while True:
        userPassword = input("Enter a Password: ")

        if(userPassword != ""):
            break

    while True:
        confirmPassword = input("\nConfirm Your Password: ")

        if(confirmPassword == userPassword):
            break
        else:
            print("Passwords Don't Match!")
    
    if(accountAlreadyExists(userName, userPassword)):
        while True:
            registerError = input("You Are Already Registered!\n\nPress (T) to Try Again...\nPress (L) to Login...\nWhat would you like to do? (T/L): ").upper()

            if(registerError == "T"):
                register()
                break
            elif(error == "L"):
                login()
                break
            else:
                print("\nInvalid Character Input. Please Try Again!")
    addAccountInfo([userName, hashPassword(userPassword)])

    print("\nYou are now Registered!!")
    time.sleep(2)

    mainMenu()

# Displays the Login page with its attributes and functions
def login():
    clear()
    print("Login to Your Account!\n")

    accountInfo = {}
    with open("./Project14_LoginSystem/accountSystem.txt", "r") as file:
        for line in file:
            line = line.split()
            accountInfo.update({line[0]: line[1]})

    while True:
        userName = input("Enter Your Name: ")
        userName = sanitizeName(userName)
        if userName not in accountInfo:
            print("\nYou Are Not Registered!")
        else:
            break

    while True:
        userPassword = input("\nEnter Your Password: ")
        if not checkhashPassword(userPassword, accountInfo[userName]):
            print("Incorrect Password!")
        else:
            break

    print("\nYou have now Logged In!!")
    time.sleep(1)
    account()

def account():
    clear()
    print("Welcome to Your Account!")
    print("A) Change Your Username")
    print("B) Change Password")
    print("C) Logout")

    while True:
        userChoice = input("What would you like to do? (A/B/C): ").upper()

        if(userChoice in ["A", "B", "C"]):
            break

    if(userChoice == "A"):
        changeUserName()
    elif(userChoice == "B"):
        changeUserPassword()
    elif(userChoice == "C"):
        print("\nLogging Out...")
        time.sleep(1)
        raise SystemExit

def changeUserName():
    pass

def changeUserPassword():
    pass
 
# Adds the account in the txt file
def addAccountInfo(userInfo: list):
    with open("./Project14_LoginSystem/accountSystem.txt", "a") as file:
        for info in userInfo:
            file.write(info)
            file.write(" ")
        file.write("\n")

# Checks the txt file if the account already exists
def accountAlreadyExists(userName, userPassword):
    userPassword = hashPassword(userPassword)
    accountInfo = {}
    with open("./Project14_LoginSystem/accountSystem.txt", "r") as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1] == userPassword:
                accountInfo.update({line[0]: line[1]})
    if accountInfo == {}:
        return False
    return accountInfo[userName] == userPassword

def sanitizeName(userName):
    userName = userName.split()
    userName = "-".join(userName)
    return userName

# Applies protection and security of the password of the user's account
def hashPassword(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def checkhashPassword(password, hash):
    return hashPassword(password) == hash

if __name__ == "__main__":
    mainMenu()