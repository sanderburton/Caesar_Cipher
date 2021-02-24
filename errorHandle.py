import sys

USAGE = '''
Usage: 
caesar.py encrypt|decrypt [OPTIONS...] Files...'''


def error(msg=""):
    print(f"Error! {msg}", file=sys.stderr)
    print(USAGE, file=sys.stderr)


def validateInput(userInput):
    if len(userInput) < 3:
        error("You must specify 'encrypt' or 'decrypt' and at least one file name")
        sys.exit(1)

    operation = userInput[1].lower()
    if operation != 'encrypt' and operation != 'decrypt':
        error(f"First argument must be either 'encrypt' or 'decrypt' (Got '{userInput[1]}')")
        sys.exit(1)

def getOption(flag, args, dataType):
    if flag in args:
        i = args.index(flag)
        args.pop(i)
        option = args.pop(i) 
        if dataType == int:
            if option.isdigit():
                return int(option)
            else:
                error(f"An integer is required after the {flag} flag (Got '{option}')")
        return option