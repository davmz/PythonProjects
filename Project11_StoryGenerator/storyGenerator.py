"""
Name: David Montanez
Reason: Generate a Random Story with User Input 
Created: July 10, 2021
Updated: July 10, 2021
"""

import random
import time

print("Enter words to build the story.")
mainCharacter = input("Main Character: ")
rivalName = input("Rival's Name: ")
activity = input("Activity/Event (ie Battle to the Death): ")

when = ["A long time ago", "Yesterday", "Before you were born", "In future", "Before Thanos arrived", "In a land long time ago"]
went = ["Arkham Asylum", "Gotham City", "Stark Tower", "Bat Cave", "Avengers HQ", "Hotel", "Motel"]

story = f"{random.choice(when)} {mainCharacter} went to {random.choice(went)} {activity}."
print(story)