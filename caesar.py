from errorHandle import validateInput, getOption
from cipher import cipher

import os
import sys

validateInput(sys.argv)

# outPutFile = sys.stdout
operation = sys.argv[1].lower()
args = sys.argv[2:]

outPutFile = getOption("-s", args, str)
rotation = getOption("-r", args, int)

outPutStr = cipher(args, 1)

print(outPutStr.strip('\n'))
# After all options have been removed, check for fileName

# print(type(rotation), type(outPutFile))
# print(args)
