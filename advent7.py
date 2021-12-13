textfile = open("advent7.txt", "r")

data = []
for line in textfile:
    data.append(line)

data = data[0].split(",")

# print(str(data))

min = 0
max = 1910

# for i in data:
#     if (int(i) > max):
#         max = int(i)
#     if (int(i) < min):
#         min = int(i)
# print("MIN: " + str(min))
# print("MAX: " + str(max))

numData = []
for i in data:
    numData.append(int(i))

numData.sort()

pivot = int(len(numData)/2)

leftShifts = 0
rightShifts = 0
expoDict = {}

def getExpoValByNum(n):
    total = 0
    increase = 0
    for i in range(n):
        total = total + 1 + increase
        increase = increase + 1
    return total

def buildExpoDict():
    for i in range(1, 2000):
        expoDict[i] = getExpoValByNum(i)
buildExpoDict()

def determineShifts(data, ind):
    lshift = 0
    rshift = 0

    pivotVal = data[ind]

    for i in range(0, ind):
        # lshift = lshift + (pivotVal-data[i])
        m = pivotVal - data[i]
        if m > 0:
            lshift = lshift + expoDict[m]
    for i in range(ind+1, len(data)):
        # rshift = rshift + (data[i]-pivotVal)
        m = data[i] - pivotVal
        if (m > 0):
            rshift = rshift + expoDict[m]

    return[lshift, rshift]

recordMin = 100000000000000000000000
recordInd = -1
for i in range(len(numData)):
    d = determineShifts(numData, i)
    if (d[0]+d[1]) < recordMin:
        recordMin = d[0]+d[1]
        recordInd = i
print(str(recordMin))
