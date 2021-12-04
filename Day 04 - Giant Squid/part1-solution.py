from more_itertools import grouper

def check_victory(boardmarks):
    for boardid, boardmark in enumerate(boardmarks):
        # check rows        
        if any(all(x for x in row) for row in boardmark):
            return boardid
        
        # check columns
        if any(all(x for x in column) for column in [*zip(*boardmark)]):
            return boardid
    
    return None

def calc_score(board, boardmark):
    sum = 0
    for row, rowmark in zip(board, boardmark):
        for cell, cellmark in zip(row, rowmark):
            if not cellmark:
                sum += int(cell)
    return sum

with open('./input.txt') as input:
    numbers = input.readline()
    boards = []
    for board in grouper(6, input):
        boards.append([row.strip().split() for row in board[1:]])
    
    boardmarks = [[[False for cell in row] for row in board] for board in boards]
    for number in numbers.split(','):
        for boardid, board in enumerate(boards):
            for rowid, row in enumerate(board):
                for colid, cell in enumerate(row):
                    if board[rowid][colid] == number:
                        boardmarks[boardid][rowid][colid] = True
        victoryboard = check_victory(boardmarks)
        if victoryboard != None:
            score = calc_score(boards[victoryboard], boardmarks[victoryboard])
            print(score * int(number)) # 38594
            break

