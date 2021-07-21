"""
Name: David Montanez
Reason: Hello World
Created: July 21, 2021
Updated: July 21, 2021
"""

## Packages
# pip install pipwin => PyAudio download errors
# pip install wheel => needed to download PyAudio package
# pipwin install pyaudio
# https://stackoverflow.com/questions/53866104/pyaudio-failed-to-install-windows-10

## Imports
# pip install SpeechRecognition

# pip install pyttsx3



# pip install PyAudio

## Program 
def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Anything: ")
        audio = r.listen(source)

        text = r.recognize_google(audio)

        print(text)


if(__name__ == "__main__"):
    speech()

