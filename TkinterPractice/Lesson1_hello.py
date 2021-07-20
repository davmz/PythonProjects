"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 19, 2021
"""

# Everything is a widget
from tkinter import *

# Happens at the start of your program
root = Tk()

# Creating a Label Widget
myLabel = Label(root, text = "Hello World!")

# Display onto the screen
myLabel.pack()

root.mainloop()