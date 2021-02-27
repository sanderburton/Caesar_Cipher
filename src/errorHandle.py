import sys
import os

USAGE = '''
Use the following syntax:

python caesar.py [OPTIONS...] Files...

===options===

[-s]
Save output to a file. Program will prompt user to enter a path(including the file name).

[-r]
Specify the amount by which to rotate the characters (forward through the alphabet) as an integer.
This option will disable the smartCipher, so that you can manually encrypt/decrypt files. You will be 
prompted to enter a rotation amount as an integer. If a character is rotatedd past 'z', it will wrap to 
the beginning of the alphabet; consequently, rotations greater than 26 are not very useful.
'''


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