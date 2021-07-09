"""
Name: David Montanez
Reason: Hello World
Created: July 8, 2021
Updated: July 8, 2021
"""

# string concatenation (aka how to put strings together)
## Introduction: create a string => "My name is ____"
name = "David Montanez"

# Few ways to do this:
# print("My name is " + name)
# print("My name is {}".format(name))
# print(f"My name is {name}\n")

## Program:
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
person = input("Person: ")

mablib = f"Computer programming is so {adj}!\n It makes me so excited all the time because \
I love to {verb1}.\n Stay hydrated and {verb2} like you are {person}!"

print(f"MadLib: {mablib}")