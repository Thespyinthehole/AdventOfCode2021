import time
import itertools


class cube:
    def __init__(self, x, y, z, sort=False) -> None:
        self.x = [int(x[0]), int(x[1])]
        self.y = [int(y[0]), int(y[1])]
        self.z = [int(z[0]), int(z[1])]

        if sort:
            self.x = sorted(self.x)
            self.y = sorted(self.y)
            self.z = sorted(self.z)

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    def __repr__(self) -> str:
        return str(self)

    def get_overlap(self, other):
        if not(
                (self.x[1] >= other.x[0]) and
                (self.x[0] <= other.x[1]) and
                (self.y[1] >= other.y[0]) and
                (self.y[0] <= other.y[1]) and
                (self.z[1] >= other.z[0]) and
                (self.z[0] <= other.z[1])
        ):
            return None
        return cube(
            [
                max(self.x[0], other.x[0]),
                min(self.x[1], other.x[1])
            ],
            [
                max(self.y[0], other.y[0]),
                min(self.y[1], other.y[1])
            ],
            [
                max(self.z[0], other.z[0]),
                min(self.z[1], other.z[1])
            ])

    def lights_on(self):
        return (self.x[1] - self.x[0] + 1) * (self.y[1] - self.y[0] + 1) * (self.z[1] - self.z[0] + 1)


def puzzle(data):
    total = 0
    on = []
    for line in data:
        line = line.replace('\n', '')
        is_on = 'on' in line
        line = line.split(' ')[1].split(',')
        line = [x.split('=')[1].split('..') for x in line]
        box = cube(line[0], line[1], line[2], True)
        new_on = []
        for b in on:
            overlap = box.get_overlap(b)
            if overlap == None:
                new_on.append(b)
                continue

            low_x = [b.x[0], overlap.x[0] - 1]
            high_x = [overlap.x[1] + 1, b.x[1]]
            low_y = [b.y[0], overlap.y[0] - 1]
            high_y = [overlap.y[1] + 1, b.y[1]]
            low_z = [b.z[0], overlap.z[0] - 1]
            high_z = [overlap.z[1] + 1, b.z[1]]

            faces = [
                cube(low_x, overlap.y, overlap.z),
                cube(high_x, overlap.y, overlap.z),
                cube(overlap.x, low_y, overlap.z),
                cube(overlap.x, high_y, overlap.z),
                cube(overlap.x, overlap.y, low_z),
                cube(overlap.x, overlap.y, high_z)
            ]

            faces = [face for face in faces if face.lights_on() > 0]
            new_on = new_on + faces

            corners = [
                cube(low_x, low_y, low_z),
                cube(low_x, low_y, high_z),
                cube(low_x, high_y, low_z),
                cube(low_x, high_y, high_z),
                cube(high_x, low_y, low_z),
                cube(high_x, low_y, high_z),
                cube(high_x, high_y, low_z),
                cube(high_x, high_y, high_z)
            ]

            corners = [corner for corner in corners if corner.lights_on() > 0]
            new_on = new_on + corners

            edges = [
                cube(low_x, overlap.y, low_z),
                cube(low_x, overlap.y, high_z),
                cube(high_x, overlap.y, low_z),
                cube(high_x, overlap.y, high_z),

                cube(overlap.x, low_y, low_z),
                cube(overlap.x, low_y, high_z),
                cube(overlap.x, high_y, low_z),
                cube(overlap.x, high_y, high_z),

                cube(low_x, low_y, overlap.z),
                cube(low_x, high_y, overlap.z),
                cube(high_x, low_y, overlap.z),
                cube(high_x, high_y, overlap.z)
            ]
            edges = [edge for edge in edges if edge.lights_on() > 0]
            new_on = new_on + edges
        on = new_on
        if is_on:
            on.append(box)

    for box in on:
        lights = box.lights_on()
        total = total + lights
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
