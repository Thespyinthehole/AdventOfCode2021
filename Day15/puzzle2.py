import time


def grid_value(grid, y, x):
    max_x = len(grid[0])
    max_y = len(grid)
    value = grid[y % max_y][x % max_x]
    offset = value + int(x / max_x) + int(y / max_y)
    scaled = (offset - 1) % 9 + 1
    return scaled


def shortest(grid, distance):
    max_x = len(distance[0])
    max_y = len(distance)
    start = distance[0][0]
    distance[max_y - 1][max_x - 1] = grid_value(grid, max_y - 1, max_x - 1)
    for y in range(max_y - 1, -1, -1):
        for x in range(max_x - 1, -1, -1):
            if x < max_x - 1:
                value = distance[y][x] + grid_value(grid, y, x + 1)
                distance[y][x + 1] = min(distance[y][x + 1], value)
            if x > 0:
                value = distance[y][x] + grid_value(grid, y, x - 1)
                distance[y][x - 1] = min(distance[y][x - 1], value)
            if y < max_y - 1:
                value = distance[y][x] + grid_value(grid, y + 1, x)
                distance[y + 1][x] = min(distance[y + 1][x], value)
            if y > 0:
                value = distance[y][x] + grid_value(grid, y - 1, x)
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

    short = [
        [
            float('inf') for _ in range(len(grid[0]) * 5)
        ]
        for _ in range(len(grid) * 5)
    ]
    shortest(grid, short)
    total = short[0][0] - grid[0][0]
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
