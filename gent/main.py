import gent
import sys
import time

sys.path.append('./')
from convert_to_image.convert import convert

ITERATIONS, CELL_TYPES = [int(setting) for setting in sys.argv[1:]]

rows, columns = 100, 100
grid = gent.generate_random_grid(rows, columns, CELL_TYPES)
final_grid, color_map = gent.iterate(grid, ITERATIONS, save_once =False)
time.sleep(0.5)
for x in range(100):
    grid = gent.remove_single_pixes(final_grid)
    convert(grid, colors = color_map[1])
    time.sleep(0.05)
