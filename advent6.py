textfile = open("advent6.txt", "r")

data = []
for line in textfile:
    data.append(line)

data = data[0].split(",")

for i in range(len(data)):
    data[i] = int(data[i])

fishGroups = []

def groupFish(fish, fishGroups):
    if (len(fishGroups) == 0):
        fishGroups.append({"size": 1, "tts": fish[0]})
    
    for i in fish:
        fishGroups = checkFishGroup(i, fishGroups)
    fishGroups[0]["size"] = fishGroups[0]["size"]-1
    return fishGroups
    
def checkFishGroup(fish, fishGroups):
    for i in fishGroups:
        if i["tts"] == fish:
            i["size"] = i["size"] + 1
            return fishGroups
    fishGroups.append({"size": 1, "tts": fish})
    return fishGroups

def oneDictDay(fishGroupList):
    newFish = 0
    for i in fishGroupList:
        if i["tts"] > 0:
            i["tts"] = i["tts"]-1
        else:
            i["tts"] = 6
            newFish = newFish + i["size"]
    if (newFish > 0):
        fishGroupList.append({"size": newFish, "tts": 8})
    return fishGroupList

fishGroups = groupFish(data, fishGroups)

def timePass2(fishList, days):
    ourFishList = fishList
    for i in range(days):
        ourFishList = oneDictDay(ourFishList)
    return ourFishList

finalFishList = timePass2(fishGroups, 256)

count = 0
for i in finalFishList:
    count = count + i["size"]
print(str(count))