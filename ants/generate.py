import sys
import time
import random
sys.path.append("\\".join(__file__.split("\\")[:-2]))
from grid_generator.grid import *
from convert_to_image.convert import *

def update_position(base_grid, new_grid, x, y):
    possible_positions = get_valid_adjacent_positions(base_grid, x, y, check_empty =True)
    grid_value = base_grid[x, y]
    if possible_positions:
        new_x, new_y = random.choice(possible_positions)
        new_grid[new_x, new_y] = grid_value

        return new_grid
    
    return new_grid

def update_grid(grid):
    while True:
        new_grid = grid.copy()
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                if grid[x, y] != 0:
                    update_position(grid, new_grid, x, y)
        
        time.sleep(0.04)
        convert(grid)
        grid = new_grid
        
        if np.count_nonzero(grid == 0) == 0:
            break

rows, columns = 100, 100
grid = generate(rows, columns)
regions = 10 #int((100 * 100) / 50)
for n in range(regions + 1):
    x, y = random.randint(0, rows - 1), random.randint(0, columns - 1)
    grid[x, y] = n

update_grid(grid)
for x in range(rows):
    for y in range(columns):
        if grid[x, y] == 0:
            print(x, y)

print(np.count_nonzero(grid == 0))
        
