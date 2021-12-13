textfile = open("advent8.txt", "r")

data = []
for line in textfile:
    data.append(line)

def filterOne(m, v):
    usedLetters = "cf"
    for i in usedLetters:
        for j in v:
            m[i] = removeCharFromString(m[i], j)
    return m      

def filterFour(m, v):
    usedLetters = "bcdf"
    for i in usedLetters:
        for j in v:
            m[i] = removeCharFromString(m[i], j)
    return m

def filterSeven(m, v):
    usedLetters = "acf"
    for i in usedLetters:
        for j in v:
            m[i] = removeCharFromString(m[i], j)
    return m

def assignA(m, one, seven):
    for i in seven:
        if i not in one:
            m["a"] = i
    return m


def reduceSingle(map):
    for i in map:
        if (len(i) == 1):
            for j in map:
                if j in map and len(map[j]) > 1:
                    map[j] = removeCharFromString(map[j], i)
    return map

def removeCharFromString(s, c):
    result = ""
    for i in s:
        if i != c:
            result = result + i
    return result

def buildMap(nums):
    numMap = {"a": "abcdefg", "b": "abcdefg", "c": "abcdefg", "d": "abcdefg", "e": "abcdefg", "f": "abcdefg", "g": "abcdefg"}
    for i in nums:
        for j in uniques:
            if len(i) == len(numbers[j]):
                numMap[i] = removeEliminatedValues(numMap[i], numbers[j])
                print(str(numMap[i]))
            for k in numMap:
                if len(k) > 1:
                    continue
                return numMap
    return numMap

def removeEliminatedValues(mapValues, possibleValues):
    results = []
    for i in mapValues:
        for j in possibleValues:
            if i == j:
                results.append(j)
    return results

def decode(map, values):
    s = ""
    sValues = sorted(values)
    for i in sValues:
        s = s + map[i]
    return getNumber(s)

def getNumber(s):
    for i in range(len(numbers)):
        if numbers[i] == s:
            return i
    return -1

firstArr = []
secondArr= []
for i in data:
    splitData = i.split(" | ")
    firstArr.append(splitData[0])
    if (splitData[1][len(splitData[1])-1] == "\n"):
        secondArr.append(splitData[1][:len(splitData[1])-1])
    else:
        secondArr.append(splitData[1])

numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
uniques = [1, 4, 7, 8]

finalResults = []

for i in range(len(firstArr)):
    nums = firstArr[i].split(" ")
    for j in nums:
        numMap = buildMap(j)
        result = []
        for k in secondArr[i].split(" "):
            result.append(decode(numMap, k))
        
    finalResults.append(result)
count = 0
for i in finalResults:
    for j in i:
        if j == 1 or j == 4 or j == 7 or j == 8:
            count = count + 1
print(str(count))

for i in secondArr:
    s = i.split(" ")
    for j in s:
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            count = count + 1
print(str(count))


allMaps = []
for i in range(len(firstArr)):
    nums = firstArr[i].split(" ")
    for j in nums:
        numMap = buildMap(j)
        result = []
        for k in secondArr[i].split(" "):
            if len(k) == 2:
                numMap = filterOne(numMap, k)
            if len(k) == 3:
                numMap = filterSeven(numMap, k)
            if len(k) == 4:
                numMap = filterFour(numMap, k)
            numMap = reduceSingle(numMap)
        result.append(numMap)
        
    allMaps.append(result)

print(str(allMaps))
    


