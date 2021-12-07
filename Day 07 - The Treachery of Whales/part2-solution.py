
def calc_score(crabs, i):
    return sum([abs(c - i) * (abs(c - i) + 1) // 2 for c in crabs])

with open('./input.txt') as input:
    crabs = [int(s) for s in input.readline().split(',')]

    best_score = max(crabs) * max(crabs) * len(crabs)

    for test in range(max(crabs)):
        new_score = calc_score(crabs, test)
        if (new_score < best_score):
            best_score = new_score
        elif (new_score > best_score):
            break # it only gets worse from here

    print(best_score) # 355592