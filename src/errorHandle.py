import sys

USAGE = '''
Use the following syntax:

python caesar.py [OPTIONS...] Files...

===options===

[-s FileName]
specify a file for the output to be saved to.

[-r rotationAmount]
specify the amount by which to rotate the characters (forward through the alphabet) as an integer. By
default the cipher rotates by 10'''


def error(msg=""):
    print(f"Error! {msg}", file=sys.stderr)
    print(USAGE, file=sys.stderr)
    sys.exit(1)


def validateInput(userInput):
    if len(userInput) < 1:
        error("You must specify at least one file name")


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