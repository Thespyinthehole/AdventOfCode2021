

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