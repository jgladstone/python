#Josh Gladstone
#Section B4
#marquis.gladstone@gatech.edu / 902985753
#I worked on this assignment alone using only the assigned course materials.

import string

def passOrNot(grade):
    if grade >= 70 and grade <= 100:
        return "Congratulations. You passed!"
    elif grade < 70 and grade >= 0:
        return "Sorry. You must have at least 70% to pass. See you next semester."

def modulusFour(start):
    if start > 0:
        print(start)
        n = start - 4
        start = n
        modulusFour(start)
    elif start < 0:
        print("The remainder is the number shown above.")

def letterSpace(s):
    index = 0
    while index < len(s):
        letter = s[index]
        if letter in string.letters:
            print(letter, end="")
        else:
            print(" ", end="")
        index = index + 1


def complimentMaker(answer1,answer2,answer3,answer4):
    sentence = "You are"
    if answer1 == False and answer2 == False and answer3 == False and answer4 == False:
        return "No comment"
    if answer1 == True:
        ans1 = " super"
    else:
        ans1 = ""
    if answer2 == True:
        ans2 = " nice"
    else:
        ans2 = ""
    if answer3 == True:
        ans3 = " smart"
    else:
        ans3 = ""
    if answer4 == True:
        ans4 = " cool"
    else:
        ans4 = ""

    return sentence + ans1 + ans2 + ans3 + ans4 + "."

def wordMesh(wordA,wordB):
    place = 0
    word = ""
    while place < len(wordA):
        word = word + (wordA[place]) + (wordB[place])
        place = place + 1
    return word

def replaceWord(oldWord,newWord,aStr):
    print(aStr.replace(oldWord,newWord))

def numMountainRange(x):
    start = 1
    row = 3
    space = " "
    while start <= x and 2 <= x <= 9:
        gap = (space * (x - int(start)))
        print(str(start) + gap + (int(row)- 2) * str(start) + gap + str(start))
        start = int(start) + 1
        row = row + 2

def print10table():
    r = 0
    print("Times:\t 10\t 20\t 30\t 40\t 50\t 60\t 70\t 80\t 90\t 100")
    r = r + 1
    while r <= 10:
        print((r * 10),"\t",(r * 10) * 10,"\t",(r * 10) * 20,"\t",(r * 10) * 30,"\t",(r * 10) * 40,"\t",(r * 10) * 50,"\t",(r * 10) * 60,"\t",(r * 10) * 70,"\t",(r * 10) * 80,"\t",(r * 10) * 90,"\t",(r * 10) * 100)
        r = r + 1

#def printTimes(N, inc):
