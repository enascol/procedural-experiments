import sys
import time
import rules

sys.path.append("./")
from grid_generator.grid import *
from convert_to_image.convert import *

RULE = 100

def name_neighboors(x, y, neighboors):
    n = {}
    for nx, ny in neighboors:
        if  (nx, ny) == (x + 1, y):
            n["down"] = (nx, ny)
        if  (nx, ny) == (x - 1, y):
            n["up"] = (nx, ny)
        if  (nx, ny) == (x, y - 1):
            n["left"] = (nx, ny)
        if  (nx, ny) == (x, y + 1):
            n["right"] = (nx, ny)
    
    return n

def update_position(base_grid, grid, x, y, rule_set):
    n = get_valid_vn_neighboorhood(base_grid, x, y)
    named_neighboors = name_neighboors(x, y, n)

    config = ()
    for name in "up right down left".split():
        try:
            px, py = named_neighboors[name]
            config += (base_grid[px, py], )
        except KeyError:
            config += (0, )
    
    
    grid[x][y] = rule_set[config]
    return grid

def update_grid(grid, rule_set, rule_name):
    rows, columns = grid.shape
    new_grid = grid.copy()
    color = {1: get_random_color(), 0: get_random_color()}
    while True:
        convert(grid, f"automata_v2", colors = color)
        for x in range(rows):
            for y in range(columns):
                grid = update_position(grid, new_grid,x, y, rule_set)
        
        time.sleep(0.05)


rows, columns = 50, 100
grid = generate(rows, columns, 20)
mx, my = int(rows / 2), int(columns / 2)
grid[mx, my] = 1
rule = random.randint(0, rules.get_rule_size() - 1)
rule_set = rules.get(rule)
print(f"Rule {rule}")
update_grid(grid, rule_set, rule)




