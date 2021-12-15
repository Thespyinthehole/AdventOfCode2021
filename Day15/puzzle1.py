cache = {}


def shortest(grid, x, y):
    if x == 0 and y == 0:
        return 0
    if (x, y) in cache:
        return cache[(x, y)]
    right = shortest(grid, x - 1, y) if x - 1 >= 0 else float('inf')
    down = shortest(grid, x, y - 1) if y - 1 >= 0 else float('inf')
    value = min(right, down) + grid[y][x]
    cache[(x, y)] = value
    return value

def puzzle(data):
    total = 0
    grid = []
    for line in data:
        line = line.replace('\n', '')
        grid.append([])
        for chr in line:
            grid[-1].append(int(chr))

    total = shortest(grid, len(grid[0]) - 1, len(grid)-1)
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
