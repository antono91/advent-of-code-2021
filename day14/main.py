from collections import Counter


def get_input(file):
    rules = {}
    with open(file) as f:
        polymere, insertion = f.read().split('\n\n')
        for x in insertion.split('\n'):
            f, t = x.split(' -> ')
            rules[f] = t
    return polymere, rules


def solve(polymere, rules, steps):
    elements = Counter(polymere)
    polymere = Counter([a + b for a, b in zip(polymere, polymere[1:])])
    for _ in range(steps):
        new_polymere = Counter()
        for pair in polymere:
            new_polymere[pair[0] + rules[pair]] += polymere[pair]
            new_polymere[rules[pair] + pair[1]] += polymere[pair]
            elements[rules[pair]] += polymere[pair]
        polymere = new_polymere
        
    values = list(elements.values())
    return max(values) - min(values)


puzzle = get_input('input.txt')
print(solve(*puzzle, 10))
print(solve(*puzzle, 40))
