def get_input(file):
    with open(file) as f:
        return [int(line) for line in f]


def solve(puzzle):
    count = 0
    for i in range(1, len(puzzle)):
        if puzzle[i] > puzzle[i-1]:
            count += 1
    return count

def solve2(puzzle):
    windows = [sum(puzzle[i:i+3]) for i in range(len(puzzle)-2)]
    return solve(windows)

puzzle = get_input('input.txt')
print(solve(puzzle))
print(solve2(puzzle))

