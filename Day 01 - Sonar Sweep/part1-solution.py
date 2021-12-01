with open('./input.txt') as input:
    last = 999999999999
    counter = 0
    for line in input.readlines():
        current = int(line.strip())
        if (current > last):
            counter += 1
        last = current
    print(counter) # 1342