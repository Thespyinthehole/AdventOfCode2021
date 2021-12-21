import time


def puzzle(data):
    total = 0
    players = []
    for line in data:
        line = line.replace('\n', '')
        players.append([int(line.split(': ')[1]), 0])

    turn = 0
    while players[0][1] < 1000 and players[1][1] < 1000:
        roll = 9 * turn + 6
        player = players[turn % 2]
        player[0] = (player[0] + roll - 1) % 10 + 1
        player[1] = player[1] + player[0]
        players[turn % 2] = player
        turn = turn + 1
    total = turn * 3 * players[turn % 2][1]
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
