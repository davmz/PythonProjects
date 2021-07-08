"""
Name: David Montanez
Reason: Hello World
Created: July 7, 2021
Updated: July 7, 2021
"""

import json
import os

# # string concatenation (aka how to put strings together)

# ## Introduction: create a string => "My name is ____"
# name = "David Montanez"

# # Few ways to do this:
# print("My name is " + name)
# print("My name is {}".format(name))
# print(f"My name is {name}\n")

# ## Program:
# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# person = input("Person: ")

# mablib = f"Computer programming is so {adj}!\n It makes me so excited all the time because \
# I love to {verb1}.\n Stay hydrated and {verb2} like you are {person}!"

# print(mablib)

## Program:
class MadLibs:
    path = ".\\templates"
    def __init__(self, wordDescriptions, template):
        self.template = template
        self.wordDescriptions = wordDescriptions
        self.userInput = []
        self.story = None

    @classmethod
    def fromJSON(cls, name, path = None):
        if not path:
            path = cls.path
        filePath = os.path.join(path, name)

        with open(filePath, "r") as f:
            data = json.load(f)

        madLib = cls(**data)

        return madLib

    def getWordsFromUser(self):
        print("Please provide the following words: ")

        for desc in self.wordDescriptions:
            ui = input(desc + ": ")
            self.userInput.append(ui)

        return self.userInput

    def buildStory(self):
        self.story = self.template.format(*self.userInput)

        return self.story

    def show_story(self):
        print(story)

def selectTemplate():
    print("Select a Mad Lib from the following list: ")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template

templateName = selectTemplate()
madlib = MadLibs.fromJSON(templateName)
words = madlib.getWordsFromUser()
story = madlib.buildStory()
madlib.show_story()