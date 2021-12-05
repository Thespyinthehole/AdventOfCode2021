
def puzzle(data):
    points = {}
    lines = []
    for line in data:
        line = line.replace('\n', '').split(' -> ')
        line = [line[0].split(','), line[1].split(',')]
        v1 = [int(line[0][0]), int(line[0][1])]
        v2 = [int(line[1][0]), int(line[1][1])]
        dx = v2[0] - v1[0]
        dy = v2[1] - v1[1]

        if not (v1[0] == v2[0] or v1[1] == v2[1]):
            continue
        if dx != 0:
            m = dy / dx
            if m == -0.0:
                m = 0
            c = v1[1] - m * v1[0]
            def func(x): return m * x + c

            offset = 1 if dx > 0 else -1
            for x in range(v1[0], v2[0] + offset, offset):
                y = int(func(x))
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)] = 1
        else:
            m = dx / dy
            if m == -0.0:
                m = 0
            c = v1[0] - m * v1[1]
            def func(y): return m * y + c

            offset = 1 if dy > 0 else -1
            for y in range(v1[1], v2[1] + offset, offset):
                x = int(func(y))
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)] = 1

    points = dict(filter(lambda elem: elem[1] > 1, points.items()))
    print("Answer: " + str(len(points)))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
