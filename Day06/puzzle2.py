
def puzzle(data):
    points = {x: 0 for x in range(9)}
    for line in data:
        line = line.replace('\n', '').split(',')
        for elem in line:
            elem = int(elem)
            points[elem] = points[elem] + 1

    for i in range(256):
        next = {x: 0 for x in range(9)}
        for x in range(8):
            next[x] = points[x + 1]
        next[8] = points[0]
        next[6] = next[6] + points[0]
        points = next

    total = sum(points.values())
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
