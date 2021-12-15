import math
def heuristic(point, height, width):
    (x, y) = point
    # distance to the bottom right field (squared)
    return math.sqrt((x - height + 1) ** 2 + (y - width + 1) ** 2)


def node_with_min_f(discovered, f):
    return min(discovered, key = lambda k: f.get(k, 999999999999999))

def calc_risk_value(predecessors, current, cave):
    path = [current]
    total = cave[current]
    while current in predecessors:
        current = predecessors[current]
        path.append(current)
        total += cave[current]
    # first risk is ignored
    total -= cave[current]
    return total

def astar(start, goal, cave, height, width):
    discovered = {start}
    predecessors = {}
    g = {}
    g[start] = 0
    f = {}
    f[start] = heuristic(start, height, width)

    while (len(discovered) > 0):
        current = node_with_min_f(discovered, f)
        crow, ccol = current
        if current == goal:
            return calc_risk_value(predecessors, current, cave)
        discovered.remove(current)
        for ofsrow, ofscol in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if crow + ofsrow < 0 or crow + ofsrow >= height or ccol + ofscol < 0 or ccol + ofscol >= width:
                continue
            neighbor = (crow + ofsrow, ccol + ofscol)
            tentative_g = g[current] + cave[neighbor]
            if tentative_g < g.get(neighbor, 999999999999999):
                predecessors[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic(neighbor, height, width)
                if neighbor not in discovered:
                    discovered.add(neighbor)
        

with open('input.txt') as input:

    cave = {}
    width = 0
    height = 0
    for rowid, row in enumerate(input.readlines()):
        height += 1
        width = 0
        for colid, risk in enumerate(row.strip()):
            cave[(rowid, colid)] = int(risk)
            width += 1
    
    path = astar((0, 0), (height - 1, width - 1), cave, height, width)
    print(path) # 626

    
    



    