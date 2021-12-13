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

def getBlockDict():
    return {
        "(":0,
        "[":0,
        "{":0,
        "<":0
    }

def getCloseDict():
    return {
        ")":"(",
        "]":"[",
        "}":"{",
        ">":"<"
    }

def detectErrors(line):
    opens = getBlockDict()
    closes = getCloseDict()
    for i in line:
        if i in opens.keys():
            opens[i] += 1
        if i in closes.keys():
            opens[closes[i]] -= 1
            if opens[closes[i]] < 0:
                print("yo mama")
                return i
    return -1

def score(errArr):
    score = 0
    for i in errArr:
        if i == ")":
            score += 3
        elif i == "]":
            score += 57
        elif i == "}":
            score += 1197
        elif i == ">":
            score += 25137
    return score  

def goThroughLine(line):
    blockOpens = []
    closeDict= getCloseDict()

    for i in line:
        if i not in closeDict.keys():
            blockOpens.append(i)
        else:
            if closeDict[i] != blockOpens[len(blockOpens)-1]:
                return i
            else:
                blockOpens.pop()
    return -1

def partTwo(line):
    if goThroughLine(line) != -1:
        return -1
    
    blockOpens = []
    closeDict= getCloseDict()

    for i in line:
        if i not in closeDict.keys():
            blockOpens.append(i)
        else:
            blockOpens.pop()
    return blockOpens

def scoreLine(line, score):
    rev = line[::-1]

    for i in rev:
        score = score * 5
        if i == "(":
            score += 1
        elif i == "[":
            score += 2
        elif i == "{":
            score += 3
        elif i == "<":
            score += 4
    return score

def score2(data):
    scores = []
    for i in data:
        scores.append(scoreLine(i, 0))
    scores.sort()
    return scores[int(len(scores)/2)]

def main():
    textfile = open("advent10.txt", "r")
    data = readData(textfile)
    results = []
    for i in range(len(data)):
        err = partTwo(data[i])
        if err != -1:
            results.append(err)
    print(str(score2(results)))
    
main()