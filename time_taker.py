import subprocess


def get_time(filename):
    out = subprocess.check_output(['python3', filename]).decode("utf-8")
    time_str = out.split('Time: ')[1]
    time = float(time_str[:time_str.index('s') - 1])
    return time, 'ns' in time_str


def average(filename, times=1):
    total = 0
    all_ns = True
    for _ in range(times):
        time, ns = get_time(filename)
        total = total + (time / 1000) if ns else time
        all_ns = all_ns and ns

    total = total * 1000 if all_ns else total
    return total / times, total, all_ns


readme = open('README.md', 'w')
full = 0
for day in range(19):
    dir = 'Day' + str(day + 1).zfill(2)
    readme.write('# ' + dir + '\n')

    avg1, total1, ns1 = average(dir + '/puzzle1.py')
    avg2, total2, ns2 = average(dir + '/puzzle2.py')
    full = full + (total1 / 1000 if ns1 else total1) + \
        (total2 / 1000 if ns2 else total2)
    readme.write('Puzzle 1 Time: ' + str(avg1) +
                 ('ns\n\n' if ns1 else 'ms\n\n'))
    readme.write('Puzzle 2 Time: ' + str(avg2) +
                 ('ns\n\n' if ns2 else 'ms\n\n'))

readme.write('# Total\n')
readme.write('Total Time: ' + str(full) + 'ms')
readme.close()
