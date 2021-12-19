import time


def generate_paths(cave, caves, path=[], small=[]):
    new_path = path.copy()
    new_path.append(cave)
    new_small = small.copy()
    if cave.islower():
        new_small.append(cave)

    out_paths = []
    for passage in caves[cave]:
        if passage == 'end':
            out_paths.append(['end'])
            continue
        if passage in small:
            continue
        next_paths = generate_paths(passage, caves, new_path, new_small)
        for next in next_paths:
            out_paths.append([passage] + next)
    return out_paths


def puzzle(data):
    total = 0
    caves = {}
    start = []
    paths = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split('-')
        caveA = line[0]
        caveB = line[1]

        if not caveA in caves:
            caves[caveA] = []

        if not caveB in caves:
            caves[caveB] = []

        if not caveB in caves[caveA]:
            caves[caveA].append(caveB)
        if not caveA in caves[caveB]:
            caves[caveB].append(caveA)

    paths = generate_paths('start', caves)
    total = len(paths)
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
