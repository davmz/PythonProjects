import time 
import os
clear = lambda: os.system("cls")\

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
    print("Enter your message below:\n\n")
    message = input()
    encoded = message.encode()
    clear()

    print("\nGenerating Encryption Key...")
    time.sleep(2)
    
    print(f"\nEncryption Key: {generateKey()}")
    
    print("\nGenerating Encrypted Message...")
    time.sleep(2)

    messageEncryptionKey = Fernet(readKey())
    encryptedMessage = messageEncryptionKey.encrypt(encoded)

    file = open("message.txt", "wb")
    file.write(encryptedMessage)
    file.close()

    print(encryptedMessage)

def decryptMessage():
    clear()
    print("~~ Decrypt Your Message ~~\n")

    encryptionKey = readKey()
    fileName = input("Enter Message File: ")

    file = open(f"{fileName}", "rb")
    encryptedMessage = file.read()
    file.close()

    clear()
    print("Decrypting Message...")
    time.sleep(2)

    f2 = Fernet(encryptionKey)
    decryptedMessage = f2.decrypt(encryptedMessage)

    originalMessage = decryptedMessage.decode()
    print(f"\nDecrypted Message: \n\n{originalMessage}")

# Generates a random key for the encryption and decryption and saves it as a .key file.
def generateKey():
    key = Fernet.generate_key()

    file = open("key.key", "wb")
    file.write(key)
    file.close()
    
    return key

# Returns the key from the key.key file.
def readKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()

    return key

def generatePasswordKey():
    providePassword = input("Enter the password for the encrypted key: ")
    password = providePassword.encode()

    salt = b'\xfd\xf1\xa38\x0c\xccN1\xb0\xc8\x18f\x1bP\xd8Q'

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend = default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

if(__name__ == "__main__"):
    encrypt()