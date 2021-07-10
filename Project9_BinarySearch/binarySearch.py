"""
Name: David Montanez
Reason: Hello World
Created: July 9, 2021
Updated: July 9, 2021
"""

import random
import time

## Program
# Naive Search: scans entire list and checks if each item is equal to the target
def naiveSearch(l, target):
    for i in range(len(l)):
        if(l[i] == target):
            print(i)
    return -1

# Binary Search: uses divide and conquer for faster results
def binarySearch(l, target, low = None, high = None):
    # Decide to search above/below the midpoint
    if(low == None):
        low = 0
    if(high == None):
        high = len(l) - 1

    # If target is not in the list
    if(high < low):
        return -1

    midPoint = (low + high) // 2
    
    if(l[midPoint] == target): # item equals target
        return midPoint
    elif(target < l[midPoint]):
        return binarySearch(l, target, low, midPoint - 1)
    else:
        return binarySearch(l, target, midPoint + 1, high)

lists = [1, 3, 5, 10, 20, 4]
target = 20

naiveSearch(lists, target)
binarySearch(lists, target)

## Test the timer of each search
# if __name__ == "__main__":
#     print(naiveSearch(list, target))
#     print(binarySearch(list, target))

    ## Compare time for different time of searching method
    # length = 10000
    # sortedList = set()
    # while len(sortedList) < length:
    #     sortedList.add(random.randint(-3 * length, 3 * length))
    # sortedList = sorted(list(sortedList))

    # start = time.time()
    # for target in sortedList:
    #     naiveSearch(sortedList, target)
    # end = time.time()
    # print("Naive search time: ", (end - start)/length, " seconds")

    # start = time.time()
    # for target in sortedList:
    #     binarySearch(sortedList, target)
    # end = time.time()
    # print("Binary search time: ", (end - start)/length, " seconds")