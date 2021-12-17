def puzzle(data):
    total = 0
    for line in data:
        line = line.replace('\n', '')
        stack = []
        chr = ''
        for chr in line:
            if chr == '(' or chr == '[' or chr == '<' or chr == '{':
                stack.append(chr)
            elif chr == ')':
                top = stack.pop()
                if top != '(':
                    total = total + 3
                    break
            elif chr == '}':
                top = stack.pop()
                if top != '{':
                    total = total + 1197
                    break
            elif chr == '>':
                top = stack.pop()
                if top != '<':
                    total = total + 25137
                    break
            elif chr == ']':
                top = stack.pop()
                if top != '[':
                    total = total + 57
                    break
    print("Answer: " + str(total))


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
