

def createDict(fileName):
    file = open(fileName)
    dictionary = set()

    for line in file:
        dictionary.add(line.strip("\n"))

    return dictionary