import random
import sys
import time

sys.path.append("./")
from grid_generator import grid as grd
from convert_to_image import convert as convert
from color_manipulation import colors as col

def randomize_cells(grid, rand_range):
    rows, columns = grd.get_dimensions(grid)
    rs, re = rand_range

    for x in range(rows):
        for y in range(columns):
            rand = random.randint(1, 100) < 5
            if rand:
                grid[x][y] = random.randint(rs, re)

def update_position(base_grid, new_grid, x, y):
    a_positions = grd.get_valid_adjacent_positions(base_grid, x, y)
    new_x, new_y = random.choice(a_positions)
    
    
    value = sum([base_grid[r][c] for r,c in a_positions])

    if value > 4:
        new_grid[x][y] = 0
    elif value < 4:
        new_grid = 1
    else:
        new_grid[x][y] = 4

rows, columns = 100, 100
mid_x, mid_y = int(rows / 2), int(columns / 2)
grid = grd.generate(rows, columns, noise_density=0)

grid[mid_x][mid_y] = 1

while True:
    new_grid = grd.copy(grid)
    for x in range(rows):
        for y in range(columns):
            if grid[x][y] in (1, 2, 3):
                update_position(grid, new_grid, x, y)

    grid = new_grid
    convert.convert(grid, name="lol")
    time.sleep(0.05)


