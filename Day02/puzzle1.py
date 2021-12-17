




def puzzle(data):
    depth = 0
    horizontal = 0
    for line in data:
        command = line.replace('\n', '').split(' ')

        if command[0] == 'forward':
            horizontal = horizontal + int(command[1])
        elif command[0] == 'down':
            depth = depth + int(command[1])
        else:
            depth = depth - int(command[1])
    print("Answer: " + str(depth * horizontal))



data = open(__file__.replace('.py', 'input'))
import time
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
