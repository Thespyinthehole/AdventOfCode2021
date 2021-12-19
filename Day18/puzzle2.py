import time
import math
import itertools
from copy import deepcopy


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
            lhs = set_left(number[0], [], value)
            return [lhs, number[1]]
        else:
            return [number[0] + value, number[1]]

    if len(path) == 1 and not isinstance(number[path[0]], list):
        if path[0] == 0:
            return [number[path[0]] + value, number[1]]
        return [number[0], number[path[0]] + value]
    else:
        side = set_left(number[path[0]], path[1:], value)
        if path[0] == 0:
            return [side, number[1]]
        return [number[0], side]

    # if path == []:
    #     if isinstance(number[1], list):
    #         rhs = set_right(number[1], [], value)
    #         return [number[0], rhs]
    #     else:
    #         return [number[0], number[1] + value]

    # if len(path) == 1 and not isinstance(number[path[0]], list):
    #     if path[0] == 0:
    #         return [number[path[0]] + value, number[1]]
    #     return [number[0], number[path[0]] + value]
    # else:
    #     side = set_right(number[path[0]], path[1:], value)
    #     if path[0] == 0:
    #         return [side, number[1]]
    #     return [number[0], side]


def set_right(number, path, value):
    if path == []:
        if isinstance(number[1], list):
            rhs = set_right(number[1], [], value)
            return [number[0], rhs]
        else:
            return [number[0], number[1] + value]

    if len(path) == 1 and not isinstance(number[path[0]], list):
        if path[0] == 0:
            return [number[path[0]] + value, number[1]]
        return [number[0], number[path[0]] + value]
    else:
        side = set_right(number[path[0]], path[1:], value)
        if path[0] == 0:
            return [side, number[1]]
        return [number[0], side]


def set_value(number, path):
    if len(path) > 1:
        side = set_value(number[path[0]], path[1:])
        if path[0] == 0:
            return [side, number[1]]
        return [number[0], side]
    else:
        if path[0] == 0:
            return [0, number[1]]
        return [number[0], 0]


def explode(number):
    path, [lhs, rhs] = get_depth_path(number)
    lhs_path = get_left(number, path)
    if lhs_path:
        number = set_right(number, lhs_path, lhs)
    rhs_path = get_right(number, path)
    if rhs_path:
        number = set_left(number, rhs_path, rhs)
    return set_value(number, path)


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
                number[i] = updated
                return number, True
        elif v >= 10:
            number[i] = [math.floor(v / 2), math.ceil(v / 2)]
            return number, True
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

    cross = itertools.product(numbers, numbers)
    # for i, x in enumerate(numbers):
    #     for o, y in enumerate(numbers):
    #         if i == o:
    #             continue
    # print(explode([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]))
    for (x, y) in cross:
        if x == y:
            continue
        total = max(total, magnitude(add(x, y)))

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
