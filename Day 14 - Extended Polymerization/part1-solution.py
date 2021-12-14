def calc_dif(polymer):
    maxv = max(set(polymer), key = polymer.count)
    minv = min(set(polymer), key = polymer.count)    

    return polymer.count(maxv) - polymer.count(minv)

with open('input.txt') as input:
    polymer = input.readline().strip()
    input.readline() # ignore empty line
    combinations = { (line.split(' -> ')[0]): line.strip().split(' -> ')[1] for line in input.readlines()}

    for step in range(10):
        next_polymer = polymer[0]
        for f, s in zip(polymer[:-1], polymer[1:]):
            if (f + s) in combinations:
                next_polymer += combinations[f+s]
            next_polymer += s
        polymer = next_polymer
    print(calc_dif(polymer)) # 2947

    