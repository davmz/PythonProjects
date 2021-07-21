"""
Name: David Montanez
Reason: Website Blocker
Created: July 20, 2021
Updated: July 20, 2021
"""

import base64
import os
clear = lambda: os.system("cls")

## Program
def encrypt():
    clear()
    print("Welcome to the Message Encryption Services!!")
    print("A) Encrypt a message")
    print("B) Decrypt a message")

    userPrompt = input("\nWhat would you like to do? (A/B): ").upper()

    if(userPrompt == "A"):
        encryptMessage()
    elif(userPrompt == "B"):
        decryptMessage()

def encryptMessage():
    clear()
    print("Provide the message you would like to encrypt: \n")
    messageToEncrypt = input()

    print(f"")

def decryptMessage():
    clear()
    print("Provide the encrypted message: \n")
    encryptedMessage = input()

    decryptionKey = input("Provide the encryption key to decrypt the message: ")

if(__name__ == "__main__"):
    encrypt()