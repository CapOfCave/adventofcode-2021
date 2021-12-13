from itertools import takewhile

def foldalongx(points, foldx):
    out = []
    for point in points:
        target = (foldx - abs(foldx - point[0]), point[1])
        if not target in out:
            out.append(target)
    return out

def foldalongy(points, foldy):
    out = []
    for point in points:
        target = (point[0], foldy - abs(foldy - point[1]))
        if not target in out:
            out.append(target)
    return out


with open('input.txt') as input:
    points = [list(map(int, line.strip().split(','))) for line in takewhile(lambda line: line != "\n", input)]
    folds = [[line.strip().split('=')[0], int(line.strip().split('=')[1])] for line in input]
    
    fold = folds[0]
    if (fold[0] == 'fold along y'):
        points = foldalongy(points, fold[1])
    else:
        points = foldalongx(points, fold[1])    
    
    print(len(points)) # 712