


def cipher(fileList, rotation):
    outputStr = ""
    for f in fileList:
        fobj = open(f)

        for line in fobj:
            line = line.strip()
            outputStr += cipherLine(line, rotation)

        fobj.close()
    return outputStr

def cipherLine(line, rotation):
    lineOutput = ""
    for char in line:
        asciiVal = ord(char)
        if not (char.isalpha()):
            lineOutput += char
            continue

        asciiVal += (rotation % 26)

        if char.isupper():
            # 90 is the max value for an uppercase letter 'Z' , 65 is the min value for an uppercase letter 'A'
            if asciiVal > 90:
                asciiVal = 65 + asciiVal - 90
        elif char.islower():
            # 122 is the max ascii value for a lowercase letter 'z', 97 is the min ascii value for a lowercase letter 'a'
            if asciiVal > 122:
                asciiVal = 97 + asciiVal - 122

        lineOutput += chr(asciiVal)
    return lineOutput + "\n"


