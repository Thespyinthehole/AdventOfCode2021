def shortest(grid, distance):
    max_x = len(distance[0])
    max_y = len(distance)
    start = distance[0][0]
    distance[max_y - 1][max_x - 1] = grid[max_y - 1][max_x - 1]
    for y in range(max_y - 1, -1, -1):
        for x in range(max_x - 1, -1, -1):
            if x < max_x - 1:
                value = distance[y][x] + grid[y][x + 1]
                distance[y][x + 1] = min(distance[y][x + 1], value)
            if x > 0:
                value = distance[y][x] + grid[y][x - 1]
                distance[y][x - 1] = min(distance[y][x - 1], value)
            if y < max_y - 1:
                value = distance[y][x] + grid[y + 1][x]
                distance[y + 1][x] = min(distance[y + 1][x], value)
            if y > 0:
                value = distance[y][x] + grid[y - 1][x]
                distance[y - 1][x] = min(distance[y - 1][x], value)
    if distance[0][0] != start:
        shortest(grid, distance)


def puzzle(data):
    total = 0
    grid = []
    for line in data:
        line = line.replace('\n', '')
        grid.append([])
        for chr in line:
            grid[-1].append(int(chr))

    short = [[float('inf') for _ in row] for row in grid]
    shortest(grid, short)
    total = short[0][0] - grid[0][0]
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
