from readDictionary import createDict
from errorHandle import isValidFilePath
import os

def cipher(fileList, rotation):
    
    outputStr = ""
    for f in fileList:
        outputStr += cipherFile(f, rotation)

    return outputStr

def smartCipher(fileList):
    print("\nSmartCipher is thinking...")
    outputStr = ''
    words = createDict(os.path.dirname(__file__) + "/../resources/words.txt")
    
    for f in fileList:
        best = 0.0

        for i in range(26):
            cipheredText = cipherFile(f, i)
            englishWords = 0
            cipheredWordList = cipheredText.split()
            for word in cipheredWordList:
                if word in words:
                    englishWords += 1
            confidence = (englishWords / len(cipheredWordList)) * 100

            if confidence > best:
                best = confidence
                bestText = cipheredText
                rotations = i

        outputStr += f"\n========{f} rotated by {rotations}, confidence: {best:.2f}%========\n{bestText}"
    return outputStr


def cipherFile(fileName, rotation):
    if isValidFilePath(fileName):
        outputStr = ''
        fobj = open(fileName)
        for line in fobj:
            line = line.strip('\n')
            outputStr += cipherLine(line, rotation)

        fobj.close()
        return outputStr
  

def cipherLine(line, rotation):
    lineOutput = ""
    for char in line:
        if not (char.isalpha()):
            lineOutput += char
            continue

        asciiVal = ord(char)
        # rotate the character by the rotation amount (at most 26, because after that we wrap around to where we started in the alphabet)
        asciiVal += (rotation % 26) 

        if char.isupper():
            # 90 is the max value for an uppercase letter 'Z' , 65 is the min value for an uppercase letter 'A'
            if asciiVal > 90:
                asciiVal = 64 + asciiVal - 90

        elif char.islower():
            # 122 is the max ascii value for a lowercase letter 'z', 97 is the min ascii value for a lowercase letter 'a'
            if asciiVal > 122:
                asciiVal = 96 + asciiVal - 122

        lineOutput += chr(asciiVal)

    return lineOutput + "\n"

