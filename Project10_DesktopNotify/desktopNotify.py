"""
Name: David Montanez
Reason: Pomodoro Timer 
Created: July 10, 2021
Updated: July 10, 2021
"""

# https://docs.python.org/3/library/time.html
import time

# https://plyer.readthedocs.io/en/latest/#plyer.facades.Notification
from plyer import notification # pip install plyer

## Program
# feel free to make any changes of your choice
# the title of your notification
title = "Hey David, take a break now!!" 

# the message of your notification
message = "Take a 5 minute break (25-5 ratio)."

# notification timer (seconds) 
timer = 10

def notify(title, message):
    notification.notify(
        title = title, 
        message = message, 

        ## Icon used for the notification
        # https://iconarchive.com/show/100-flat-icons-by-graphicloads/clock-icon.html
        app_icon = "clock.ico", # ico formatted image used

        timeout = 10, # how long the notification is displayed on desktop in seconds
    )

if __name__ == "__main__":
    while True:
        notify(title, message)
        time.sleep(timer)