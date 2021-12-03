from itertools import tee

with open('./input.txt') as input:
    rows_raw = list(map(lambda x: x.strip(), input.readlines()))
    bitcount = len(rows_raw[0])

    oxygen = 0
    rows = rows_raw
    for index in range(bitcount):    
        dif = 0
        for row in rows:
            dif += int(row[index]) * 2 - 1
        rows = [row for row in rows if int(row[index]) == int(dif >= 0)]
        if len(rows) == 1:
            oxygen = int(rows[0], 2)

    
    co2 = 0
    rows = rows_raw
    for index in range(bitcount):    
        dif = 0
        for row in rows:
            dif += int(row[index]) * 2 - 1
        rows = [row for row in rows if int(row[index]) == int(dif < 0)]
        if len(rows) == 1:
            co2 = int(rows[0], 2)

    print(oxygen * co2) # 4432698

    