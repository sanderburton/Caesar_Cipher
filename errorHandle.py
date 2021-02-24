import sys

USAGE = '''
Usage: 
caesar.py encrypt|decrypt [OPTIONS...] Files...'''


def error(msg=""):
    print(f"Error! {msg}", file=sys.stderr)
    print(USAGE, file=sys.stderr)
    sys.exit(1)


def validateInput(userInput):
    if len(userInput) < 1:
        error("You must specify at least one file name")

    # operation = userInput[1].lower()
    # if operation != 'encrypt' and operation != 'decrypt':
    #     error(f"First argument must be either 'encrypt' or 'decrypt' (Got '{userInput[1]}')")
    #     sys.exit(1)


def getOption(flag, args, dataType, default):
    '''
    Parses the command line arguments for optional flags, and handles incorrect inputs
    '''
    if flag in args:
        i = args.index(flag)
        if len(args) - 1 == i:
            error(f"No argument follows '{flag}' flag ")
        args.pop(i)
        option = args.pop(i) 
        if dataType == int:
            if option.isdigit():
                return int(option)
            else:
                error(f"An integer is required after the {flag} flag (Got '{option}')")
        return option

    return default