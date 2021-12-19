import time
import math
import itertools

def get_beacon_pairs(scanner_a, scanner_b, distances):
    beacons = {}
    for distance in distances:
        beacons_a = scanner_a[distance]
        beacons_b = scanner_b[distance]

        a_1 = beacons_a[0]
        a_2 = beacons_a[1]
        if a_1 in beacons:
            beacons[a_1] = beacons[a_1].intersection(set(beacons_b))
        else:
            beacons[a_1] = set(beacons_b)

        if a_2 in beacons:
            beacons[a_2] = beacons[a_2].intersection(set(beacons_b))
        else:
            beacons[a_2] = set(beacons_b)
    return [(a, list(b)[0]) for a, b in beacons.items() if len(b) > 0]


def rotations():
    return [
        lambda x, y, z: (-z, -y, -x),
        lambda x, y, z: (-z, -x, y),
        lambda x, y, z: (-z, x, -y),
        lambda x, y, z: (-z, y, x),
        lambda x, y, z: (-y, -z, x),
        lambda x, y, z: (-y, -x, -z),
        lambda x, y, z: (-y, x, z),
        lambda x, y, z: (-y, z, -x),
        lambda x, y, z: (-x, -z, -y),
        lambda x, y, z: (-x, -y, z),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (-x, z, y),
        lambda x, y, z: (z, -y, x),
        lambda x, y, z: (z, -x, -y),
        lambda x, y, z: (z, x, y),
        lambda x, y, z: (z, y, -x),
        lambda x, y, z: (y, -z, -x),
        lambda x, y, z: (y, -x, z),
        lambda x, y, z: (y, x, -z),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (x, -z, y),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (x, z, -y)
    ]


def position(pairs):
    positions = {}
    rotation = {}
    (x0, y0, z0) = pairs[0][0]
    for rot in rotations():
        (x1, y1, z1) = pairs[0][1]
        (x, y, z) = rot(x1, y1, z1)
        pos = (x0 - x, y0 - y, z0 - z)
        rotation[pos] = rot
        positions[pos] = 1

    for pair in pairs[1:]:
        (x0, y0, z0) = pair[0]
        for rot in rotations():
            (x1, y1, z1) = pair[1]
            (x, y, z) = rot(x1, y1, z1)
            pos = (x0 - x, y0 - y, z0 - z)
            if pos in positions:
                positions[pos] = positions[pos] + 1
    pos = list(filter(lambda elem: elem[1] > 1, positions.items()))[0][0]
    return pos, rotation[pos]


def get_distances(scanner):
    distances = {}
    for i, beacon_a in enumerate(scanner):
        for o, beacon_b in enumerate(scanner):
            if i >= o:
                continue
            x = beacon_a[0] - beacon_b[0]
            y = beacon_a[1] - beacon_b[1]
            z = beacon_a[2] - beacon_b[2]
            distance = math.sqrt(x * x + y * y + z * z)
            distances[distance] = (beacon_a, beacon_b)
    return distances


def common_beacons(scanner_a, scanner_b):
    a_distances = get_distances(scanner_a)
    b_distances = get_distances(scanner_b)
    a_dis = set(a_distances.keys())
    b_dis = set(b_distances.keys())
    common_distances = a_dis.intersection(b_dis)
    return get_beacon_pairs(a_distances, b_distances, common_distances)


def align(scanner, position, rot):
    out = []
    (x0, y0, z0) = position
    for point in scanner:
        (x1, y1, z1) = point
        (x, y, z) = rot(x1, y1, z1)
        out.append((x0 + x, y0 + y, z0 + z))
    return out


def puzzle(data):
    total = 0
    scanners = []
    for line in data:
        line = line.replace('\n', '')
        if len(line) == 0:
            continue
        if '---' in line:
            scanners.append([])
            continue
        line = line.split(',')
        scanners[-1].append((int(line[0]), int(line[1]), int(line[2])))

    aligned = [False for _, _ in enumerate(scanners)]
    aligned[0] = True
    positions = [(0,0,0)]
    while False in aligned:
        for i, scanner_a in enumerate(scanners):
            for o, scanner_b in enumerate(scanners):
                if i == o or not aligned[i] or aligned[o]:
                    continue
                beacons = common_beacons(scanner_a, scanner_b)
                if len(beacons) < 12:
                    continue

                pos, rot = position(beacons)
                positions.append(pos)
                alignment = align(scanner_b, pos, rot)
                scanners[o] = alignment
                aligned[o] = True


    for ((x0, y0, z0), (x1, y1, z1)) in itertools.permutations(positions,2):
        xdis = abs(x0 - x1)
        ydis = abs(y0 - y1)
        zdis = abs(z0 - z1)
        total = max(total, xdis + ydis + zdis)
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
