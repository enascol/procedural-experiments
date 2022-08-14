import random
import sys
import time

sys.path.append("./")

from grid_generator.grid import *
from convert_to_image.convert import *
from color_manipulation.colors import *

def generate_random_grid(rows, columns, cell_types=3):
    grid = generate(rows, columns)

    for x in range(rows):
        for y in range(columns):
            grid[x, y] = random.randint(0, cell_types - 1)
    
    return grid

def update_position(base, new, x, y):
    valid_positions = get_valid_adjacent_positions(base, x, y)
    m = [base[x][y] for x, y in valid_positions]
    
    value = int(sum(m) / len(m))

    new[x][y] = value
    
    return new

def update_grid(grid):
    rows, columns = grid.shape

    for x in range(rows):
        for y in range(columns):
            grid = update_position(grid, x, y)
    
    return grid

def remove_single_pixes(grid):
    new_grid = grid.copy()

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            n = get_adjacent_positions_values(grid, x, y)
            cell_value = grid[x, y]
            if len(set(n)) < 5 and n[0] != cell_value:
                new_grid[x, y] = n[0]
    
    return new_grid

def iterate(grid, iterations, save_once =True):
    cell_types = len(get_cell_types(grid))
    colors = {x:get_random_color() for x in range(cell_types)}

    for _ in range(iterations):
        new_g = grid.copy()
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                update_position(grid, new_g, x, y)
        grid = new_g
        if not save_once:
            time.sleep(0.05)
            convert(grid, colors = colors)
    
    return grid, convert(grid, colors = colors)






    
