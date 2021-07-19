"""
Name: David Montanez
Reason: Website Blocker
Created: July 17, 2021
Updated: July 17, 2021
"""

import time
from datetime import datetime as dt

## Program
blockedWebsites = [
    "www.facebook.com",  "facebook.com",  
    "www.youtube.com", "youtube.com", # Does not work
    "www.gmail.com", "gmail.com"
]

windowHost = r"C:\Windows\System32\drivers\etc\hosts"
defaultHost = windowHost
redirect = "127.0.0.1"

def websiteBlocker():
    startHour = input("\nStarting Hour: (0 to 24):")
    endHour = input("Starting Hour: (0 to 24):")

    if dt(dt.now().year, dt.now().month, dt.now().day,startHour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,endHour): 
        print("Do the work ....")

        with open(defaultHost, "r+") as hostfile:
            hosts = hostfile.read()

            for site in  blockedWebsites:
                if site not in hosts:
                    hostfile.write(redirect + " " + site + "\n")
    else:
        with open(defaultHost, "r+") as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)

            for host in hosts:
                if not any(site in host for site in blockedWebsites):
                    hostfile.write(host)
            hostfile.truncate()

        print("Good Time")
    time.sleep(3)

if(__name__ == "__main__"):
    websiteBlocker()