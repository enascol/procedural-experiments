import random
import sys
import time

sys.path.append("./")
from grid_generator import grid as _grid
from convert_to_image.convert import *

match_table = {
    (1, 2): 1,
    (1, 3): 3,
    (2, 1): 1,
    (2, 3): 2,
    (3, 1): 3,
    (3, 2): 2
}

def who_wins(x, y):
   return match_table[(x, y)]

def get_losing_match(x):
    for match in match_table:
        mx, my = match
        if x in match and who_wins(mx, my) != x:
            return match[0] if match[0] != x else match[1]

def count_neighboors(grid, x, y):
    neighboors = _grid.get_valid_adjacent_positions(grid, x, y)
    n = {}

    for x, y in neighboors:
        pos_value = grid[x][y]
        try:
            n[pos_value] += 1
        except KeyError:
            n[pos_value] = 1
    
    return n

def update_position(base, new_grid, x, y):
    n = count_neighboors(base, x, y)
    position_value = base[x][y]
    loss_match = get_losing_match(position_value)

    if loss_match in n:
        if n[loss_match] >= 2:
            new_grid[x][y] = loss_match
    
    return new_grid


def populate(grid):
    rows, columns = _grid.get_dimensions(grid)
    
    for x in range(rows):
        for y in range(columns):
            grid[x][y] = random.randint(1, 3)
    
    return grid


rows, columns = 50, 150
grid = _grid.generate(rows, columns)
grid = populate(grid)

colors = {1: get_random_color(), 2: get_random_color(), 3: get_random_color()}
while True:
    new_grid = _grid.copy(grid)
    for x in range(rows):
        for y in range(columns):
            grid = update_position(grid, new_grid, x, y)
    
    grid = new_grid
    convert(grid, name ="kill", colors = colors)
    time.sleep(0.05)