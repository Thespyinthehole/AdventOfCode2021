import time
import math


def parse_literal(bits, offset):
    number = ''
    while(bits[offset] == '1'):
        number = number + bits[offset + 1:offset + 5]
        offset = offset + 5
    number = number + bits[offset + 1:offset + 5]
    return offset + 5, 0, int(number, 2)


def evaluate(values, type):
    if type == '000':
        return sum(values)
    if type == '001':
        return math.prod(values)
    if type == '010':
        return min(values)
    if type == '011':
        return max(values)
    if type == '101':
        return 1 if values[0] > values[1] else 0
    if type == '110':
        return 1 if values[0] < values[1] else 0
    if type == '111':
        return 1 if values[0] == values[1] else 0


def parse_15_operator(bits, offset, type):
    length = int(bits[offset:offset + 15], 2)
    offset = offset + 15
    start_offset = offset
    version = 0
    values = []
    while (offset - start_offset < length):
        offset, v, value = parse_packet(bits, offset)
        values.append(value)
        version = version + v
    return offset, version, evaluate(values, type)


def parse_11_operator(bits, offset, type):
    length = int(bits[offset:offset + 11], 2)
    offset = offset + 11
    version = 0
    values = []
    for _ in range(length):
        offset, v, value = parse_packet(bits, offset)
        values.append(value)
        version = version + v
    return offset, version, evaluate(values, type)


def parse_packet(bits, offset=0):
    version = int(bits[offset:offset + 3], 2)
    type = bits[offset + 3:offset + 6]
    v = 0
    value = 0
    if type == '100':
        offset, v, value = parse_literal(bits, offset + 6)
        return offset, version + v, value
    length_type = bits[offset+6]
    if length_type == '0':
        offset, v, value = parse_15_operator(bits, offset + 7, type)
    if length_type == '1':
        offset, v, value = parse_11_operator(bits, offset + 7, type)
    return offset, version + v, value


def puzzle(data):
    total = 0
    bits = ''
    for line in data:
        line = line.replace('\n', '')
        for chr in line:
            bits = bits + bin(int(chr, 16))[2:].zfill(4)
    _, _, total = parse_packet(bits)
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
