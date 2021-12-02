with open('./input.txt') as input:
    horizontal_position = 0
    depth = 0
    for row in input.readlines():
        attribute, count_str = row.split()
        count = int(count_str)
        if attribute == 'forward':
            horizontal_position += count
        elif attribute == 'down':
            depth += count
        elif attribute == 'up':
            depth -= count
        else:
            print(f"Error: unknown attribute {attribute}")
    print(horizontal_position * depth) # 2019945