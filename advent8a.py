# textfile = open("advent8.txt", "r")
#
# data = []
# for line in textfile:
#     data.append(line)

def generateData(tf):
    data = []
    for line in tf:
        data.append(line)
    return data

def cutNewline(s):
    if s[len(s)-1] == "\n":
        return s[:len(s)-1]
    return s

def splitAllLines(rawData):
    leftValues = []
    rightValues = []
    for i in rawData:
        splitData = i.split(" | ")
        leftValues.append(splitData[0])
        rightValues.append(cutNewline(splitData[1]))
    return [leftValues, rightValues]

def getAllOfLen(arr, n):
    result = []
    for i in arr:
        if len(i) == n:
            result.append(i)
    return result

def getIndexOfZero(known, sixes): # with 6 removed, only 0 does not contian each value of 4 (9 does)
    four = known[4]
    for i in range(len(sixes)):
        for j in four:
            if j not in sixes[i]:
                return i
    return -1
    
def getIndexOfSix(known, sixes): # 6 is the only len 6 value that does not contain both values of 1
    for i in range(len(sixes)):
        one = known[1]
        if not (one[0] in sixes[i] and one[1] in sixes[i]):
            return i
    return -1
    
def getIndexOfThree(known, fives): # 3 is the only len 5 value that contains both values of 1
    one = known[1]
    for i in range(len(fives)):
        if (one[0] in fives[i]) and (one[1] in fives[i]):
            return i
    return -1

def getIndexOfFive(known, fives):# with 3 removed, only 5 contains 3 values of 4 (2 has 2 values)
    for i in range(len(fives)):
        count = 0
        for j in known[4]:
            if j in fives[i]:
                count = count + 1
            if (count == 3):
                return i
    return -1

def assignUniqueValues(known, arr):
    for i in arr:
        if len(i) == 2:
            known[1] = i
        if len(i) == 3:
            known[7] = i
        if len(i) == 4:
            known[4] = i
        if len(i) == 7:
            known[8] = i
    return known

def assignLenFive(known, arr):
    fivers = getAllOfLen(arr, 5) # 3, 5, 2

    ind = getIndexOfThree(known, fivers)
    known[3] = fivers[ind]
    del(fivers[ind])

    ind = getIndexOfFive(known, fivers)
    known[5] = fivers[ind]
    del(fivers[ind])

    known[2] = fivers[0]

    return known

def assignLenSix(known, arr):
    sixers = getAllOfLen(arr, 6) # 0, 6, 9

    ind = getIndexOfSix(known, sixers)
    known[6] = sixers[ind]
    del(sixers[ind])

    ind = getIndexOfZero(known, sixers)
    known[0] = sixers[ind]
    del(sixers[ind])

    known[9] = sixers[0]

    return known

def buildCypher(known, arr):
    known = assignUniqueValues(known, arr)
    known = assignLenFive(known, arr)
    known = assignLenSix(known, arr)
    return known

def decodeNumber(known, s):
    answer = ""
    arr = s.split(" ")
    for i in arr:
        sNum = sorted(i)
        for j in range(len(known)):
            if sNum == known[j]:
                answer = answer + str(j)
    return int(answer)

def splitAndSortLine(s):
    nArr = s.split(" ")
    for i in range(len(nArr)):
        nArr[i] = sorted(nArr[i])
    return nArr

def buildFourDigitNumbers(cypherValues, codedValues):
    fourDigitNumbers = []
    for i in range(len(cypherValues)):
        knownValues = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        lineArr = splitAndSortLine(cypherValues[i])
        knownValues = buildCypher(knownValues, lineArr)
        fourDigitNumbers.append(decodeNumber(knownValues, codedValues[i]))
    return fourDigitNumbers

def getSum(arr):
    sum = 0
    for i in arr:
        sum = sum + int(i)
    return sum

def main():
    textfile = open("advent8.txt", "r")
    splitData = splitAllLines(generateData(textfile))
    fourDigitNumbers = buildFourDigitNumbers(splitData[0], splitData[1])
    print(str(getSum(fourDigitNumbers)))

main()
