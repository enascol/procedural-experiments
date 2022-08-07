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


def get_dimensions(grid):
    return len(grid), len(grid[0])

def copy(grid):
    rows, columns = grid.shape
    return np.array([[grid[x][y] for y in range(columns)] for x in range(rows)])

def show(grid, hide_zeroes=False):
    for row in grid:
        if hide_zeroes:
            print("".join([str(x) for x in row]).replace("0", " "))
        else:
            print("".join([str(x) for x in row]))

def is_valid_position(grid, x, y):
    rows, columns = grid.shape
    
    valid_x = (x >= 0) and (x < rows)
    valid_y = (y >= 0) and (y < columns)
    
    return valid_x and valid_y

def get_all_directions_name():
    directions = (
        "dlt",
        "top",
        "drt",
        "left",
        "right",
        "dlb",
        "down",
        "drb"
    )
    
    return directions

def get_direction_name(x, y, dir_x, dir_y):
    if (dir_x, dir_y) == (x - 1, y - 1):
        return "dlt"
    elif (dir_x, dir_y) == (x - 1, y):
        return "top"
    elif (dir_x, dir_y) == (x - 1, y + 1):
        return "drt"
    elif (dir_x, dir_y) == (x, y - 1):
        return "left"
    elif (dir_x, dir_y) == (x, y + 1):
        return "right"
    elif (dir_x, dir_y) == (x + 1, y - 1):
        return "dlb"
    elif (dir_x, dir_y) ==  (x + 1, y):
        return "down"
    elif (dir_x, dir_y) == (x + 1, y + 1):
        return "drb"

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

def get_valid_vn_neighboorhood(grid, x, y):
    n  = [
        (x - 1, y), #UP
        (x + 1, y), #DOWN
        (x, y + 1), #RIGHT
        (x, y - 1), #LEFT
    ]

    return [(x, y) for x, y in n if is_valid_position(grid, x, y)]
    
def get_valid_adjacent_positions(grid, x, y):
    adjacent_positions = get_adjacent_positions(x, y)
    valid_positions = [(x, y) for x, y in adjacent_positions if is_valid_position(grid, x, y)]

    return valid_positions

def get_adjacent_values(grid, x, y):
    adjacent_positions = get_valid_adjacent_positions(grid, x, y)
    return sum([grid[x, y] for x, y in adjacent_positions])

def convert_to_grid(string):
    pattern = string.split("\n")
    max_len = len(max(pattern, key=len))

    for index, row in enumerate(pattern):
        row = row.replace("O", "1")
        row = row.replace(".", "0")

        if len(row) < max_len:
            row += ("0" * (max_len - len(row)))

        pattern[index] = [int(cell) for cell in row]

    grid = np.array(pattern)

    return grid