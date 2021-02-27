from errorHandle import validateInput, getOption
from cipher import cipher, smartCipher

import os
import sys
import time

def main():
    startTime = time.perf_counter()
    args = sys.argv[1:]

    outputFile = getOption("-s", args, str, default=sys.stdout)
    rotation = getOption("-r", args, int, default=10)

    validateInput(args)

    outputStr = smartCipher(args)
    if type(outputFile) == str:
        outputFile = open(outputFile, 'w')
        print(outputStr, end='', file=outputFile)
        outputFile.close()
    else:
        print(outputStr, end='')

    endTime = time.perf_counter()
    print(f"\nDone in {endTime - startTime:.4f} seconds!!")
    # After all options have been removed, check for fileName

main()