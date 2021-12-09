def get_input(file):
    with open(file) as f:
        return [(line.split()[0], int(line.split()[1])) for line in f]


def solve(puzzle):
    horizontal = depth = 0
    for direction, value in puzzle:
        if direction == "forward": horizontal += value
        elif direction == "up": depth -= value
        else: depth += value
    return horizontal * depth

def solve2(puzzle):
    horizontal = depth = aim = 0
    for direction, value in puzzle:
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "up": aim -= value
        else: aim += value
    return horizontal * depth

puzzle = get_input('input.txt')
print(solve(puzzle))
print(solve2(puzzle))
