

def puzzle(data):
    depth = -1
    increased = 0
    for line in data:
        newDepth = int(line[:-1])
        if depth == -1:
            depth = newDepth
            continue
        if newDepth > depth:
            increased = increased + 1
        depth = newDepth
    print("Answer: " + str(increased))

data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())