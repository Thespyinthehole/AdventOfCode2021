def puzzle(data):
    total = 0
    for line in data:
        line = line.replace('\n', '').split(' | ')
        inData = line[0].split(' ')
        outData = line[1].split(' ')
        for d in outData:
            length = len(d)
            if length in [2, 3, 4, 7]:
                total = total + 1
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
