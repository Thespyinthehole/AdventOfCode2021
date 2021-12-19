import time


def puzzle(data):
    total = 0
    for line in data:
        line = line.replace('\n', '').split(' | ')
        inData = line[0].split(' ')
        outData = line[1].split(' ')
        lengths = {x: [] for x in range(2, 8)}
        possibleMappings = {x: {} for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}
        digitMap = {x: set({}) for x in range(10)}
        for i in inData:
            length = len(i)
            lengths[length].append(set(sorted(i)))

        digitMap[1] = lengths[2][0]
        digitMap[7] = lengths[3][0]
        digitMap[4] = lengths[4][0]
        digitMap[8] = lengths[7][0]

        possibleMappings['c'] = lengths[2][0]
        possibleMappings['f'] = lengths[2][0]
        possibleMappings['a'] = list(lengths[3][0] - lengths[2][0])[0]
        tmp = lengths[4][0] - lengths[2][0]
        possibleMappings['b'] = tmp

        for s in lengths[6]:
            possibleMappings['b'] = possibleMappings['b'].intersection(s)

        possibleMappings['d'] = list(tmp - possibleMappings['b'])[0]
        possibleMappings['b'] = list(possibleMappings['b'])[0]

        for s in lengths[6]:
            if not possibleMappings['d'] in s:
                digitMap[0] = s
            elif len(s.intersection(lengths[2][0])) != 2:
                digitMap[6] = s
            else:
                digitMap[9] = s
        for s in lengths[5]:
            if len(s.intersection(lengths[2][0])) == 2:
                digitMap[3] = s
            elif possibleMappings['b'] in s:
                digitMap[5] = s
            else:
                digitMap[2] = s

        inverseDigitMap = {''.join(value): key for key,
                           value in digitMap.items()}
        output = ''
        for d in outData:
            key = ''.join(set(sorted(d)))
            output = output + str(inverseDigitMap[key])
        total = total + int(output)
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
