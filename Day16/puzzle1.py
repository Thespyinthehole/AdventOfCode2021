def parse_literal(bits, offset):
    number = ''
    while(bits[offset] == '1'):
        number = number + bits[offset + 1:offset + 5]
        offset = offset + 5
    number = number + bits[offset + 1:offset + 5]
    return offset + 5, 0


def parse_15_operator(bits, offset):
    length = int(bits[offset:offset + 15], 2)
    offset = offset + 15
    start_offset = offset
    version = 0
    while (offset - start_offset < length):
        offset, v = parse_packet(bits, offset)
        version = version + v
    return offset, version


def parse_11_operator(bits, offset):
    length = int(bits[offset:offset + 11], 2)
    offset = offset + 11
    version = 0
    for _ in range(length):
        offset, v = parse_packet(bits, offset)
        version = version + v
    return offset, version


def parse_packet(bits, offset=0):
    version = int(bits[offset:offset + 3], 2)
    type = bits[offset + 3:offset + 6]
    v = 0
    if type == '100':
        offset, v = parse_literal(bits, offset + 6)
        return offset, version + v
    length_type = bits[offset+6]
    if length_type == '0':
        offset, v = parse_15_operator(bits, offset + 7)
    if length_type == '1':
        offset, v = parse_11_operator(bits, offset + 7)
    return offset, version + v


def puzzle(data):
    total = 0
    bits = ''
    for line in data:
        line = line.replace('\n', '')
        for chr in line:
            bits = bits + bin(int(chr, 16))[2:].zfill(4)
    _, total = parse_packet(bits)
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
