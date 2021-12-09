from functools import reduce
import heapq

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

def calculate_basin_size(row_id, col_id, cave):
    visited = []
    tovisit = [(row_id, col_id)]
    while len(tovisit) > 0:
        cell_x, cell_y = tovisit.pop(0)
        if (cell_x, cell_y) in visited:
            continue
        visited.append((cell_x, cell_y))
        for of_row, of_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            checkrow = getordefault(cave, cell_x + of_row, [])
            checkcell = getordefault(checkrow, cell_y + of_col, 9)
            if checkcell != 9 and checkcell >= cave[cell_x][cell_y] and (cell_x + of_row, cell_y + of_col) not in tovisit:
                tovisit.append((cell_x + of_row, cell_y + of_col))
    return len(visited)


with open('input.txt') as input:
    cave = [list(map(int, line.strip())) for line in input.readlines()]
    basin_sizes = []
    for row_id, row in enumerate(cave):
        for col_id, cell in enumerate(row):
            if is_lowpoint(row_id, col_id, cave):
                basin_size = calculate_basin_size(row_id, col_id, cave)
                basin_sizes.append(basin_size)
    print(reduce(lambda x, y: x * y, heapq.nlargest(3, basin_sizes))) # 1397760
    