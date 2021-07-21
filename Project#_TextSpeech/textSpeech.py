"""
Name: David Montanez
Reason: Hello World
Created: July 21, 2021
Updated: July 21, 2021
"""

## Packages
# pip install pipwin => PyAudio download errors
# pip install wheel => needed to download PyAudio package
# pipwin install pyaudio or pip install PyAudio
# https://stackoverflow.com/questions/53866104/pyaudio-failed-to-install-windows-10

## Imports
import os
clear = lambda: os.system("cls")

# pip install SpeechRecognition
import speech_recognition as sr

# pip install pyttsx3
import pyttsx3

# pip install python-vlc

## Program 
def speech():
    recognizer = sr.Recognizer()
    voiceEngine = pyttsx3.init()
    voiceEngine.setProperty("rate", 190)

    # voiceEngine.say("I am Jarvis. Your AI Helper!")
    # voiceEngine.say("How can I help you?")
    # voiceEngine.runAndWait()

    while True:
        try:
            with sr.Microphone() as source:
                
                recognizer.adjust_for_ambient_noise(source, duration = 0.2)
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(text)

                if("hey google" in text):
                    voiceEngine.say("How can I help you... Question mark!")
                    voiceEngine.runAndWait()

                if("my name is" in text):
                    name = text.split()
                    voiceEngine.say(f"Your name is {name[-1]}")
                    voiceEngine.runAndWait()

                if("clap" in text):

                
                voiceEngine.say(text)
                voiceEngine.runAndWait()
        except:
            recognizer = sr.Recognizer()
            continue

def test():
    recognizer = sr.Recognizer()
    voiceEngine = pyttsx3.init()
    voiceEngine.setProperty("rate", 190)

    voiceEngine.say("I am Jarvis. Your AI Helper!")
    voiceEngine.say("How can I help you?")
    voiceEngine.runAndWait()

    voice = voiceEngine.getProperty("voices")
    for i in voice:
        print(i)

    # while True:
    #     try:
    #         with sr.Microphone() as source:
                
    #             recognizer.adjust_for_ambient_noise(source, duration = 0.2)
    #             audio = recognizer.listen(source)

    #             text = recognizer.recognize_google(audio)

    #             print(text)
    #     except:
    #         recognizer = sr.Recognizer()
    #         continue

if(__name__ == "__main__"):
    speech()
    # test()

