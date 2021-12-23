import time
import heapq


def print_map(positions):
    pos_map = {y: x for (x, y) in positions}
    for y in range(5):
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


def moves(position, positions):
    filled_positions = {x: y for (y, x) in positions}
    if (position[1][0], position[1][1] - 1) in filled_positions:
        return []
    if position[0] == 'A' and position[1][0] == 3:
        if position[1][1] == 3:
            return []
        if filled_positions[(3, 3)] == 'A':
            return []
    if position[0] == 'B' and position[1][0] == 5:
        if position[1][1] == 3:
            return []
        if filled_positions[(5, 3)] == 'B':
            return []
    if position[0] == 'C' and position[1][0] == 7:
        if position[1][1] == 3:
            return []
        if filled_positions[(7, 3)] == 'C':
            return []
    if position[0] == 'D' and position[1][0] == 9:
        if position[1][1] == 3:
            return []
        if filled_positions[(9, 3)] == 'D':
            return []

    mid_points = [(4, 1), (6, 1), (8, 1)]

    possible_moves = [(1, 1), (2, 1)] + mid_points + [(10, 1), (11, 1)]
    if position[1][1] == 1:
        possible_moves = []

    if position[0] == 'A':
        if (3, 3) in filled_positions and filled_positions[(3, 3)] == 'A':
            possible_moves = possible_moves + [(3, 2), (3, 3)]
        else:
            possible_moves = possible_moves + [(3, 3)]
    if position[0] == 'B':
        if (5, 3) in filled_positions and filled_positions[(5, 3)] == 'B':
            possible_moves = possible_moves + [(5, 2), (5, 3)]
        else:
            possible_moves = possible_moves + [(5, 3)]
    if position[0] == 'C':
        if (7, 3) in filled_positions and filled_positions[(7, 3)] == 'C':
            possible_moves = possible_moves + [(7, 2), (7, 3)]
        else:
            possible_moves = possible_moves + [(7, 3)]
    if position[0] == 'D':
        if (9, 3) in filled_positions and filled_positions[(9, 3)] == 'D':
            possible_moves = possible_moves + [(9, 2), (9, 3)]
        else:
            possible_moves = possible_moves + [(9, 3)]

    possible_moves = [x for x in possible_moves if not x in filled_positions]
    moves = []
    mid_points = [x for x in mid_points if x in filled_positions]
    for move in possible_moves:
        success = True
        for point in mid_points:
            if point[0] < position[1][0] and move[0] < point[0]:
                success = False
                break
            if point[0] > position[1][0] and move[0] > point[0]:
                success = False
                break
        if success:
            moves.append(move)
    return moves


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
    return a == 2 and b == 2 and c == 2 and d == 2


energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def cost(position, move):
    x = abs(position[1][0] - move[0])
    up = abs(position[1][1] - 1)
    down = abs(move[1] - 1)
    distance = x + up + down
    return distance * energy_costs[position[0]]


def add_states(board, base_energy, queue):
    easy_moves = board
    for position in board:
        _moves = moves(position, board)
        if len(_moves) == 1:
            easy_moves = [x for x in easy_moves if x[1] != position[1]]
            easy_moves.append((position[0], _moves[0]))
            base_energy = base_energy + cost(position, _moves[0])
    for position in easy_moves:
        _moves = moves(position, easy_moves)
        for _move in _moves:
            energy = base_energy + cost(position, _move)
            new_state = [x for x in easy_moves if x[1] != position[1]]
            new_state.append((position[0], _move))
            heapq.heappush(queue, (energy, sorted(new_state)))


def next_state(queue, done):
    state = heapq.heappop(queue)
    base_energy = state[0]
    board = state[1]
    if str(board) in done:
        return -1
    done.append(str(board))
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

    done = []
    queue = []
    heapq.heappush(queue, (0, positions))

    while len(queue) != 0:
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
