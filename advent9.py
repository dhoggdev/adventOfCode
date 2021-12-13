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

def getAdjacent(data, x, y):
    adjacentValues = []
    if x > 0:
        adjacentValues.append(data[y][x-1])
    if x < len(data[y])-1:
        adjacentValues.append(data[y][x+1])
    if y > 0:
        adjacentValues.append(data[y-1][x])
    if y < len(data)-1:
        adjacentValues.append(data[y+1][x])
    return adjacentValues

def isLeast(n, adj):
    for i in adj:
        if int(i) <= int(n):
            return False
    return True

def gatherLows(data):
    lows = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            adjVals = getAdjacent(data, x, y)
            if isLeast(data[y][x], adjVals):
                lows.append([y, x])
    return lows

def getNNN(data, y, x):
    nonNineNeighbors = []
    if x > 0 and int(data[y][x-1]) != 9:
        nonNineNeighbors.append([y, x-1])
    if x < len(data[y])-1 and int(data[y][x+1]) != 9:
        nonNineNeighbors.append([y,x+1])
    if y > 0 and int(data[y-1][x]) != 9:
        nonNineNeighbors.append([y-1,x])
    if y < len(data)-1 and int(data[y+1][x]) != 9:
        nonNineNeighbors.append([y+1,x])
    return nonNineNeighbors


def baisinBuilder(data, y, x):
    checkedCoords = []
    uncheckedCoords = [[y,x]]

    while len(uncheckedCoords) > 0:
        nnn = getNNN(data, uncheckedCoords[0][0], uncheckedCoords[0][1])
        for i in nnn:
            if i not in uncheckedCoords and i not in checkedCoords:
                uncheckedCoords.append(i)
        if uncheckedCoords[0] not in checkedCoords:
            checkedCoords.append(uncheckedCoords[0])
        uncheckedCoords.pop(0)

    return len(checkedCoords)

def main():
    textfile = open("advent9.txt", "r")
    data = readData(textfile)
    lows = gatherLows(data)
    
    basins = []
    for i in lows:
        basins.append(baisinBuilder(data, i[0], i[1]))

    basins.sort(reverse = True)
    print(str(basins[0] * basins[1] * basins[2]))

main()