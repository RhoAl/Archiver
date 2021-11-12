import json
import sqlite3
import requests
from flask import Flask
from PIL import Image
#import ImageTransformerService

#To Add:
#A method that lets the user redefine entries in the dictionary

#Dictionary containing all of the import information
archive = {
    "StringBool" : False,
    "FloatBool" : False,
    "FloatProperty" : None,
    "StringPropery" : None,
    "Picture" : None
}

app = Flask(__name__)
filename = "save.json"  #Filename of the external save file
archiveList = []    #List of dictionaries


def add(sBool, fBool, num, string):
    """Adds an item to archiveList"""
    picture = "None"
    print("Do you want to add an image? Yes or no? ")
    ans = input()
    firstChar = ans[0].upper()
    if (firstChar == 'Y'):
        picture = picAdd(picture)
    archiveList.append({"StringBool":sBool, "FloatBool":fBool, "FloatProperty":num, "StringProperty":string, "Picture" : picture})


def delete():
    """Deletes an item from archiveList; for right now it just pops it like a stack"""
    archiveList.pop()


def picAdd(picture):
    """Adds an image file name to the name section of the archive dictionary"""
    #I'll need to add funtionallity that allows it to check if the picture exists
    print("Please insert the file name: ")
    picture = input()
    return picture


#######
# Edit this later to add more practical funtionality.
# This was initially created to just test out something.
#######
#def picDisplay(archive):
#    """Displays a picture"""
#    if (archive["Picture"] == "Sandwich.jpg"):
#        img = Image.open("Sandwich.jpg")
#        img.show()
#        #ImageTransformerService.transform()


def display():
    """Outputs the list of dictionaries"""
    count = len(archiveList)
    for count in archiveList:
        print(count)
        #picDisplay(count)  


def saveFile():
    """Saves an external JSON file"""
    with open(filename, 'w') as file:
        json.dump(archiveList, file)
        print("File successfully saved\n")


def loadFile():
    """Loads an external JSON file"""
    try:
        with open(filename) as file:
            archiveList = json.load(file)
            print("File successfully opened\n")
    except FileNotFoundError:
        print("No file has been loaded\n")


def editStringBool():
    """Asks what the user would like to set the string bool as"""
    sBoolLoop = True
    while (sBoolLoop == True):
        print("\nIs there a string?\n")
        ans = input("Enter either Yes or No: ")
        firstChar = ans[0].upper()
        if (firstChar == 'Y'):
            return True
            sBoolLoop = False   #Doesn't actually do anything, but it seems prudent to do this
        elif(firstChar == 'N'):
            return False
            sBoolLoop = False
        else:
            print("Only Yes or No answers are allowed\n")


def editFloatBool():
    """Asks the user if they want to set the float bool as"""
    fBoolLoop = True
    while (fBoolLoop == True):
        print("\nIs there a number?\n")
        ans = input("Enter either Yes or No: ")
        firstChar = ans[0].upper()
        if (firstChar == 'Y'):
            return True
            fBoolLoop = False   #Doesn't actually do anything, but it seems prudent to do this
        elif(firstChar == 'N'):
            return False
            fBoolLoop = False
        else:
            print("Only Yes or No answers are allowed\n")


def addFloat():
    """Adds to the float"""
    num = input("Enter a number: ")
    return num


def addString():
    """Adds to the string"""
    string = input("Enter your text: ")
    return string


#########
#Main
#########

#Initializing variables
checkLoop = True    #Used to check if a loop should keep going, or stop
sBool = False
fBool = False
num = None
string = None

loadFile()

#Adding to the archive
while (checkLoop == True):
    print("\nSelect an Option\n")
    print("1 - Add to the archive\n")
    print("2 - Delete from the archive\n")
    print("3 - Display the archive\n")
    print("4 - Quit\n")
    ans = input("Enter Option: ")
    if (ans == '4'):
        checkLoop = False
    elif (ans == '1'):
        sBool = editStringBool()
        fBool = editFloatBool()
        if (fBool == True):
            num = addFloat()
        if (sBool == True):
            string = addString()

        if (fBool == False and sBool == False):
            print("Error! You have to have at least one item to add\n")
        else:
            add(sBool, fBool, num, string)
    elif (ans == '2'):
        delete()
    elif (ans == '3'):
        display()
    else:
        print("Error! Option out of range\n")

saveFile()