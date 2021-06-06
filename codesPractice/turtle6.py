import turtle
myTurtle = turtle.Turtle()
VALID_COMMANDS = ("turn", "forward", "shape", "snowflake", "text", "penup", "pendown",
                  "record", "stop", "save", "load", "end")

def getIntegerInput(prompt):
    number = ""
    while not number.isdigit():
        number = input(prompt)
        if not number.isdigit():
            print("Please enter only integers as arguments!")
    return int(number)

#Print the available commands, then get the selected command from the user. Then, depending on the command,
#prompt the user for the arguments necessary to execute that command. Then, create a tuple with that command
#name as the first value and the arguments provided as the remaining values.
def getCommandFromUser():
    print("The options are: " + ", ".join(VALID_COMMANDS))
    command = input("Enter a command: ")
    if command == "turn":
        angle = getIntegerInput("Enter the angle: ")
        commandTuple = ('turn', angle)
    elif command == "forward":
        distance = getIntegerInput("Enter distance: ")
        commandTuple = ('forward', distance)
    elif command == "shape":
        numSides = getIntegerInput("Enter the number of sides (3 or more): ")
        sideLength = getIntegerInput("Enter the length of each side: ")
        commandTuple = ('shape', numSides, sideLength)
    elif command == "snowflake":
        numSides = getIntegerInput("Enter the number of sides (3 or more): ")
        sideLength = getIntegerInput("Enter the length of each side: ")
        rotationAngle = getIntegerInput("Enter the rotation angle for each flake: ")
        commandTuple = ('snowflake', numSides, sideLength, rotationAngle)
    elif command == "text":
        message = input("Enter the message to print: ")
        message = message.replace("\\n", "\n")
        commandTuple = ('text', message)
    elif command == "penup":
        commandTuple = ('penup',)   #Comma forces commandTuple to be a tuple
    elif command == "pendown":
        commandTuple = ('pendown',) #Comma forces commandTuple to be a tuple
    elif command == "record":
        commandTuple = ('record',)  #Comma forces commandTuple to be a tuple
    elif command == "stop":
        repeats = getIntegerInput("How many times should these commands repeat? ")
        commandTuple = ('stop', repeats)
    elif command == "save":
        filename = input("Enter the filename to which to save: ")
        commandTuple = ('save', filename)
    elif command == "load":
        filename = input("Enter the filename from which to load: ")
        commandTuple = ('load', filename)
    elif command == "end":
        commandTuple = ('end',) #Comma forces commandTuple to be a tuple
    else:
        commandTuple = ('invalid',) #Comma forces commandTuple to be a tuple
    return commandTuple

#Execute a command tuple, where the name of the command is given in the first spot and the arguments are provided
#in the remaining spots.
def executeCommand(commandTuple):
    global recordList
    global recording
    global allCommandsList
    allCommandsList.append(commandTuple)
    command = commandTuple[0]
    if command == "turn":
        myTurtle.right(commandTuple[1])
    elif command == "forward":
        myTurtle.forward(commandTuple[1])
    elif command == "shape":
        drawShape(commandTuple[1], commandTuple[2])
    elif command == "snowflake":
        drawSnowflake(commandTuple[1], commandTuple[2], commandTuple[3])
    elif command == "text":
        myTurtle.write(commandTuple[1], True, font = ("Arial", 16, "normal"))
    elif command == "penup":
        myTurtle.penup()
        print("Pen up!")
    elif command == "pendown":
        myTurtle.pendown()
        print("Pen down!")
    elif command == "record":
        if not recording:
            print("Recording!")
            recordList.clear()
            recording = True
        else:
            print("You're already recording!")
    elif command == "stop":
        recording = False
        print("Playing back " + str(len(recordList)) + " commands " + str(commandTuple[1]) + " times!")
        for _ in range(0, commandTuple[1]):
            for recordedCommand in recordList:
                executeCommand(recordedCommand)
    elif command == "save":
        save(commandTuple[1])
    elif command == "load":
        loadedCommands = load(commandTuple[1])
        for loadedCommand in loadedCommands:
            executeCommand(loadedCommand)
    elif command == "end":
        pass    #Skip if so; the loop won't repeat again if command == "end"
    else:
        print("Invalid command! Please enter one of the following: " + ", ".join(VALID_COMMANDS))

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

command = ""
recording = ""
recordList = []
allCommandsList = []

while not command == "end": #Loop until the user's command is 'end'
    commandTuple = getCommandFromUser()
    command = commandTuple[0]
    if not recording or command == "stop":   #If we're not recording...
        executeCommand(commandTuple)    #Execute the command
    else:
        recordList.append(commandTuple) #Record the command