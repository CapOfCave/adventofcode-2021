def path(current, visited_small_caves, cmap):
    if current == 'end':
        return [[current]]
    next_caves = cmap[current]
    paths = []
    for next_cave in next_caves:
        if next_cave in visited_small_caves:
            continue
        if next_cave.islower():
            next_visited_small_caves = visited_small_caves + [next_cave]
        else:
            next_visited_small_caves = visited_small_caves
        followups = path(next_cave, next_visited_small_caves, cmap)
        for followup in followups:
            paths.append([current] + followup)
    return paths

with open('input.txt') as input:
    connections = [(line.split('-')[0], line.strip().split('-')[1]) for line in input.readlines()]
    # build connection map
    cmap = {}
    for s, e in connections:
        if s in cmap:
            cmap[s].append(e)
        else:
            cmap[s] = [e]
        if e in cmap:
            cmap[e].append(s)
        else:
            cmap[e] = [s]
    
    paths = path('start', ['start'], cmap) 
    print(len(paths)) # 4754