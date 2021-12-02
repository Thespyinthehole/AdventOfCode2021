

def puzzle(data):
    depth = 0
    horizontal = 0
    aim = 0
    for line in data:
        command = line.replace('\n', '').split(' ')

        if command[0] == 'forward':
            horizontal = horizontal + int(command[1])
            depth = depth + aim * int(command[1])
        elif command[0] == 'down':
            aim = aim + int(command[1])
        else:
            aim = aim - int(command[1])
    print("Answer: " + str(depth * horizontal))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
