from multiprocessing.sharedctypes import Value
import sys
sys.path.append("./")
from grid_generator import grid as grd
from convert_to_image import convert

import random
import time

def is_valid_and_empty(grid, cur_x, cur_y, x, y):
    is_a_valid_pos = grd.is_valid_position(grid, x, y)

    if (x, y) in ((cur_x + 1, cur_y - 1), (cur_x + 1, cur_y + 1)):
        pos = x - 1, y
        if grd.is_valid_position(grid, pos[0], pos[1]):
            has_free_way = grid[pos[0]][pos[1]] == 0
        else:
            return False
    else:
        has_free_way = True
    
    if is_a_valid_pos:
        is_empty = grid[x][y] == 0
    else:
        is_empty = False

    return is_a_valid_pos and is_empty and has_free_way

def update_grid(grid, x, y):
    bottom, bottom_left, bottom_rght = (x + 1, y), (x + 1, y - 1) , (x + 1, y + 1)
    
    empty_valid_positions = list(
        filter(
            lambda pos: is_valid_and_empty(grid, x, y, pos[0], pos[1]),
            (bottom, bottom_left, bottom_rght)
        )
    )
    if len(empty_valid_positions) >= 1:
        if bottom in empty_valid_positions:
            grid[bottom[0]][bottom[1]] = 1
        else:
            new_x, new_y = random.choice(empty_valid_positions)
            grid[new_x][new_y] = 1
        grid[x][y] = 0


def run(grid, iterations  =10):
    rows, columns =  len(grid), len(grid[0])
    while True:
        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == 1:
                    update_grid(grid, x, y)
    
            convert.convert(grid)
            time.sleep(0.1)

grid = grd.generate(100, 100)
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if random.randint(1, 100) < 10:
            grid[x][y] = 1

run(grid)
