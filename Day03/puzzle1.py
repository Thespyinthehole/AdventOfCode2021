

import time


def puzzle(data):
    counts = []
    first = True
    length = 0
    for line in data:
        chars = list(line.replace('\n', ''))
        if first:
            first = False
            length = len(chars)
            counts = [0 for _ in range(length)]
        for i in range(length):
            counts[i] = counts[i] + (-1 if chars[i] == '0' else 1)
    gammaRate = ''
    epsilonRate = ''
    for char in counts:
        if char >= 0:
            gammaRate += '1'
            epsilonRate += '0'
        else:
            gammaRate += '0'
            epsilonRate += '1'

    gammaValue = int(gammaRate, 2)
    epsilonValue = int(epsilonRate, 2)
    print("Answer: " + str(gammaValue * epsilonValue))


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
