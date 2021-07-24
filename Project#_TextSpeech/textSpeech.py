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

# pip install playsound
from playsound import playsound

## Program 
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 190)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print("Listening...")

            listener.adjust_for_ambient_noise(source, duration = 0.2)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if("hey jarvis" in command):
                engine.say("How can I help you... Question mark!")
                engine.runAndWait()

                command = command.replace("hey jarvis", "")
                print(command)
    except:
        pass
    return command

def runJarvis():
    command = takeCommand()
    print(command)

    if("poop" in command):
        engine.say("POOOOOP")
        engine.runAndWait()
    # elif(command == "hey jarvis clap"):
    #     playsound(".\\Project#_commandSpeech\\clap.mp3", True)
    # elif("my name is" in command):
    #     name = command.split()
    #     engine.say(f"Your name is {name[-1]}")
    #     engine.runAndWait()
    # else:
    #     talk("I did not get that...")


if(__name__ == "__main__"):
    while True:
        runJarvis()