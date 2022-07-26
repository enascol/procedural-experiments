import time
from PIL import Image
import numpy as np

import rules as _rules
import sys
import random

columns = 950
rows = 480
#rule = int(sys.argv[1])

def get_current_cell_value(grid, x):
    rules = _rules.get_rule(rule)
    
    if x == 0:
        left, middle, right = 0, grid[x], grid[x + 1]
    elif x == columns - 1:
        left, middle, right = grid[x - 1], grid[x], 0
    else:
        left, middle, right = grid[x - 1], grid[x], grid[x + 1]
    
    return  rules[(left, middle, right)]

def get_next_sequence(grid):
    if len(grid) == 0:
        sequence = [0 for _ in range(columns)]
        mid_cell_index = int(len(sequence) / 2)
        sequence[mid_cell_index] = 1
    else:
        sequence = []
        for index, _ in enumerate(grid[-1]):
            sequence.append(get_current_cell_value(grid[-1], index))
    
    return sequence

def build_grid():
    grid = []
    for x in range(rows):
        grid.append(get_next_sequence(grid))
    
    return grid

def convert_to_imag(grid, name ="hii"):
    for x in range(rows):
        for y in range(columns):
            pixel = grid[x][y]

            if pixel == 0:
                grid[x][y] = 255, 255, 255
            else:
                grid[x][y] = 0, 0, 0

    numpy_matrix = np.asarray(grid, dtype=np.uint8)
    img = Image.fromarray(numpy_matrix)
    img.save(f"{name}.png")

for x in range(256):
    rule = x
    convert_to_imag(build_grid(), name =f"rule {rule}")