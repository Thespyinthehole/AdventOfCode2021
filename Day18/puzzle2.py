from os import getlogin
import time
from copy import deepcopy
import math


def depth(L):
    return isinstance(L, list) and len(L) and max(map(depth, L)) + 1


def deepest(L):
    max_depth = 0
    index = 0
    for i, v in enumerate(L):
        d = depth(v)
        if d > max_depth:
            max_depth = d
            index = i
    return index


def get_depth_path(L):
    index = deepest(L)
    if isinstance(L[index], list):
        path, value = get_depth_path(L[index])
        return [index] + path, value
    return [], L


def get_left(number, path):
    if not path:
        return None
    found = get_left(number[path[0]], path[1:])
    if found:
        return [path[0]] + found
    if 1 <= path[0]:
        return [path[0]-1]
    return None


def get_right(number, path):
    if not path:
        return None
    found = get_right(number[path[0]], path[1:])
    if found:
        return [path[0]] + found
    if len(number) > path[0] + 1:
        return [path[0]+1]
    return None


def set_left(number, path, value):
    if path == []:
        if isinstance(number[0], list):
            set_left(number[0], [], value)
        else:
            number[0] = number[0] + value
    else:
        if len(path) == 1 and not isinstance(number[path[0]], list):
            number[path[0]] = number[path[0]] + value
        else:
            set_left(number[path[0]], path[1:], value)


def set_right(number, path, value):
    if path == []:
        if isinstance(number[1], list):
            set_right(number[1], [], value)
        else:
            number[1] = number[1] + value
    else:
        if len(path) == 1 and not isinstance(number[path[0]], list):
            number[path[0]] = number[path[0]] + value
        else:
            set_right(number[path[0]], path[1:], value)


def set_value(number, path):
    if len(path) > 1:
        set_value(number[path[0]], path[1:])
    else:
        number[path[0]] = 0


def explode(number):
    output = deepcopy(number)
    path, [lhs, rhs] = get_depth_path(number)
    lhs_path = get_left(output, path)
    if lhs_path:
        set_right(output, lhs_path, lhs)
    rhs_path = get_right(output, path)
    if rhs_path:
        set_left(output, rhs_path, rhs)

    set_value(output, path)
    return output


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


def split(number):
    for i, v in enumerate(number):
        if isinstance(v, list):
            updated, use = split(v)
            if use:
                out = deepcopy(number)
                out[i] = updated
                return out, True
        elif v >= 10:
            out = deepcopy(number)
            out[i] = [math.floor(v / 2), math.ceil(v / 2)]
            return out, True
    return number, False


def reduce(number):
    if depth(number) > 4:
        return reduce(explode(number))

    if sum(i >= 10 for i in flatten(number)):
        number, _ = split(number)
        return reduce(number)
    return number


def add(a, b):
    return reduce([a] + [b])


def magnitude(number):
    if isinstance(number, list):
        return 3 * magnitude(number[0]) + 2 * magnitude(number[1])
    return number


def puzzle(data):
    total = 0
    numbers = []
    for line in data:
        line = line.replace('\n', '')
        numbers.append(eval(line))


    for i, x in enumerate(numbers):
        for o, y in enumerate(numbers):
            if i <= o:
                continue
            total = max(total, magnitude(add(x, y)), magnitude(add(y, x)))
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
