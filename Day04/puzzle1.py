from copy import deepcopy


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
    for board in output:
        for x in range(5):
            for y in range(5):
                if board[x][y] == int(draw):
                    board[x][y] = -1
                    if checkBoard(board, x, y):
                        return output, board
    return output, None


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

    for draw in draws:
        boards, board = drawNumber(boards, draw)
        if board != None:
            total = 0
            for x in range(5):
                for y in range(5):
                    if board[x][y] != -1:
                        total = total + board[x][y]
            print("Answer: " + str(total * int(draw)))
            break
    


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
