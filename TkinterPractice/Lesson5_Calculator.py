"""
Name: David Montanez
Reason: Website Blocker
Created: July 19, 2021
Updated: July 20, 2021
"""

from tkinter import *

## Program
root = Tk()
root.title("Simple Calculator")

entryField = Entry(root, width = 35, borderwidth = 5)
entryField.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 15)

def buttonClick(number):
    # entryField.delete(0, END)

    # Add numbers from the right not to the left
    current = entryField.get()
    entryField.delete(0, END)
    entryField.insert(0, str(current) + str(number))

def buttonClear():
    entryField.delete(0, END)

def buttonAdd():
    firstNumber = entryField.get()
    global firstNum
    global mathOperator
    mathOperator = "add"
    firstNum = int(firstNumber)

    entryField.delete(0, END)

def buttonSubtract():
    firstNumber = entryField.get()
    global firstNum
    global mathOperator
    mathOperator = "subtract"
    firstNum = int(firstNumber)

    entryField.delete(0, END)

def buttonMultiply():
    firstNumber = entryField.get()
    global firstNum
    global mathOperator
    mathOperator = "multiply"
    firstNum = int(firstNumber)

    entryField.delete(0, END)

def buttonDivide():
    firstNumber = entryField.get()
    global firstNum
    global mathOperator
    mathOperator = "divide"
    firstNum = int(firstNumber)

    entryField.delete(0, END)

def buttonEqual():
    secondNumber = entryField.get()
    entryField.delete(0, END)

    if(mathOperator == "add"):
        entryField.insert(0, firstNum + int(secondNumber))
    elif(mathOperator == "subtract"):
        entryField.insert(0, firstNum - int(secondNumber))
    elif(mathOperator == "multiply"):
            entryField.insert(0, firstNum * int(secondNumber))
    elif(mathOperator == "divide"):
        entryField.insert(0, firstNum / int(secondNumber))

## Creating a Button Widget
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: buttonClick(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: buttonClick(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: buttonClick(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: buttonClick(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: buttonClick(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: buttonClick(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: buttonClick(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: buttonClick(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: buttonClick(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: buttonClick(0))

# 
button_Add = Button(root, text = "+", padx = 39, pady = 20, command = buttonAdd)
button_Subtract = Button(root, text = "-", padx = 41, pady = 20, command = buttonSubtract)
button_Multiply = Button(root, text = "*", padx = 39, pady = 20, command = buttonMultiply)
button_Divide = Button(root, text = "/", padx = 39, pady = 20, command = buttonDivide)

button_Equal = Button(root, text = "=", padx = 86, pady = 20, command = buttonEqual)
button_Clear = Button(root, text = "Clear", padx = 77, pady = 20, command = buttonClear)

## Display Button on Screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)

button_Add.grid(row = 5, column = 0)
button_Subtract.grid(row = 6, column = 0)
button_Multiply.grid(row = 6, column = 1)
button_Divide.grid(row = 6, column = 2)

button_Equal.grid(row = 5, column = 1, columnspan = 2)
button_Clear.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()