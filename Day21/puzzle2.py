import time
rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
cache = {}


def universes(player_a, player_b, turn):
    global cache
    if player_a[1] >= 21:
        return (1, 0)
    if player_b[1] >= 21:
        return (0, 1)

    if str((player_a, player_b, turn)) in cache:
        return cache[str((player_a, player_b, turn))]
    value_a = 0
    value_b = 0
    if turn == 0:
        for i in range(3, 10):
            position = (player_a[0] + i - 1) % 10 + 1
            player = [position, player_a[1] + position]
            (a_win, b_win) = universes(player, player_b, 1)
            value_a = value_a + rolls[i] * a_win
            value_b = value_b + rolls[i] * b_win
    else:
        for i in range(3, 10):
            position = (player_b[0] + i - 1) % 10 + 1
            player = [position, player_b[1] + position]
            (a_win, b_win) = universes(player_a, player, 0)
            value_a = value_a + rolls[i] * a_win
            value_b = value_b + rolls[i] * b_win
    cache[str((player_a, player_b, turn))] = (value_a, value_b)
    return (value_a, value_b)


def puzzle(data):
    total = 0
    players = []
    for line in data:
        line = line.replace('\n', '')
        players.append(int(line.split(': ')[1]))

    (a_win, b_win) = universes([players[0], 0], [players[1], 0], 0)
    total = max(a_win, b_win)
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
