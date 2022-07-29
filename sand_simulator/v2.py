import sys
sys.path.append("./")
from grid_generator import grid as grd
from convert_to_image import convert
import particles

import numpy as np
import random
import time

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = np.zeros(shape = (self.rows, self.columns))

    def __setitem__(self, index, value):
        self.grid[index] = value
    
    def __getitem__(self, index):
        return self.grid[index]

    def __len__(self):
        return len(self.grid)

    def generate(self, density =0):
        for x in range(self.rows):
            for y in range(self.columns):
                add_noise = density > random.randint(1, 100)
                self.grid[x][y] = add_noise * 1
    
    def show(self):
        for rows in self.grid:
            print(rows)
    
    def is_movable_position(self, x, y, curx, cury):
        is_valid = grd.is_valid_position(self.grid, x, y)
        
        if is_valid:
            is_empty = self.grid[x][y] == 0
        else:
            return False

        if (x, y) in ((curx + 1, cury - 1), (curx + 1, cury +1)):
            x2, y2 = x - 1, y
            has_free_side = grd.is_valid_position(self.grid, x2, y2) and self.grid[x2][y2] == 0
        else:
            has_free_side = True

        return is_valid and is_empty and has_free_side

    def upgrade_sand_position(self, cur_grid, x, y, step =1):
        bottom, bottom_left, bottom_rght = (x + step, y), (x + step, y - step) , (x + step, y + step)

        empty_valid_positions = list(
            filter(
                lambda pos: self.is_movable_position(pos[0], pos[1], x, y),
                (bottom, bottom_left, bottom_rght)
            )
        )
        
        pixel_value = grid[x][y]

        if len(empty_valid_positions) >= 1:
            if bottom in empty_valid_positions:
                cur_grid[bottom[0]][bottom[1]] = pixel_value
            else:
                new_x, new_y = random.choice(empty_valid_positions)
                cur_grid[new_x][new_y] = pixel_value
            
            cur_grid[x][y] = 0
    
    def upgrade_water_position(self, cur_grid, x, y, step =1):
        a_pos  = (x + 1, y), (x, y + 1), (x, y - 1)

        empty_valid_positions = list(
            filter(
                lambda pos: self.is_movable_position(pos[0], pos[1], x, y),
                a_pos
            )
        )
        
        bottom = (x + 1, y)

        if len(empty_valid_positions) >= 1:
            if bottom in empty_valid_positions:
                cur_grid[bottom[0]][bottom[1]] = 2
            else:
                new_x, new_y = empty_valid_positions[0]
                cur_grid[new_x][new_y] = 2
            
            cur_grid[x][y] = 0


rows, columns = 100, 100
grid = Grid(rows, columns)
grid.generate(density = 0)

bg_color = 	(0, 0, 0)
sand_color = 168, 143, 74
platform_color = [random.randint(0, 255) for x in range(3)]

column  = int(columns / 2)

colors = {1: sand_color, 0: bg_color, 3: platform_color, 2: (5, 247, 183)}

row_range = range(10, rows - 10)
column_range = range(10, columns - 10)

def add_random_block(rate):
    for x in range(int(rows * columns / rate)):
        r, c = random.choice(row_range), random.choice(column_range)
        grid[r][c] = 3

def add_random_platforms(amount, platform_size):
    for x in range(amount):
        r, c = random.choice(row_range), random.choice(column_range)
        for l in range(platform_size):
            if grd.is_valid_position(grid, r, c + l):
                grid[r][c + l] = 3

add_random_block(25)

c1 = column - int(columns / 3)
c2 = column
c3 = column + int(columns / 3)

spread = 0

count = 5

while True:
    cur_grid = grd.copy(grid.grid)

    cur_grid[0][random.randint(c1 - spread, c1 + spread)] = random.choice(range(3, count))
    cur_grid[0][random.randint(c2 - spread, c2 + spread)] = random.choice(range(3, count))
    cur_grid[0][random.randint(c3 - spread, c3 + spread)] = random.choice(range(3, count))
    for x in range(grid.rows):
        for y in range(grid.columns):
            pixel_v = grid[x][y]
            if grid[x][y] in  range(4, count):
                grid.upgrade_sand_position(cur_grid, x, y, step =1)
            elif grid[x][y] == 2:
                grid.upgrade_water_position(cur_grid, x, y, step =1)
    
    if count < 20:
        count += 1
        colors[count] = [random.randint(0, 255) for x in range(3)]

    grid.grid = cur_grid
    convert.convert(grid, "grid", colors = colors)
    time.sleep(0.04)