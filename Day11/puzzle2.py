def energy_burst(x, y, grid, searched):
    if ((x, y) in searched) or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return
    grid[x][y] = grid[x][y] + 1
    if grid[x][y] == 10:
        searched.append((x, y))
        energy_burst(x - 1, y - 1, grid, searched)
        energy_burst(x - 1, y, grid, searched)
        energy_burst(x - 1, y + 1, grid, searched)
        energy_burst(x, y - 1, grid, searched)
        energy_burst(x, y, grid, searched)
        energy_burst(x, y + 1, grid, searched)
        energy_burst(x + 1, y - 1, grid, searched)
        energy_burst(x + 1, y, grid, searched)
        energy_burst(x + 1, y + 1, grid, searched)


def puzzle(data):
    grid = []
    for line in data:
        line = line.replace('\n', '')
        grid.append([int(x) for x in line])

    total = 0
    for i in range(1000):
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                search = []
                energy_burst(x, y, grid, search)

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] > 9:
                    count = count + 1
                    grid[x][y] = 0
        if count == 100:
            total = i + 1
            break
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
