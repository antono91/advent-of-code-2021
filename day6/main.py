def get_input(file):
    with open(file) as f:
        return [int(x) for x in f.readline().strip().split(',')]


def solve(puzzle, days):
    state = [puzzle.count(i) for i in range(9)]
    for _ in range(days):
        state = state[1:] + [state[0]]
        state[6] += state[8]
    return sum(state)


puzzle = get_input('input.txt')
print(solve(puzzle, 80))
print(solve(puzzle, 256))
