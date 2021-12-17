
def getCount(list):
    length = len(list[0])
    counts = [0 for _ in range(length)]
    for o in range(len(list)):
        for i in range(length):
            counts[i] = counts[i] + (-1 if list[o][i] == '0' else 1)
    return counts


def resolveCriteria(list, bit,  A, B):
    if len(list) == 1:
        return list
    temp = list.copy()
    counts = getCount(list)
    keep = A if counts[bit] >= 0 else B
    for i in range(len(list)):
        if list[i][bit] != keep:
            temp.remove(list[i])
    return temp.copy()


def puzzle(data):
    o2 = []
    co2 = []
    for line in data:
        chars = list(line.replace('\n', ''))
        o2.append(chars)
        co2.append(chars)

    length = len(o2[0])

    for bit in range(length):
        o2 = resolveCriteria(o2, bit, '1', '0')
        co2 = resolveCriteria(co2, bit, '0', '1')

    o2 = "".join(o2[0])
    co2 = "".join(co2[0])
    print("Answer: " + str(int(o2, 2) * int(co2, 2)))


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
