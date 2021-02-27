import sys
import os

USAGE = '''
Use the following syntax:

python caesar.py [OPTIONS...] Files...

===options===

[-s]
specify a file for the output to be saved to.

[-r]
specify the amount by which to rotate the characters (forward through the alphabet) as an integer. By
default the cipher rotates by 10'''


def error(msg=""):
    print(f"Error! {msg}", file=sys.stderr)
    print(USAGE, file=sys.stderr)
    sys.exit(1)


def validateInput(userInput):
    if len(userInput) < 1:
        error("You must specify at least one file name")


def isValidFilePath(filePath):
    if os.access(filePath, os.R_OK):
        return True
    else:
        error(f"{filePath} is not a valid file or you do not have permission to open it")