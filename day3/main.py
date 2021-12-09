with open('input.txt') as f:
    puzzle = [l.strip() for l in f]

def solve(puzzle):
    gamma = epsilon = ""
    for bits in zip(*puzzle):
        gamma += '1' if bits.count('1') > bits.count('0') else '0'
        epsilon += '1' if bits.count('1') < bits.count('0') else '0'
    return int(gamma, 2) * int(epsilon, 2)

def solve2(puzzle):
    oxygen, co2 = puzzle.copy(), puzzle.copy()

    for i in range(len(puzzle[0])):
        o_bits = ''.join([x[i] for x in oxygen])
        c_bits = ''.join([x[i] for x in co2])
        most_common = '1' if o_bits.count('1') >= o_bits.count('0') else '0'
        least_common = '1' if c_bits.count('1') < c_bits.count('0') else '0'

        if len(oxygen) > 1:
            oxygen = list(filter(lambda b: b[i] == most_common, oxygen))
    
        if len(co2) > 1:
            co2 = list(filter(lambda b: b[i] == least_common, co2))

    return int(oxygen[0], 2) *int(co2[0], 2)


print(solve(puzzle))
print(solve2(puzzle))
