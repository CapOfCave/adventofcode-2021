with open('./input.txt') as input:
    fish = {}
    for f in input.readline().split(','):
        i = int(f)
        fish[i] = fish.get(i, 0) + 1

    days = 256
    for day in range(days):
        fish = {d - 1: f for d, f in fish.items()}
        if (-1 in fish):
            fish[6] = fish.get(6, 0) + fish[-1]
            fish[8] = fish[-1]
            del fish[-1]
    print(sum(fish.values())) # 388739
    
