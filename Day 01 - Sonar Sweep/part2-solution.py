with open('./input.txt') as input:
    lines = [int(s.strip()) for s in input.readlines()]
    last = 999999999999
    counter = 0
    for (a, b, c) in zip(lines[0:-2], lines[1:-1], lines[2:]):
        current = a + b + c
        if (current > last):
            counter += 1
        last = current
    print(counter) # 1378
