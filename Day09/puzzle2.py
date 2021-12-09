def findBasin(grid, x, y, basin):
    if grid[y][x] == 9 or (x, y) in basin:
        return []

    basin.append((x, y))
    if (x != 0):
        findBasin(grid, x - 1, y, basin)
    if (y != 0):
        findBasin(grid, x, y - 1, basin)
    if (x != len(grid[y]) - 1):
        findBasin(grid, x + 1, y, basin)
    if (y != len(grid) - 1):
        findBasin(grid, x, y + 1, basin)
    return basin


def puzzle(data):
    grid = []
    for line in data:
        line = list(line.replace('\n', ''))
        line = [int(x) for x in line]
        grid.append(line)

    searched = []
    sizes = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in searched:
                continue
            basin = []
            findBasin(grid, x, y, basin)
            if len(basin) != 0:
                searched = searched + basin
                sizes.append(len(basin))

    sizes = sorted(sizes)
    total = sizes[-1] * sizes[-2] * sizes[-3]
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
