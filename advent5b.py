textfile = open("advent5.txt", "r")

data = []
for line in textfile:
    data.append(line)

dupeDict = {}

def formatPoints(line):
    s = line.split(' -> ')
    results = []
    for i in s:
        results.append(removeWhitey(str(i)))
    return results

def removeWhitey(s):
    res = ""
    for i in s:
        if (str(i) != " " and str(i) != "\n"):
            res = res + str(i)
    return res

def onlyStrights(lines):
    result = [[],[]]
    for line in lines:
        t = line[0].split(",")
        t2 = line[1].split(",")
        if (int(t[0]) == int(t2[0]) or int(t[1]) == int(t2[1])):
            result[0].append(line)
        else:
            result[1].append(line)
    return result

def buildLines(line):
    p1 = line[0].split(",")
    p2 = line[1].split(",")
    getLineArr(p1, p2)

def varIndValues(n1, n2):
    results = []
    if int(n1) < int(n2):
        for x in range(n1, n2+1):
            results.append(x)
    else:
        for x in range(n2, n1+1):
            results.append(x)
    return results

def getLineArr(p1, p2):
    varValArr = []
    varInd = 0
    stableInd = 1
    if (int(p1[0]) != int(p2[0])):
        varValArr = varIndValues(int(p1[0]), int(p2[0]))
    else:
        varValArr = varIndValues(int(p1[1]), int(p2[1]))
        varInd = 1
        stableInd = 0
    linePointArr(varValArr, p1[stableInd], stableInd, varInd)

def linePointArr(arr, stableVal, stableInd, varInd):
    for i in arr:
        t = [1,1]
        t[stableInd] = stableVal
        t[varInd] = i
        s = str(t[0]) + "," + str(t[1])
        if (s in dupeDict):
            dupeDict[s] = True
        else:
            dupeDict[s] = False

## diags
def doDiag(dline):
    p1 = dline[0].split(",")
    p2 = dline[1].split(",")
    dPoints(p1, p2)

def dPoints(p1, p2):
    xarr = diagSingleArr(int(p1[0]), int(p2[0]))
    yarr = diagSingleArr(int(p1[1]), int(p2[1]))
    joinArrsToPoints(xarr, yarr)

def diagSingleArr(n1, n2):
    results = []
    if n1 < n2:
        for i in range(n1, n2+1):
            results.append(i)
    else:
        for i in range(n1, n2-1, -1):
            results.append(i)
    return results

def joinArrsToPoints(arr1, arr2):
    for i in range(len(arr1)):
        s = (str(arr1[i]) + "," + str(arr2[i]))
        if (s in dupeDict):
            dupeDict[s] = True
        else:
            dupeDict[s] = False

###################################################

formatLines = []
for i in data:
    formatLines.append(formatPoints(i))

filteredLines = onlyStrights(formatLines)
straights = filteredLines[0]
diags = filteredLines[1]

for i in straights:
    buildLines(i)

for i in diags:
    doDiag(i)

count = 0
for i in dupeDict:
    if (dupeDict[i]):
        count = count + 1

print(str(count))