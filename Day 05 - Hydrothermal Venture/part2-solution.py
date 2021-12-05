import itertools
with open('./input.txt') as input:
    hits = {}
    for line in input:
        (x1, y1), (x2, y2) = [ map(int, point.split(',')) for point in line.strip().split(' -> ')]
        iterx = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        itery = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        if abs(x1 - x2) < abs(y1 - y2):
            iterx = itertools.cycle(iterx)
        else:
            itery = itertools.cycle(itery)

        for x, y in zip(iterx, itery):
            if (x, y) in hits:
                hits[(x, y)] += 1
            else:
                hits[(x, y)] = 1

    print(len([val for val in hits.values() if val > 1])) # 16925