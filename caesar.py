from errorHandle import validateInput, getOption
from cipher import cipher

import os
import sys

def main():
    args = sys.argv[1:]

    outputFile = getOption("-s", args, str, default=sys.stdout)
    rotation = getOption("-r", args, int, default=10)

    validateInput(args)

    outputStr = cipher(args, rotation)
    if type(outputFile) == str:
        outputFile = open(outputFile, 'w')
        print(outputStr, end='', file=outputFile)
        outputFile.close()
    else:
        print(outputStr, end='')
    # After all options have been removed, check for fileName

main()