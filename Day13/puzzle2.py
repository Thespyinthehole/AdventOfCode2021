def foldX(points, position):
    folded = set()
    for point in points:
        x = point[0]
        y = point[1]

        if x > position:
            x = position - (x - position)
        folded.add((x, y))
    return folded


def foldY(points, position):
    folded = set()
    for point in points:
        x = point[0]
        y = point[1]

        if y > position:
            y = position - (y - position)
        folded.add((x, y))
    return folded


def printpoints(points):
    maxX = 0
    maxY = 0
    for point in points:
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            print('#' if (x, y) in points else ' ', end='')
        print()


def puzzle(data):
    total = 0
    fold = False
    points = set()
    for line in data:
        line = line.replace('\n', '')
        if line == '':
            fold = True
            continue
        if fold:
            command = line.split(' ')[-1]
            command = command.split('=')
            if command[0] == 'x':
                points = foldX(points, int(command[1]))
            elif command[0] == 'y':
                points = foldY(points, int(command[1]))
            continue
        point = line.split(',')
        points.add((int(point[0]), int(point[1])))
    printpoints(points)
    # print()
    # print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
