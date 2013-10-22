# Josh Gladstone
# Section B04
# marquis.gladstone@gatech.edu / GTID: 902985753
"""I worked on the homework assignment with the help of StackOverflow (only for the string
formatting used in the function rorherIndex, line 42) and this semester's course materials. The
url used for the string formatting is:
http://stackoverflow.com/questions/455612/python-limiting-floats-to-two-decimal-points"""

import math

def celciusToFahrenheit():
    c = input("Enter the temperature in degrees Celcius")
    f = 9 * float(c) / 5 + 32

    print(f, "Degrees Fahrenheit")

def cylinderVolume():
    r = input("Please enter the radius (in inches) of the cylinder")
    h = input("Please enter the height (in inches) of the cylinder")
    v = math.pi * float(r)**2 * float(h)

    print("The volume of the cylinder is", int(v) , "inches-cubed.")

def timeCleanUp():
    s = input("Please enter the number of seconds you wish you convert")
    remWeeks = int(s) % 604800
    remDays = int(s) % 86400
    remMinutes = int(s) % 3600
    seconds = int(s) % 60
    minutes = int(remMinutes) / 60
    hours = int(remDays) / 3600
    days = int(remWeeks) / 86400
    weeks = int(s) / 604800


    print(int(weeks), "weeks", int(days), "days", int(hours), "hours", int(minutes),
          "minutes", int(seconds), "seconds")

def rohrerIndex():
    weight = input("Please enter your weight(in pounds)")
    height = input("Please enter your height(in inches)")
    ri = int(weight) / int(height)**3 * 2768

    print("Your RI is", "{0:.2f}".format(ri), ".")