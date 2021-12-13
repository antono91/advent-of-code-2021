def get_input(file):
    with open(file) as f:
        return [l.strip() for l in f]


def solve(puzzle):
    brackets = ['()', '{}', '[]', '<>']
    closing = {')': 3, ']': 57, '}': 1197, '>': 25137}
    opening = {'(': 1, '[': 2, '{': 3, '<': 4}
    part1 = 0
    incomplete = []
    # Part 1
    for line in puzzle:
        while any(x in line for x in brackets):
            for br in brackets:
                line = line.replace(br, '')

        if not any(x in line for x in closing.keys()): incomplete.append(line) 

        for c in line:
            if c in closing.keys():
                part1 += closing[c]
                break

    # Part 2
    final_scores = []
    for line in incomplete:
        scores = [opening[b] for b in line[::-1]]
        score = 0
        for s in scores:
            score = score * 5 + s
        final_scores.append(score)
    part2 = sorted(final_scores)[len(final_scores) // 2]

    return part1, part2


puzzle = get_input('input.txt')
print(solve(puzzle))
