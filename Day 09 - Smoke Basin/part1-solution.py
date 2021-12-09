def getordefault(ls, ind, default):
    if ind < 0 or ind >= len(ls):
        return default
    return ls[ind]

def is_lowpoint(row_id, col_id, cave):
    for of_row, of_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        checkrow = getordefault(cave, row_id + of_row, [])
        checkcell = getordefault(checkrow, col_id + of_col, 10)
        if checkcell <= cave[row_id][col_id]:
            return False
    return True

with open('input.txt') as input:
    cave = [list(map(int, line.strip())) for line in input.readlines()]
    risklevelsum = 0

    for row_id, row in enumerate(cave):
        for col_id, cell in enumerate(row):
            if is_lowpoint(row_id, col_id, cave):
                risklevel = cave[row_id][col_id] + 1
                risklevelsum += risklevel
    print(risklevelsum) # 462
