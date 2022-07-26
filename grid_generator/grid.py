import numpy as np
import random

def generate(rows, columns, noise_density=0):
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