import time

def puzzle(data):
    total = 0
    lines = [[]]
    i = 0
    for line in data:
        line = line.replace('\n', '')
        if i == 4 or i == 5 or i == 15:
            lines[-1].append(int(line.split(' ')[2]))
        i = (i + 1) % 18
        if i == 0:
            lines.append([])
    lines = lines[:-1]
    stack = []
    inp = [0 for _ in range(14)]
    for i, [a, b, c] in enumerate(lines):
        if b >= 10:
            stack.append((i, [a, b, c]))
        else:
            (i1, [a1, b1, c1]) = stack.pop()
            if c1 + b > 0:
                inp[i1] = 1
                inp[i] = 1 + (c1 + b)
            else:
                inp[i] = 1
                inp[i1] = 1 - (c1 + b)
    inp = [str(x) for x in inp]
    total = ''.join(inp)
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
