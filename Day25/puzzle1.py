import time


def print_grid(x, y, cucumbers):
    for _y in range(y):
        for _x in range(x):
            if (_x, _y) in cucumbers:
                print(cucumbers[(_x, _y)], end='')
            else:
                print('.', end='')
        print()


def puzzle(data):
    total = 0
    cucumbers = {}
    y = 0
    x = 0
    for line in data:
        line = line.replace('\n', '')
        line = list(line)
        x = len(line)
        for i, c in enumerate(line):
            if c == '.':
                continue
            cucumbers[(i, y)] = c
        y = y + 1

    changed = True
    while changed:
        changed = False
        east = {pos: c for pos, c in cucumbers.items() if c == '>'}
        next = {pos: c for pos, c in cucumbers.items() if c == 'v'}

        for pos in sorted(east.keys()):
            pos_x = (pos[0] + 1) % x
            new_pos = (pos_x, pos[1])
            if new_pos in cucumbers:
                next[pos] = '>'
            else:
                next[new_pos] = '>'
                changed = True

        cucumbers = next
        south = {pos: c for pos, c in cucumbers.items() if c == 'v'}
        next = {pos: c for pos, c in cucumbers.items() if c == '>'}

        for pos in sorted(south.keys()):
            pos_y = (pos[1] + 1) % y
            new_pos = (pos[0], pos_y)
            if new_pos in cucumbers:
                next[pos] = 'v'
            else:
                next[new_pos] = 'v'
                changed = True
        cucumbers = next
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
