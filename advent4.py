textfile = open("advent4.txt", "r")

data = []
for line in textfile:
    data.append(line)

calls = data[0].split(",")
data.pop(0)
data.pop(0)

boards = []

def parseRow(line):
    row = []
    rawRow = line.split(" ")
    for i in rawRow:
        if (i != ""):
            row.append(int(i))
    return row

boards = []

rows = []
for i in data:
    if (i != "\n"):
        rows.append(parseRow(i))
    else:
        boards.append(rows)
        rows = []

def boardCheck(board, called):
    for row in range(len(board)):
        if (checkHorizontal(board[row], called)):
                return True
        for cell in range(len(board[row])):
            col = getColumn(board, cell)
            if (checkHorizontal(col, called)):
                return True
    return False

def checkBoard(board, called):
    for i in range(len(board[0])):
        if (checkHorizontal(getColumn(board, i), called)):
            return True
    for i in board:
        if checkHorizontal(i, called):
            return True
    return False

def getColumn(board, index):
    col = []
    for i in board:
        col.append(i[index])
    return col

def checkHorizontal(row, calledNumbers):
    for i in row:
        if (str(i) not in calledNumbers):
            return False
    return True

def boardSum(board, called):
    sum = 0
    for i in board:
        for j in i:
            if (str(j) not in called):
                sum = sum + int(j)
    return sum
winningBoards = []
madeCalls = []
def doThing():
    for i in calls:
        madeCalls.append(i)
        for j in range(len(boards)):
            if (checkBoard(boards[j], madeCalls)):
                if (j not in winningBoards):
                    winningBoards.append(j)
                    print(str(boards[j]))
                    x = (madeCalls[len(madeCalls)-1])
                    print(str(x))
                    print(str(int(boardSum(boards[j], madeCalls)) * int(x)))
                    
doThing()
