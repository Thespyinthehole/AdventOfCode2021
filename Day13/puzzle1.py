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
            break
        point = line.split(',')
        points.add((int(point[0]), int(point[1])))
    total = len(points)
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
import time
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
