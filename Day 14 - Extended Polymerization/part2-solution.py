def inc(polymer, key, dif = 1):
    polymer[key] = polymer.get(key, 0) + dif

def calc_dif(polymer, polymerraw):
    lettercount = {}
    for combi, combicount in polymer.items():
        inc(lettercount, combi[0], combicount)
        inc(lettercount, combi[1], combicount)
    
    # divide by 2 (except for first and last letter)
    inc(lettercount, polymerraw[0])
    inc(lettercount, polymerraw[-1])
    lettercount = {k: v // 2 for k, v in lettercount.items()}

    return max(lettercount.values()) - min(lettercount.values()) 

with open('input.txt') as input:
    polymerraw = input.readline().strip()
    input.readline() # ignore empty line
    combinations = { (line.split(' -> ')[0]): line.strip().split(' -> ')[1] for line in input.readlines()}

    polymer = {}
    for f, s in zip(polymerraw[:-1], polymerraw[1:]):
        inc(polymer, f+s)
    
    # do polymerization
    for step in range(40):
        next_polymer = {}
        for polycombi, count in polymer.items():
            if polycombi in combinations:
                res = combinations[polycombi]
                inc(next_polymer, polycombi[0]+res, count)
                inc(next_polymer, res + polycombi[1], count)
            else:
                inc(next_polymer, polycombi, count)
        polymer = next_polymer
    
    # print dif
    print(calc_dif(polymer, polymerraw)) # 3232426226464
    
    
    