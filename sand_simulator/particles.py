import random
import sys

sys.path.append("./")
from grid_generator import grid as grd

class Particle:
    def __init__(self, grid, row, column, value =0, step =1):
        self.row = row
        self.column = column
        self.value = value
        self.step = 1
        self.grid = grid

    def get_position(self):
        return self.row, self.column
    
    def set_position(self, x,  y, value):
        self.row = x
        self.column = 1
        self.value = value

    def is_movable_position(self, x, y):
        curx, cury = self.get_position()

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
    
class Sand(Particle):
    DEFAULT_VALUE = 1

    def __init__(self, row, column,  value):
        super().__init__(row, column, value)
    
    def update_position(self, x, y):
        step = self.step

        bottom, bottom_left, bottom_rght = (x + step, y), (x + step, y - step) , (x + step, y + step)

        empty_valid_positions = list(
            filter(
                lambda pos: self.is_movable_position(self.grid ,pos[0], pos[1]),
                (bottom, bottom_left, bottom_rght)
            )
        )
        
        if len(empty_valid_positions) >= 1:
            if bottom in empty_valid_positions:
                cur_grid[bottom[0]][bottom[1]] = 1
            else:
                new_x, new_y = empty_valid_positions[0]
                cur_grid[new_x][new_y] = 1
            
            cur_grid[x][y] = 0
        