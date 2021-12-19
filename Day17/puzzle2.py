import time
import math


def overshot(s, area):
    return s[0] > area[0][1] or s[1] < area[1][0]


def in_area(s, area):
    return s[0] >= area[0][0] and s[1] <= area[1][1]


def run_path(x, y, area):
    s = (0, 0)
    u = (x, y)
    a = (-1, -1)

    while not overshot(s, area):
        if in_area(s, area):
            return True
        s = (s[0] + u[0], s[1] + u[1])
        u = (u[0] + a[0], u[1] + a[1])
        if u[0] == 0:
            a = (0, -1)
    return False


def puzzle(data):
    total = 0
    area = [[], []]
    for line in data:
        line = line.replace('\n', '')
        line = line.split(':')[1]
        line = line.split(',')
        x = line[0].split('=')[1]
        y = line[1].split('=')[1]
        area[0] = x.split('..')
        area[1] = y.split('..')
    area = [[int(x) for x in y] for y in area]

    y = range(area[1][0], -(area[1][0] + 1) + 1)
    low_x = math.ceil(math.sqrt(1 + 8 * area[0][0]) - 1) / 2
    x = range(int(low_x), area[0][1] + 1)

    for _x in x:
        for _y in y:
            if run_path(_x, _y, area):
                total = total + 1

    print("Answer: " + str(total))


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
