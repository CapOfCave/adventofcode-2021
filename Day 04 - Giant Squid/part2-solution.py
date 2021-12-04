from more_itertools import grouper

def check_victory(boards):
    out = []
    for board in boards:
        # check rows        
        if any(all(x for x in row) for row in board["marks"]):
            out.append(board)
        # check columns
        elif any(all(x for x in column) for column in [*zip(*board["marks"])]):
            out.append(board)
    
    return out

def calc_score(board):
    sum = 0
    for row, rowmark in zip(board["values"], board["marks"]):
        for cell, cellmark in zip(row, rowmark):
            if not cellmark:
                sum += int(cell)
    return sum

with open('./input.txt') as input:
    numbers = input.readline()
    boards = []
    for board in grouper(6, input):
        boards.append({"values": [row.strip().split() for row in board[1:]], "marks": [[False for cell in row.strip().split()] for row in board[1:]]})
    for number in numbers.split(','):
        for boardid, board in enumerate(boards):
            for valuerow, markrow in zip(board["values"], board["marks"]):
                for index, value in enumerate(valuerow):
                    if value == number:
                        markrow[index] = True
        victoryboards = check_victory(boards)
        if len(victoryboards) > 0 and len(boards) == 1:
            score = calc_score(victoryboards[0])
            print(score * int(number)) # 21184
            break
        for vboard in victoryboards:
            boards.remove(vboard)
        
            


