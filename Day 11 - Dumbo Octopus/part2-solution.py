def print2d(arr):
    print("\n".join(["".join(map(str, line)) for line in arr]))
    print()

def inc_energy_level(world, row, col, octopi_to_flash, flashed_octipi):
    world[row][col] = world[row][col] + 1
    if world[row][col] > 9 and (row, col) not in flashed_octipi and (row, col) not in octopi_to_flash:
        octopi_to_flash.append((row, col))
                

with open('input.txt') as input:
    world = []
    for line in input.readlines():
        world.append([int(s) for s in line.strip()])
    
    flashes = 0
    flashed_this_step = 0
    step = 0
    while flashed_this_step < len(world) * len(world[0]):
        # step
        octopi_to_flash = []
        flashed_octipi = []
        for row_index, line in enumerate(world):
            for col_index, octopus in enumerate(line):
                inc_energy_level(world, row_index, col_index, octopi_to_flash, flashed_octipi)
        
        while len(octopi_to_flash) > 0:
            oc_row, oc_col = octopi_to_flash.pop()
            flashed_octipi.append((oc_row, oc_col))
            for of_x, of_y in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                if (oc_row + of_x >= 0 and oc_row + of_x < len(world) and oc_col + of_y >= 0 and oc_col + of_y < len(world[0])):
                    inc_energy_level(world, oc_row + of_x, oc_col + of_y, octopi_to_flash, flashed_octipi)
        for (oc_row, oc_col) in flashed_octipi:
            world[oc_row][oc_col] = 0 

        flashed_this_step = len(flashed_octipi)
        flashes += flashed_this_step
        step += 1
    print(step) # 229
