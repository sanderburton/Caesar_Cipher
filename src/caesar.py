from errorHandle import validateInput
from cipher import cipher, smartCipher
from options import parseOptions, getAdditionalInput

import os
import sys
import time

def main():
    args = sys.argv[1:]

    
    optionsList = parseOptions(args)
    validateInput(args)
    options = getAdditionalInput(optionsList)

    startTime = time.perf_counter()

    if 'rot' in options:
        outputStr = cipher(args, options['rot'])
    else:
        outputStr = smartCipher(args)

    if 'saveFile' in options:
        try:
            file = open(options['saveFile'], 'w')
            print(outputStr, end='', file=file)
            print(f"Result has been saved to {options['saveFile']}" )
            file.close()
        except FileNotFoundError:
            print("The path specified could not be found, please ensure that any directories in the file path already exist")
            sys.exit(1)
    else:
        print(outputStr, end='')

    endTime = time.perf_counter()
    print(f"\nDone in {endTime - startTime:.4f} seconds!!")
    # After all options have been removed, check for fileName

main()