"""
Name: David Montanez
Reason: Hello World
Created: July 7, 2021
Updated: July 7, 2021
"""

# Small and simple adventure
## Program
promptStart = input("Would you like to play? (yes/no): ")

if(promptStart.lower().strip() == "yes"):

    promptStart = input("You have reached a crossroad. Would you like to go left (L) or right (R)?: ").lower().strip()

    if(promptStart == "left"):
        promptStart = input("You have encountered a monster. Would you like to run (R) or attack (A)?: ").lower().strip()

        if(promptStart == "a"):
            print("The monster was stronger than you. You lost!")
        elif(promptStart == "r"):
            print("You outran the monster! You made it away safely.")

            promptStart = input("You have come across a stripway. Would you like to use the car (C) or the airplane (A)?: ").lower().strip()

            if(promptStart == "c"):
                print("Unfortunately the car doesn't have any fuel...")
                print("The monster has now caught up and has killed you... You Lost!")
                raise SystemExit
            elif(promptStart == "a"):
                print("You have now escaped the city. You Won!")



    elif(promptStart == "right"):
        print("You came across a trap! You Lost!")
        raise SystemExit
else:
    print("That's too bad :(")