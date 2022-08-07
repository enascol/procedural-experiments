import sys
import time
import numpy as np

sys.path.append("./")
from grid_generator.grid import *
import convert_to_image.convert as cvt
from generator import *

rows, columns = 100, 200
grid = generate(rows, columns, noise_density=70)

cvt.convert(grid)
while True:
    grid = update_grid(grid, prob = False)
    time.sleep(0.03)
    cvt.convert(grid)

    
            
