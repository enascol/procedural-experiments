import cv2
import  inspect
import numpy as np
import os.path
import random
import sys

sys.path.append("./")
from grid_generator.grid import copy as copy_grid
from color_manipulation import colors

import PATHS

def convert(matrix, name ="IMG", colors = {1: (255, 255, 255), 0: (0, 0, 0)}):
    rows, columns =  len(matrix), len(matrix[0])
    base = [[0 for _ in range(columns)] for _ in range(rows)]
    
    for x in range(rows):
        for y in range(columns):
            pixel = matrix[x][y]
            try:
                base[x][y] = colors[pixel]
            except KeyError:
                pixel_color = [random.randint(0, 255) for x in range(3)]
                colors[pixel] = pixel_color
                base[x][y] = colors[pixel]

    if not os.path.exists(PATHS.IMAGE_FOLDER):
        os.mkdir(PATHS.IMAGE_FOLDER)
    
    name = inspect.stack()[1].filename.split("\\")[-2]
    path_to_save = PATHS.save_image_path(f"{name}.png")
    base = np.asarray(base, dtype=np.uint8)
    cv2.imwrite(path_to_save, cv2.cvtColor(base, cv2.COLOR_RGB2BGR))

    return base, colors
