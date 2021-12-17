import math
from typing import Mapping


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

    u = 0
    y = area[1]
    n = -(y[0] + 1)
    total = int(n * (n + 1) / 2)
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
