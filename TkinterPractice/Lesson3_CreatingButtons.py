"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 19, 2021
"""

# https://www.tutorialspoint.com/python/tk_button.htm

## Everything is a widget
from tkinter import *


def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!!")
    myLabel.pack()

## Happens at the start of your program
root = Tk()

## Creating a Button Widget
myButton = Button(root, text = "Click Me!", padx= 50, pady = 50, command = myClick, bg = "orange", fg = "blue")

## Display onto the screen
myButton.pack()

root.mainloop()