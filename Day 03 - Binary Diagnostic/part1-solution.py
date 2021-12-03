from itertools import tee

with open('./input.txt') as input:
    handle1, handle2 = tee(input)
    bitcount = len(next(handle1).strip())
    count = 0
    print(bitcount)
    occurences = [0] * bitcount
    for row in handle2:
        for index, bit in enumerate(row.strip()):
            occurences[index] += int(bit)
        count += 1
    
    gamma = sum([2 ** (bitcount - 1 - index) * (occurence > count / 2) for index, occurence in enumerate(occurences)])
    epsilon = 2 ** bitcount - 1 - gamma
    print(gamma * epsilon) # 3374136
    