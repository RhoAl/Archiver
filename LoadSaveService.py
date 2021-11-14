import json

#To anyone reviewing this, please tell me where comments would be helpful

#I use the same name for the local variables of methods and the global variables declared after methods, if they have the same function.
#I'm not sure if this keeps consistency, or if it's just confusing.

#toSave = {}

def importSave():
    """Imports a save from another program"""
    filename = input("Please enter the name of the file you want to read: ")
    try:
        with open(filename) as file:
            copy = json.load(file)
            print("File successfully opened\n")
            return True, copy
    except FileNotFoundError:
        print("No file has been loaded\n")
        return False, False


def display():
    """Outputs the content of the file"""
    #for key in toSave:
    print(toSave)


def saveDict():
    """Adds data to the loaded-in dictionary"""
    category = input("Enter the category for the item: ")
    item = input("Enter the name of the item: ")
    toSave[category] = item
    return toSave


def deleteDict():
    """Deletes data from the dictionary"""
    #This currently works by removing the first category that matches the user inputted key
    #If I have time, I'll try to implement a system where the user can delete on a case by case basis
    catRemove = input("Enter the category you want to remove: ")
    removeKey = toSave.pop(catRemove, None)
    if (removeKey == None):
        print("Item could not be found\n")
    else:
        print(catRemove, "has been successfully removed\n")
        return toSave


def askDict():
    """Asks if the user would like to edit their save file"""
    checkLoop = True
    while (checkLoop == True):
        print("\nWould you like to add to a save file?\n")
        ans = input("Enter \"Yes\" or \"No\": ")
        firstChar = ans[0].upper()
        if (firstChar == 'Y'):
            toSave = saveDict()
        else:
            checkLoop = False

    checkLoop = True
    while (checkLoop == True):
        print("Would you like to remove from the save file?\n")
        ans = input("Enter \"Yes\" or \"No\": ")
        firstChar = ans[0].upper()
        if (firstChar == 'Y'):
            toSave = deleteDict()
        else:
            checkLoop = False

    return toSave


def exportSave(toSaveS):
    """Exports the saved file"""
    filename = input("Please enter the name of the file you want to write to: ") 
    with open(filename, 'w') as file:
        json.dump(toSave, file)
        print("File successfully saved\n")


#Main Program

#I'm not sure if it's good or bad coding practice to initialize variables in Python; It might make it more readible, even if it's pointless in terms of making the program run.
checkLoop = True    #Used to determine if a loop should keep looping
checkFile = (False, False)   #Used to determine if a file has been properly loaded
ans = ""    #Used for all answers the user wants to input
firstChar = ""  #Used to contain the first character of the ans string

while (checkLoop == True):
    print("\nWould you like to edit a save file?\n")
    ans = input("Enter \"Yes\" or \"No\": ")
    firstChar = ans[0].upper()
    
    if (firstChar == 'N'):
        checkLoop = False
    elif (firstChar == 'Y'):
        toSave = {}
        checkFile = importSave()
        if (checkFile[0] == True):
            toSave = checkFile[1]
            toSave = askDict()
            exportSave(toSave)
            checkLoop = True    #Not necessary, but it seems prudent to set it to true; in more complicated programs, this would likely just increase runtime
    else:
        print("Please enter only yes or no answers\n")