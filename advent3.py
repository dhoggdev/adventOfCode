textfile = open("advent3.txt", "r")

data = []
for line in textfile:
    data.append(line)


countArr = []

for i in data:
    for c in i:
        if (c != "\n"):
            countArr.append(0)
    break
# print(str(countstring))
total = 0
for i in data:
    i = i[:len(i)-1]
    for c in range(len(i)):
        if (int(i[c]) == 1):
            countArr[c] = countArr[c] + 1
    total = total + 1
realResults = []
for i in countArr:
    if (i >= total - i):
        realResults.append(1)
    else:
        realResults.append(0)

print(str(realResults))


#####################################################

fData = data
for res in range(len(realResults)):
    for i in data:
        continue

def dtrim(data, n, i):
    results = []
    for li in data:
        if (li[i] == str(n)):
            results.append(li)
    return results

def reduceUntilOne(da, rr):
    for i in range(len(rr)):
        da = dtrim(da, rr[i], i)
        if (len(da) == 1):
            return da
    return da

def reverseRR(arr):
    narr = []
    for i in arr:
        if i == 1:
            narr.append(0)
        else:
            narr.append(1)
    return narr

print(str(reduceUntilOne(data, realResults)))
print(str(reduceUntilOne(data, reverseRR(realResults))))
