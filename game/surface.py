import pygame
import random
import sys

sys.path.append("./")
from grid_generator import grid as grd

DEAD = (0, 0, 0)
ALIVE = (194, 178, 128)

class Surface:

    def __init__(self, width, height):
        self.rows = height
        self.columns = width
        self.surface = pygame.Surface((self.columns, self.rows))
    
    def populate(self):
        for x in range(self.rows):
            for y in range(self.columns):
               print(x, y, self.surface.get_at((y, x)))
    
    def __setitem__(self, index, value):
        x, y = index
        self.set(x, y, value)
    
    def __getitem__(self, index):
        x, y = index
        return self.get(x, y)

    def set(self, x, y, value):
        if x >= self.rows or y >= self.columns:
            raise IndexError(f"invalid indexes [{x}, {y}]")
        
        self.surface.set_at((y, x), value)
    
    def get(self, x, y):
        return self.surface.get_at((y, x))
    
    def is_valid(self, x, y):
        valid_x = x >= 0 and x < self.rows
        valid_y = y >= 0 and y < self.columns

        return valid_x and valid_y
    
    def get_cell_value(self, x, y):
        if self[x, y] == DEAD:
            return 0
        
        if self[x, y] == ALIVE:
            return 1

    def get_valid_positions(self, x, y):
        return [(x, y) for x, y in grd.get_adjacent_positions(x, y) if self.is_valid(x, y)]

    def update_position(self, new_grid, x, y):
        valid_positions = self.get_valid_positions(x, y)
        value = [self.get_cell_value(cx, cy) for cx, cy in valid_positions]

        cell_value = self.get_cell_value(x, y)
        cell_state = self[x, y]

        if cell_value == ALIVE and value >= 4:
            new_grid[x, y] = DEAD
        elif cell_value == ALIVE and value <= 1:
            new_grid[x, y] = DEAD
        elif cell_value == DEAD and value == 3:
            new_grid[x, y] = ALIVE
        else:
            new_grid[x, y] = cell_state
    
    def clone(self):
        surface = pygame.Surface((self.columns, self.rows))
        for x in range(self.rows):
            for y in range(self.columns):
                surface.set_at((y, x), self[x, y])
        
        return surface
    
    def update_grid(self):
        new_surface = Surface(self.rows, self.columns)
        new_surface.surface = self.clone()

        for x in range(self.rows):
            for y in range(self.columns):
                self.update_position(new_surface, x, y)
        
        self.surface = new_surface.surface


