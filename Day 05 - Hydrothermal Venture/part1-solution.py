with open('./input.txt') as input:
    hits = {}
    for line in input:
        (x1, y1), (x2, y2) = [ map(int, point.split(',')) for point in line.strip().split(' -> ')]
        
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) in hits:
                    hits[(x1, y)] += 1
                else:
                    hits[(x1, y)] = 1
        
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) in hits:
                    hits[(x, y1)] += 1
                else:
                    hits[(x, y1)] = 1

    print(len([val for val in hits.values() if val > 1])) # 5147