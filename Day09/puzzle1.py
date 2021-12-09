def puzzle(data):
    grid = []
    for line in data:
        line = list(line.replace('\n', ''))
        grid.append(line)

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            low = True
            if (x != 0):
                low = low and grid[y][x] < grid[y][x - 1]
            if (y != 0):
                low = low and grid[y][x] < grid[y - 1][x]
            if (x != len(grid[y]) - 1):
                low = low and grid[y][x] < grid[y][x + 1]
            if (y != len(grid) - 1):
                low = low and grid[y][x] < grid[y + 1][x]
            if low:
                total = total + 1 + int(grid[y][x])
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
