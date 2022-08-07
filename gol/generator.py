import time
import sys
sys.path.append("./")
from convert_to_image import convert
import numpy as np
from  PIL import Image
import random
import copy


def generate_grid(rows, columns, noise_density=0):
    grid = np.array([[0 for _ in range(columns)] for _ in range(rows)])
    
    if not noise_density:
        return grid
    else:
        for row in range(rows):
            for column in range(columns):
                add_noise = random.randint(1, 100) < noise_density
                grid[row, column] = add_noise * 1
    
    return grid

def show(grid, hide_zeroes=False):
    for row in grid:
        if hide_zeroes:
            print("".join([str(x) for x in row]).replace("0", " "))
        else:
            print("".join([str(x) for x in row]))

def is_valid_position(grid, x, y):
    rows, columns = len(grid), len(grid[0])
    
    valid_x = (x >= 0) and (x < rows)
    valid_y = (y >= 0) and (y < columns)
    
    return valid_x and valid_y

def get_adjacent_positions(x, y):
    dlt = x - 1, y - 1
    top = x - 1, y
    drt = x - 1, y + 1
    left = x, y - 1
    right = x, y + 1
    dlb = x + 1, y - 1
    down = x + 1, y
    drb = x + 1, y + 1

    return dlt, top, drt, left, right, dlb, down, drb

def get_valid_adjacent_positions(grid, x, y):
    adjacent_positions = get_adjacent_positions(x, y)
    valid_positions = [(x, y) for x, y in adjacent_positions if is_valid_position(grid, x, y)]

    return valid_positions
  
def get_adjacent_values(grid, x, y):
    adjacent_positions = get_valid_adjacent_positions(grid, x, y)
    return sum([grid[x, y] for x, y in adjacent_positions])

def update_cell(base_grid, new_grid, x,  y, prob =False):
    cell_value = base_grid[x, y]
    adjacent_values = get_adjacent_values(base_grid, x, y)

    if cell_value == 1 and adjacent_values >= 4:
        if prob and random.randint(1, 100) <= 5:
            new_grid[x, y] = 0
        elif not prob:
            new_grid[x, y] = 0
    elif cell_value == 1 and adjacent_values <= 1:
        if prob and random.randint(1, 100) <= 10:
            new_grid[x, y] = 0
        elif not prob:
            new_grid[x, y] = 0
    elif cell_value == 0 and adjacent_values == 3:
        if prob and random.randint(1, 100) <= 75:
            new_grid[x, y] = 1
        elif not prob:
            new_grid[x, y] = 1
    else:
        pass

bg = [random.randint(0, 255) for x in range(3)]
fg = [random.randint(0, 255) for x in range(3)]

colors = {0: bg, 1: fg}

def update_grid(grid, prob = False):
    rows, columns = grid.shape
    new_grid = grid.copy()

    for x in range(rows):
        for y in range(columns):
            update_cell(grid, new_grid, x, y, prob)

    return new_grid
