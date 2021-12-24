import time
import heapq


def print_map(positions):
    pos_map = {y: x for (x, y) in positions}
    for y in range(7):
        for x in range(13):
            if (x, y) in pos_map:
                print(pos_map[(x, y)], end='')
                continue
            if y == 1 and x > 0 and x < 12:
                print(' ', end='')
                continue
            if y > 1 and x == 3 and y < 4:
                print(' ', end='')
                continue
            if y > 1 and x == 5 and y < 4:
                print(' ', end='')
                continue
            if y > 1 and x == 7 and y < 4:
                print(' ', end='')
                continue
            if y > 1 and x == 9 and y < 4:
                print(' ', end='')
                continue
            print('#', end='')
        print()


def all_room_moves(type):
    if type == 'A':
        return [(3, 2), (3, 3), (3, 4), (3, 5)]
    if type == 'B':
        return [(5, 2), (5, 3), (5, 4), (5, 5)]
    if type == 'C':
        return [(7, 2), (7, 3), (7, 4), (7, 5)]
    if type == 'D':
        return [(9, 2), (9, 3), (9, 4), (9, 5)]


def room_moves(type, positions):
    room = all_room_moves(type)
    room.reverse()
    for m in room:
        if not m in positions:
            return [m]
        if positions[m] != type:
            return []
    return []


def hallway_moves():
    return [(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)]


def is_blocked(start, end, positions):
    for hallway in hallway_moves():
        if not hallway in positions:
            continue
        if (start[0] - hallway[0]) * (end[0] - hallway[0]) < 0:
            return True

    if start[1] == 3 and (start[0], 2) in positions:
        return True
    if start[1] == 4 and (start[0], 3) in positions:
        return True
    if start[1] == 5 and (start[0], 4) in positions:
        return True

    if end[1] == 3 and (end[0], 2) in positions:
        return True
    if end[1] == 4 and (end[0], 3) in positions:
        return True
    if end[1] == 5 and (end[0], 4) in positions:
        return True

    return False


def in_room_safely(type, position, positions):
    x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}[type]
    if position[0] != x:
        return False
    for y in range(position[1], 6):
        if positions[(x, y)] != type:
            return False
    return True


def moves(pod, pods):
    positions = {x: y for (y, x) in pods}
    if in_room_safely(pod[0], pod[1], positions):
        return []
    all_moves = room_moves(pod[0], positions)
    if pod[1][1] != 1:
        all_moves = all_moves + hallway_moves()

    all_moves = [
        x
        for x in all_moves
        if (not x in positions) and
        not is_blocked(pod[1], x, positions)
    ]
    return all_moves


def is_done(positions):
    a = 0
    b = 0
    c = 0
    d = 0
    for position in positions:
        if position[0] == 'A' and position[1][0] == 3:
            a = a + 1
        if position[0] == 'B' and position[1][0] == 5:
            b = b + 1
        if position[0] == 'C' and position[1][0] == 7:
            c = c + 1
        if position[0] == 'D' and position[1][0] == 9:
            d = d + 1
    return a == 4 and b == 4 and c == 4 and d == 4


energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def cost(position, move):
    x = abs(position[1][0] - move[0])
    up = abs(position[1][1] - 1)
    down = abs(move[1] - 1)
    distance = x + up + down
    return distance * energy_costs[position[0]]


def add_states(board, base_energy, queue):
    # print_map(board)
    for position in board:
        _moves = moves(position, board)
        for _move in _moves:
            energy = base_energy + cost(position, _move)
            new_state = [x for x in board if x[1] != position[1]]
            new_state.append((position[0], _move))
            heapq.heappush(queue, (energy, sorted(new_state)))


def next_state(queue, done):
    state = heapq.heappop(queue)
    base_energy = state[0]
    board = state[1]
    if str(board) in done:
        return -1
    done.add(str(board))
    if is_done(board):
        return base_energy
    add_states(board, base_energy, queue)
    return 0


def puzzle(data):
    total = 0
    positions = []
    y = 2
    for line in data:
        line = line.replace('\n', '')
        if 'A' in line or 'B' in line or 'C' in line:
            x = 3
            for c in line.split('#'):
                if c in ['A', 'B', 'C', 'D']:
                    positions.append((c, (x, y)))
                    x = x + 2
            y = y + 1

    done = set()
    queue = []
    heapq.heappush(queue, (0, positions))
    states = 0
    while len(queue) != 0:
        states = states + 1
        mode = next_state(queue, done)
        if mode == -1:
            continue
        elif mode != 0:
            total = mode
            break
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
