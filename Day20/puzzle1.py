import time
state = 0


def get_chars(image, x, y):
    chars = []
    for _y in [-1, 0, 1]:
        pos_y = y + _y
        for _x in [-1, 0, 1]:
            pos_x = x + _x
            if pos_y < 0 or pos_x < 0 or pos_y >= len(image) or pos_x >= len(image[0]):
                    chars.append('.' if state == 0 else '#')
            else:
                chars.append(image[pos_y][pos_x])
    return chars


def enhanced_char(chars, enhancement):
    index = 0
    for i, char in enumerate(chars):
        index = index + (2 ** (8 - i) if char == '#' else 0)
    return enhancement[index]


def get_new_image(image, enhancement):
    new_image = []
    lit = 0
    for _y in range(-1, len(image) + 1):
        new_image.append([])
        for _x in range(-1, len(image[0]) + 1):
            char = enhanced_char(get_chars(image, _x, _y), enhancement)
            lit = lit + (1 if char == '#'else 0)
            new_image[-1].append(char)
    return new_image, lit


def puzzle(data):
    global state
    total = 0
    enhancement = []
    image = []
    for line in data:
        line = line.replace('\n', '')
        if enhancement == []:
            enhancement = list(line)
            continue
        if len(line) == 0:
            continue
        image.append(list(line))

        
    image, _ = get_new_image(image, enhancement)
    if enhancement[0] == '#':
        state = 1
    _, total = get_new_image(image, enhancement)

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
