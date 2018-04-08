import turtle
myTurtle = turtle.Turtle()
#GET COMMAND FUNCTIONS
def getTurnCommand():
    angle = getIntegerInput("Enter the angle: ")
    return ('turn', angle)
def getForwardCommand():
    distance = getIntegerInput("Enter distance: ")
    return ('forward', distance)
def getShapeCommand():
    numSides = getIntegerInput("Enter the number of sides (3 or more): ")
    sideLength = getIntegerInput("Enter the length of each side: ")
    return ('shape', numSides, sideLength)
def getSnowflakeCommand():
    numSides = getIntegerInput("Enter the number of sides (3 or more): ")
    sideLength = getIntegerInput("Enter the length of each side: ")
    rotationAngle = getIntegerInput("Enter the rotation angle for each flake: ")
    return ('snowflake', numSides, sideLength, rotationAngle)
def getTextCommand():
    message = input("Enter the message to print: ")
    message = message.replace("\\n", "\n")
    return ('text', message)
def getPenupCommand():
    return ('penup',)   #Comma forces commandTuple to be a tuple
def getPendownCommand():
    return ('pendown',)   #Comma forces commandTuple to be a tuple
def getRecordCommand():
    return ('record',)  #Comma forces commandTuple to be a tuple
def getStopCommand():
    repeats = getIntegerInput("How many times should these commands repeat? ")
    return ('stop', repeats)
def getSaveCommand():
    filename = input("Enter the filename to which to save: ")
    return ('save', filename)
def getLoadCommand():
    filename = input("Enter the filename from which to load: ")
    return ('load', filename)
def getEndCommand():
    return ('end',) #Comma forces commandTuple to be a tuple

#EXECUTE COMMAND FUNCTIONS
def executeTurnCommand(commandTuple):
    myTurtle.right(commandTuple[1])
def executeForwardCommand(commandTuple):
    myTurtle.forward(commandTuple[1])
def executeShapeCommand(commandTuple):
    drawShape(commandTuple[1], commandTuple[2])
def executeSnowflakeCommand(commandTuple):
    drawSnowflake(commandTuple[1], commandTuple[2], commandTuple[3])
def executeTextCommand(commandTuple):
    myTurtle.write(commandTuple[1], True, font = ("Arial", 16, "normal"))
def executePenupCommand(commandTuple):
    myTurtle.penup()
    print("Pen up!")
def executePendownCommand(commandTuple):
    myTurtle.pendown()
    print("Pen down!")
def executeRecordCommand(commandTuple):
    global recording
    global recordList
    if not recording:
        print("Recording!")
        recordList.clear()
        recording = True
    else:
        print("You're already recording!")
def executeStopCommand(commandTuple):
    global recording
    recording = False
    print("Playing back " + str(len(recordList)) + " commands " + str(commandTuple[1]) + " times!")
    for _ in range(0, commandTuple[1]):
        for recordedCommand in recordList:
            executeCommand(recordedCommand)
def executeSaveCommand(commandTuple):
    save(commandTuple[1])
def executeLoadCommand(commandTuple):
    loadedCommands = load(commandTuple[1])
    for loadedCommand in loadedCommands:
        executeCommand(loadedCommand)
def executeEndCommand(commandTuple):
    pass    #Skip if so; the loop won't repeat again if command == "end"

def getIntegerInput(prompt):
    number = ""
    while not number.isdigit():
        number = input(prompt)
        if not number.isdigit():
            print("Please enter only integers as arguments!")
    return int(number)

def getCommandFromUser():
    print("The options are: " + ", ".join(COMMAND_DICTIONARY.keys()))
    command = input("Enter a command: ")
    if command in COMMAND_DICTIONARY:
        return COMMAND_DICTIONARY[command]["get"]()
    else:
        return ("Invalid",)

def executeCommand(commandTuple):
    global allCommandsList
    allCommandsList.append(commandTuple)
    if commandTuple[0] in COMMAND_DICTIONARY:
        COMMAND_DICTIONARY[commandTuple[0]]["execute"](commandTuple)
    else:
        print("Invalid command! Please enter one of the following: " + ", ".join(COMMAND_DICTIONARY.keys()))

def drawShape(numSides, sideLength):
    for _ in range(0, numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(360/numSides)

def drawSnowflake(numSides, sideLength, rotationAngle):
    numShapes = int(360 / rotationAngle)
    for _ in range(0, numShapes):
        drawShape(numSides, sideLength)
        myTurtle.right(rotationAngle)

def save(filename): #Saves allCommandsList to the filename given
    global allCommandsList
    outputFile = open(filename, "w")
    excludedCommands = ["save", "load", "record", "stop"]
    for command in allCommandsList:
        if not command[0] in excludedCommands:    #Do not save certain commands
            print(command, file=outputFile)
    outputFile.close()

def load(filename): #Loads commands from a file
    import ast
    loadedCommands = []
    inputFile = open(filename, "r")
    for line in inputFile:  #Assume each line is a command
        loadedCommands.append(ast.literal_eval(line))   #Use this to read in a tuple
    return loadedCommands

COMMAND_DICTIONARY = {"turn" : {"get" : getTurnCommand, "execute" : executeTurnCommand},
                      "forward" : {"get" : getForwardCommand, "execute" : executeForwardCommand},
                      "shape" : {"get" : getShapeCommand, "execute" : executeShapeCommand},
                      "snowflake" : {"get" : getSnowflakeCommand, "execute" : executeSnowflakeCommand},
                      "text" : {"get" : getTextCommand, "execute" : executeTextCommand},
                      "penup" : {"get" : getPenupCommand, "execute" : executePenupCommand},
                      "pendown" : {"get" : getPendownCommand, "execute" : executePendownCommand},
                      "record" : {"get" : getRecordCommand, "execute" : executeRecordCommand},
                      "stop" : {"get" : getStopCommand, "execute" : executeStopCommand},
                      "save" : {"get" : getSaveCommand, "execute" : executeSaveCommand},
                      "load" : {"get" : getLoadCommand, "execute" : executeLoadCommand},
                      "end" : {"get" : getEndCommand, "execute" : executeEndCommand}}

command = ""
recording = False
recordList = []
allCommandsList = []

while not command == "end": #Loop until the user's command is 'end'
    commandTuple = getCommandFromUser()
    command = commandTuple[0]
    if not recording or command == "stop":   #If we're not recording...
        executeCommand(commandTuple)    #Execute the command
    else:
        recordList.append(commandTuple) #Record the command
