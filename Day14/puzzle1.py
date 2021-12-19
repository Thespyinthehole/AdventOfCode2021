import time


def puzzle(data):
    total = 0
    template = ''
    rules = None
    for line in data:
        line = line.replace('\n', '')
        if template == '':
            template = line
            continue
        if rules == None:
            rules = {}
            continue
        line = line.split(' -> ')
        rules[line[0]] = line[1]

    for _ in range(10):
        new_template = ''
        for i in range(len(template)):
            if i == 0:
                new_template = new_template + template[i]
                continue
            combo = template[i - 1] + template[i]
            new_template = new_template + rules[combo] + template[i]
        template = new_template

    res = {i: template.count(i) for i in set(template)}
    res = [(k, v) for k, v in sorted(res.items(), key=lambda item: item[1])]
    total = res[-1][1]-res[0][1]
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
