def get_input(file):
    with open(file) as f:
        dots, folds = f.read().split('\n\n')
        paper = set(tuple(map(int, x.split(','))) for x in dots.split())
        folds = [(f[11], int(f[13:])) for f in folds.split('\n')]
        return paper, folds


def print_paper(paper):
    max_x = max([x for x, _ in paper])
    max_y = max([y for _, y in paper])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print('#', end=' ') if (x, y) in paper else print('.', end=' ')
        print()


def solve(paper, folds, p1):
    for d, f_line in folds:
        fold_dict = dict(
            (a, a - b)
            for a, b in zip(range(f_line *
                                  2, f_line, -1), range(f_line * 2, 0, -2)))
        new_paper = set()
        for x, y in paper:
            if d == 'y':
                new_pos = (x, fold_dict[y] if y in fold_dict else y)
            else:
                new_pos = (fold_dict[x] if x in fold_dict else x, y)
            new_paper.add(new_pos)

        paper = new_paper
        if p1: return len(paper)
    print_paper(paper)


puzzle = get_input('input.txt')
print(solve(*puzzle, True))
print(solve(*puzzle, False))
