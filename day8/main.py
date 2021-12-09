def get_input(file):
    puzzle = []
    with open(file) as f:
        for l in f:
            inp, out = l.strip().split(' | ')
            puzzle.append((inp.split(), out.split()))
    return puzzle


def solve(puzzle):
    part1 = part2 = 0

    for inp, out in puzzle:
        # Part 1
        part1 += sum(len(n) in (2, 4, 3, 7) for n in out)

        # Part 2
        digit_map = {
            42: '0',
            17: '1',
            34: '2',
            39: '3',
            30: '4',
            37: '5',
            41: '6',
            25: '7',
            49: '8',
            45: '9'
        }
        char_score = {c: ''.join(inp).count(c) for c in 'abcdefg'}
        out_scores = [sum([char_score[c] for c in n]) for n in out]
        part2 += int(''.join(digit_map[s] for s in out_scores))

    return part1, part2


puzzle = get_input('input.txt')
print(solve(puzzle))
