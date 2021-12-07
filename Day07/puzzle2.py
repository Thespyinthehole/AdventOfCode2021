

def getFuel(target, distances):
    fuel = 0
    for key in distances:
        distance = abs(target - key)
        fuel = fuel + (distance * (distance + 1) / 2) * distances[key]
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
    print("Answer: " + str(int(actualFuel)))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
