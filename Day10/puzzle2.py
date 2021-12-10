def puzzle(data):
    total = 0
    scores = []
    for line in data:
        line = line.replace('\n', '')
        stack = []
        chr = ''
        error = False
        for chr in line:
            if chr == '(' or chr == '[' or chr == '<' or chr == '{':
                stack.append(chr)
            elif chr == ')':
                top = stack.pop()
                if top != '(':
                    error = True
                    break
            elif chr == '}':
                top = stack.pop()
                if top != '{':
                    error = True
                    break
            elif chr == '>':
                top = stack.pop()
                if top != '<':
                    error = True
                    break
            elif chr == ']':
                top = stack.pop()
                if top != '[':
                    error = True
                    break
        if error:
            continue

        score = 0
        stack.reverse()
        for chr in stack:
            score = score * 5
            if chr == '(':
                score = score + 1
            if chr == '[':
                score = score + 2
            if chr == '{':
                score = score + 3
            if chr == '<':
                score = score + 4

        scores.append(score)

    scores.sort()
    total = scores[int((len(scores) - 1) / 2)]
    print("Answer: " + str(total))


data = open(__file__.replace('.py', 'input'))
puzzle(data.readlines())
