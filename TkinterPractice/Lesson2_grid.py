"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 19, 2021
"""

## Everything is a widget
from tkinter import *

## Happens at the start of your program
root = Tk()

## Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "My Name is David Montanez").grid(row = 1, column = 0)

## Display onto the screen
# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 0)

root.mainloop()