def path(current, visited_small_caves, cmap, small_cave_visited_twice):
    if current == 'end':
        return [[current]]

    next_visited_small_caves = visited_small_caves
    next_small_cave_visited_twice = small_cave_visited_twice
    # Are we currently in a small cave?
    if current.islower() and current != 'start':
        # Yes - add it to the visited small cave list
        next_visited_small_caves = visited_small_caves + [current]
        # and if we visited it before...
        if current in visited_small_caves:
            # check if we already visited a small cave twice and react accordingly
            if small_cave_visited_twice:
                return []
            else:
                next_small_cave_visited_twice = True
        

    paths = []
    for next_cave in cmap[current]:
        if (next_cave == 'start'):
            continue
        followups = path(next_cave, next_visited_small_caves, cmap, next_small_cave_visited_twice)
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
    
    paths = path('start', [], cmap, False) 
    print(len(paths)) # 143562