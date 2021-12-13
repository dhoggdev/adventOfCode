## seperate checks
singleIncrease = 0
previousSingle = None
textfile = open('advent1.txt', 'r')

for line in textfile:
    if (previousSingle is not None):
        if (int(line) > previousSingle):
            singleIncrease = singleIncrease + 1

    previousSingle = int(line)

print("Increases: " + str(singleIncrease))

arr = []
results = []
textfile = open('advent1.txt', 'r')

for line in textfile:
    arr.append(int(line))
    if (len(arr) == 3):
        results.append(arr[0]+arr[1]+arr[2])
        arr.pop(0)

prev = None
inc = 0

for r in results:
    if (prev is not None):
        if  (int(r) > prev):
            inc = inc + 1
    prev = int(r)
    
print("Group Increases: " + str(inc))


## do it all at once
singleIncrease = 0
groupIncrease = 0
previousSingle = None
previousGroupSum = None

groupArr = []
textfile = open('advent1.txt', 'r')

def groupSum(arr):
    result = 0
    for i in arr:
        result = result + i
    return result

for line in textfile:
    num = int(line)
    groupArr.append(num)

    if (previousSingle is not None and num > previousSingle):
         singleIncrease = singleIncrease + 1
    if (len(groupArr) == 3):
        if (previousGroupSum is not None):
            if (groupSum(groupArr) > previousGroupSum):
                groupIncrease = groupIncrease + 1
        previousGroupSum = groupSum(groupArr)
        groupArr.pop(0)

    previousSingle = num

print("Singles Increases: " + str(singleIncrease))
print("Group Increases: " + str(groupIncrease))


## make increase check modular and reuse on raw list and grouped list
def getIncreases(arr):
    increases = 0
    previous = None
    for i in arr:
        if (previous is not None and i > previous):
            increases = increases + 1
        previous = i
    
    return increases

def getArrayFromFile(textfile):
    results = []
    for line in textfile:
        results.append(int(line))

    return results

def getSumOfArray(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return sum

def getGroupSumsFromArray(arr, num):
    numGroup = []
    results = []
    for i in arr:
        numGroup.append(int(i))
        if (len(numGroup) == num):
            results.append(getSumOfArray(numGroup))
            numGroup.pop(0)
    
    return results

def modularMain():
    textfile = open('advent1.txt', 'r')
    numbers = getArrayFromFile(textfile)
    groups = getGroupSumsFromArray(numbers, 3)

    print("Modular Single Increases: " + str(getIncreases(numbers)))
    print("Modular Group Increases: " + str(getIncreases(groups)))

modularMain()
