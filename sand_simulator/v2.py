import sys
sys.path.append("./")
from grid_generator import grid as grd
from convert_to_image import convert
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

    def upgrade_position(self, x, y):
        bottom, bottom_left, bottom_rght = (x + 1, y), (x + 1, y - 1) , (x + 1, y + 1)

        empty_valid_positions = list(
            filter(
                lambda pos: self.is_movable_position(pos[0], pos[1], x, y),
                (bottom, bottom_left, bottom_rght)
            )
        )
        
        if len(empty_valid_positions) >= 1:
            if bottom in empty_valid_positions:
                self.grid[bottom[0]][bottom[1]] = 1
            else:
                new_x, new_y = random.choice(empty_valid_positions)
                self.grid[new_x][new_y] = 1
            
            self.grid[x][y] = 0
        

grid = Grid(100, 100)
grid.generate(density = 5)
grid[0][50] = 1
grid[0][0] = 1

for x in range(grid.rows):
    for y in range(grid.columns):
        if grid[x][y] == 1:
            grid.upgrade_position(x, y)
    convert.convert(grid, "grid")
    time.sleep(0.1)