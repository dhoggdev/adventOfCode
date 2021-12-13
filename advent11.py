def readData(textfile):
    data = []
    for i in textfile:
        data.append(i)
    return removeNewLines(data)
    
def removeNewLines(data):
    lines = []
    for i in data:
        if (i[len(i)-1] == "\n"):
            lines.append(i[:len(i)-1])
        else:
            lines.append(i)
    return lines