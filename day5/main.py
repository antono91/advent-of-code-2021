from collections import defaultdict


def get_input(file):
    with open(file) as f:
        return [list(map(int, l.strip().replace(' -> ', ',').split(','))) for l in f]


def print_map(map):
    for y in range(10):
        for x in range(10):
            print(map[(x, y)] if (x, y) in map else '.', end=' ')
        print()


def solve(puzzle, part1):
    map = defaultdict(int)
    for x1, y1, x2, y2 in puzzle:
        dx = 1 if x1 < x2 else -1 if x1 > x2 else 0
        dy = 1 if y1 < y2 else -1 if y1 > y2 else 0
        if part1 and dy != 0 and dx != 0:
            continue

        while not (x1 == x2 + dx and y1 == y2 + dy):
            map[(x1, y1)] += 1
            x1 += dx
            y1 += dy
    return len([pos for pos, n in map.items() if n >= 2])


puzzle = get_input('input.txt')
print(solve(puzzle, True))
print(solve(puzzle, False))
