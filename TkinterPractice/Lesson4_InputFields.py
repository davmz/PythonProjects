"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 19, 2021
"""

# https://www.tutorialspoint.com/python/tk_entry.htm

## Everything is a widget
from tkinter import *

## Happens at the start of your program
root = Tk()

entry = Entry(root, width = 50, bg = "blue")
entry.pack()
entry.insert(0, "Enter Your Name:  ")

def myClick():
    hello = f"Hello {entry.get()}"
    myLabel = Label(root, hello)
    # myLabel = Label(root, text = entry.get())
    myLabel.pack()

## Creating a Button Widget
myButton = Button(root, text = "Click Me!", padx= 50, pady = 50, command = myClick, bg = "orange", fg = "blue")

## Display onto the screen
myButton.pack()

root.mainloop()