with open('./input.txt') as input:
    fish = []
    for f in input.readline().split(','):
        fish.append(int(f))

    days = 80
    for day in range(days):
        fish = [f - 1 for f in fish]
        for index, f in enumerate(fish):
            if f < 0:
                fish[index] = 6
                fish.append(8)
    print(len(fish)) # 388739
    
