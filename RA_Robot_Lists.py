#Josh Gladstone
#marquis.gladstone@gatech.edu / 902985753
#Section B4
#I worked on this assignment alone, using nothing but the course materials.


from Myro import *

init('sim')

def getValues(numSamples):
    value = []
    for x in range(0,numSamples):
        turnLeft(1,0.25)
        value.append(getLight('center'))
    return value


def printStatistics(nums):
    length = len(nums)
    start = 0
    total = 0
    while start < length:
        total = total + nums[start]
        start = start + 1

    average = total / length
    nums.sort()
    smallest = nums[0]
    end = length - 1
    largest = nums[end]
    even = 0
    for x in range(0,length):
        if x % 2 == 0:
            even = even + 1

    print("You gave me a list of " + str(length) + " numbers. The average was " + str(average) + ". The largest was " + str(largest) + ". The smallest was " + str(smallest) + ". Only " + str(even) + " of them were even numbers.")
