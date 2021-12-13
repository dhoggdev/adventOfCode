import copy
textfile = open("advent5.txt", "r")

data = []
for line in textfile:
    data.append(line)

# for i in data:
#     print(str(i))

def trimWhite(arr):
    results = []
    for i in arr:
        s = str(i)
        ns = ""
        for j in s:
            if (str(j) != " " and str(j) != "\n"):
                ns = ns + str(j)
        results.append(ns)
    return results

lines = []
def dataFormating(line):
    splitPoints = line.split(" -> ")
    nuPoints = trimWhite(splitPoints)
    for i in range(len(nuPoints)):
        nuPoints[i] = nuPoints[i].split(",")
    return nuPoints

def isStright(point1, point2):
    if (int(point1[0]) == int(point2[0])):
        return True
    if (int(point1[1]) == int(point2[1])):
        return True
    return False

def drawLine(point1, point2):
    varInd = 0 if int(point1[0]) != int(point2[0]) else 1
    smallPoint = point1 if int(point1[varInd]) < int(point2[varInd])else point2
    bigPoint = point1 if int(point1[varInd]) > int(point2[varInd])else point2
    staticVal = point1[0] if varInd == 1 else point1[1]
    arr = dl(smallPoint[varInd], bigPoint[varInd])
    return makePairs(arr, staticVal, varInd)

def dl(small, big):
    results = []

    c = int(small)
    while c <= int(big):
        results.append(c)
        c = c + 1

    return results

def makePairs(arr, val, ind):
    results = []
    if (ind == 0):
        for i in arr:
            results.append(str(i)+","+str(val))
    else:
        for i in arr:
            results.append(str(val)+","+ str(i))
    return results


ndata = []
for i in data:
    ndata.append(dataFormating(i))

lines = []
for i in ndata:
    p = i[0]
    p2 = i[1]
    if (isStright(p, p2)):
        lines.append(drawLine(p, p2))

mt2 = 0

def comp(p1, p2):
    if (int(p1[0]) ==  int(p2[0]) and int(p1[1]) == int(p2[1])):
        return True
    return False

def county():
    c = 0
    for i in lines:
        for j in i:
            if cAll(j):
                c = c + 1
    return c

def cAll(p):
    c = 0
    for i in lines:
        for j in i:
            if (comp(p, j)):
                c = c + 1
            if (c > 1):
                return True
# print(str(county()))
# total = 0
# checked = []
# for i in range(len(lines)):
#     for j in lines[i]:
#         if (j not in checked):
#             for k in range(i+1, len(lines)):
#                 if (j in lines[k]):
#                     total = total + 1
#                     checked.append(j)
# print(str(total))
count = 0
fullList = []
for i in lines:
    for j in i:
        fullList.append(j)
# print(str(fullList))

def thing(list):
    tmp = copy.deepcopy(list[0])
    del(list[0])
    if (tmp in list):
        return True
    return False

def otherThing(list):
    l  = copy.deepcopy(list)
    l2 = copy.deepcopy(l)
    count = 0
    dupes = []
    while (len(l) > 0):
        if (thing(l2)):
            if (l2[0] not in dupes):
                dupes.append(l2[0])
        del(l[0])
        l2 = copy.deepcopy(l)
    return dupes

fin = otherThing(fullList)
print(str(len(fin)))

