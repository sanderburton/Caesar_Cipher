from errorHandle import validateInput
from cipher import cipher, smartCipher
from options import parseOptions, getAdditionalInput

import os
import sys
import time

def main():
    args = sys.argv[1:]

    validateInput(args)
    optionsList = parseOptions(args)

    # outputFile = getOption("-s", args, str, default=sys.stdout)
    # rotation = getOption("-r", args, int, default=10)

    options = getAdditionalInput(optionsList)

    startTime = time.perf_counter()

    if 'rot' in options:
        outputStr = cipher(args, options['rot'])
    else:
        outputStr = smartCipher(args)

    if 'saveFile' in options:
        file = open(options['saveFile'], 'w')
        print(outputStr, end='', file=file)
        file.close()
    else:
        print(outputStr, end='')

    endTime = time.perf_counter()
    print(f"\nDone in {endTime - startTime:.4f} seconds!!")
    # After all options have been removed, check for fileName

main()