with open('./input.txt') as input:
    aim = 0
    horizontal_position = 0
    depth = 0
    for row in input.readlines():
        attribute, count_str = row.split()
        count = int(count_str)
        if attribute == 'forward':
            horizontal_position += count
            depth += aim * count
        elif attribute == 'down':
            aim += count
        elif attribute == 'up':
            aim -= count
        else:
            print(f"Error: unknown attribute {attribute}")
    print(horizontal_position * depth) # 1599311480