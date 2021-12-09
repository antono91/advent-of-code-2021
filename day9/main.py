import math

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_input(file):
    with open(file) as f:
        heat_map = {}
        inp = [l.strip() for l in f]
        for r in range(len(inp)):
            for c in range(len(inp[0])):
                heat_map[(r, c)] = int(inp[r][c])
        return heat_map


def get_neigbours(m, pos):
    neighbours = []
    for d in DIRECTIONS:
        n_pos = (pos[0] + d[0], pos[1] + d[1])
        if n_pos in m: neighbours.append(m[n_pos])
    return neighbours


def find_basin_size(m, p):
    pos_to_check = [p]
    basin = []
    while pos_to_check:
        pos = pos_to_check.pop(0)
        for d in DIRECTIONS:
            n_pos = (pos[0] + d[0], pos[1] + d[1])
            if n_pos in basin or n_pos not in m or m[n_pos] == 9: continue
            pos_to_check.append(n_pos)
            basin.append(n_pos)
    return len(basin)


def solve(heat_map):
    heat_sinks = []
    # Part 1
    for pos, height in heat_map.items():
        if all([n > height for n in get_neigbours(heat_map, pos)]):
            heat_sinks.append(pos)
    part1 = sum(heat_map[p] + 1 for p in heat_sinks)

    # Part 2
    largest_basins = sorted(
        [find_basin_size(heat_map, sink) for sink in heat_sinks])[-3:]
    part2 = math.prod(largest_basins)
    return part1, part2


puzzle = get_input('input.txt')
print(solve(puzzle))
