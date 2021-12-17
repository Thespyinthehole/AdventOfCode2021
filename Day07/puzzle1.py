

def getFuel(target, distances):
    fuel = 0
    for key in distances:
        fuel = fuel + abs(target - key) * distances[key]
    return fuel

def puzzle(data):
    actualFuel = float('inf')
    distances = {}
    minV = float('inf')
    maxV = float('-inf')
    for line in data:
        line = line.replace('\n', '').split(',')
        for value in line:
            value = int(value)
            if value in distances:
                distances[value] = distances[value] + 1
            else:
                distances[value] = 1 
            minV = min(minV, value)
            maxV = max(maxV, value)
            
        for value in range(minV, maxV):
            fuel = getFuel(value, distances)
            if fuel < actualFuel:
                actualFuel = fuel
    print("Answer: " + str(actualFuel))


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
