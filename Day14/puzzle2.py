import time
from typing import Counter


rule_days = {}


def rule_after_days(rules, element, days):
    if days == 0:
        return Counter(element)
    if (element, days) in rule_days:
        return rule_days[(element, days)].copy()
    rule = rules[element]
    a = element[0] + rule
    b = rule + element[1]
    count_a = rule_after_days(rules, a, days - 1)
    count_b = rule_after_days(rules, b, days - 1)

    count = Counter(count_a)
    count.update(count_b)
    count[rule] -= 1
    rule_days[(element, days)] = count
    return count


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

    count = Counter()
    for i in range(len(template)):
        count.update(template[i])
        if i == 0:
            continue
        combo = template[i - 1] + template[i]
        value = rule_after_days(rules, combo, 40)
        count.update(value)

        count[combo[0]] -= 1
        count[combo[1]] -= 1
    count = sorted(count.items(), key=lambda pair: pair[1])
    total = count[-1][1] - count[0][1]
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
