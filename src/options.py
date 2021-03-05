from errorHandle import error

def parseOptions(args):
    allOptions = []

    # for arg in args:
    i = -1
    while i < len(args) - 1:
        i += 1
        arg = args[i]
        if not arg.startswith("-"):
            continue

        args.pop(i) # Remove the argument starting with '-', so that args only contains file names
        i -= 1
        options = arg[1:]
        if len(options) == 0:
            error("One or more options are required immediately following a '-' character")
        
        for opt in options:
            if opt in allOptions:
                continue
            allOptions.append(opt)

    return allOptions


def  getAdditionalInput(options):
    userInput = {}
    for opt in options:
        if opt == 'r':
            userInput['rot'] = getIntegerInput("Enter rotation amount as an integer: ")
        elif opt == 's':
            userInput['saveFile'] = input("Enter the name of (or path to) the file to create: ")
        else:
            error(f"no -{opt} option exists")

    return userInput
            

def getIntegerInput(message):
    userInp = input(message)
    while True:
        if userInp.isdigit():
            return int(userInp)
        else:
            print("Error! An integer is required")


            


