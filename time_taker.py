import subprocess

readme = open('README.md', 'w')
for day in range(17):
    dir = 'Day' + str(day + 1).zfill(2)
    readme.write(dir + '\n')
    puzzle1 = subprocess.check_output(
        ['python3', dir + '/puzzle1.py']).decode("utf-8")
    puzzle1time = puzzle1.split('Time: ')[1].replace('\n','')
    puzzle2 = subprocess.check_output(
        ['python3', dir + '/puzzle2.py']).decode("utf-8")
    puzzle2time = puzzle2.split('Time: ')[1].replace('\n','')
    readme.write('Puzzle 1 Time: ' + puzzle1time)
    readme.write('Puzzle 2 Time: ' + puzzle2time + '\n\n')
readme.close()
