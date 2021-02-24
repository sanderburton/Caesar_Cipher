from errorHandle import validateInput, getOption
from cipher import cipher

import os
import sys

def main():
    args = sys.argv[1:]

    outPutFile = getOption("-s", args, str, default=sys.stdout)
    rotation = getOption("-r", args, int, default=10)

    validateInput(args)

    outputStr = cipher(args, rotation)
    print(outputStr.strip('\n'))
    # After all options have been removed, check for fileName

main()