from statistics import median


def get_input(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def solve(puzzle):
    med = int(median(puzzle))
    part1 = sum([abs(x - med) for x in puzzle])

    mean = sum(puzzle) // len(puzzle)
    gauss = lambda x: x * (x+1) // 2
    part2 = min(sum(gauss(abs(x-mean)) for x in puzzle),
                sum(gauss(abs(x-mean-1)) for x in puzzle))
    
    return part1, part2


puzzle = get_input('input.txt')
print(solve(puzzle))
