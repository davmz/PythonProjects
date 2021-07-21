"""
Name: David Montanez
Reason: Website Blocker
Created: July 20, 2021
Updated: July 20, 2021
"""

## Video
# https://www.youtube.com/watch?v=H8t4DJ3Tdrg&t=259s&ab_channel=PyTutorials

## Install
# cryptography => python -m pip install cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import os
clear = lambda: os.system("cls")

import base64

## Program
# def encryptMessage():
#     ## Get Key From File 
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()

#     ## Encode Message
#     message = input("Enter your message: ")
#     encodedMessage = message.encode()

#     ## Encrypt The Message
#     f = Fernet(key)
#     encrypted = f.encrypt(encodedMessage)
#     print(encrypted)

# def decryptMessage():
#     ## Get Key From File
#     file = open("key.key", "rb") 
#     key2 = file.read()
#     file.close()

#     ## Decrypt the encrypted message
#     f2 = Fernet(key)
#     decryptedMessage = decryptedMessage = f2.decrypt(encrypted)

#     ## Decode the message
#     originalMessage = decryptedMessage.decode()
#     print(originalMessage)

# def passwordEncryptionKey():
#     providePassword = input("Enter password for encryption: ")
#     password = providePassword.encode()
#     salt = b'\xe2\xacAz\x0b\x7f8\x82\x85\xc5?\x9d\x8c\tg\xe9' # os.urandom(16)

#     kdf = PBKDF2HMAC(
#         algorithm = hashes.SHA256(),
#         length = 32,
#         salt = salt,
#         iterations = 100000,
#         backend = default_backend()
#     )

#     key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

# def encrypt():
#     ## Generate Random Key
#     # Byte object base64 encoded string
#     key = Fernet.generate_key()
#     print(key)

#     ## Save Key To Txt File
#     file = open("key.key", "wb")
#     file.write(key) # Key is type bytes
#     file.close()

#     ## Open Key From Txt File
#     file = open("key.key", "rb")
#     key = file.read() # Key will be type bytes
#     file.close()
#     print(key)

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