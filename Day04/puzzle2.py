
import time
from copy import deepcopy
from pprint import pprint


def checkBoard(board, x, y):
    count = 0
    for _y in range(5):
        if board[x][_y] == -1:
            count = count + 1
    if count == 5:
        return True
    count = 0
    for _x in range(5):
        if board[_x][y] == -1:
            count = count + 1
    if count == 5:
        return True

    return False


def drawNumber(boards, draw):
    output = deepcopy(boards)
    lastWin = None
    toRemove = []
    for board in output:
        for x in range(5):
            for y in range(5):
                if board[x][y] == int(draw):
                    board[x][y] = -1
                    if checkBoard(board, x, y):
                        lastWin = board
                        toRemove.append(lastWin)

    for remove in toRemove:
        output.remove(remove)
    return output, lastWin


def puzzle(data):
    lineCount = 0
    draws = []
    boards = []
    first = True
    for line in data:
        line = line.replace('\n', '')
        chars = [line[i:i + 2] for i in range(0, len(line), 3)]
        if first:
            chars = line.split(',')
            first = False
        else:
            chars = [int(x) for x in chars]
        if lineCount == 0:
            draws = chars
        if lineCount > 1 and len(chars) > 0:
            boards.append(chars)

        lineCount = lineCount + 1

    boards = [boards[i:i+5] for i in range(0, len(boards), 5)]

    last = None
    lastDraw = 0
    for draw in draws:
        boards, lastWin = drawNumber(boards, draw)
        if lastWin != None:
            last = lastWin
            lastDraw = draw

    total = 0
    for x in range(5):
        for y in range(5):
            if last[x][y] != -1:
                total = total + last[x][y]
    print("Answer: " + str(total * int(lastDraw)))


data = open(__file__.replace('.py', 'input'))
start = time.perf_counter()
puzzle(data.readlines())
end = time.perf_counter()
print("Time: ", end="")
time_taken = end - start
if time_taken * 1000 < 1:
    print(time_taken * 1000000, end="")
    print("ns")
else:
    print(time_taken * 1000, end="")
    print("ms")
