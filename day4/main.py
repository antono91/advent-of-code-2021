with open('input.txt') as f:
    numbers = f.readline().strip().split(',')
    boards = [dict([(n, 0) for n in board.replace('\n' ,' ').split()]) for board in f.read().split('\n\n')]


def solve(numbers, boards):
    boards_won = []
    winning_nums = []
    
    for num in numbers:
        for board in boards:
            if num not in board or board in boards_won: continue
            board[num] = 1
            ind = list(board).index(num)
            r, c = ind // 5, ind % 5
            row = [list(board)[r*5 + i] for i in range(5)]
            col = [list(board)[c + i*5] for i in range(5)]
            if all([board[x] for x in row]) or all([board[x] for x in col]):
                boards_won.append(board)
                winning_nums.append(num)
    
    first = sum([int(key) for key, value in boards_won[0].items() if not value]) * int(winning_nums[0])
    last = sum([int(key) for key, value in boards_won[-1].items() if not value]) * int(winning_nums[-1])

    return first, last


print(solve(numbers, boards))
