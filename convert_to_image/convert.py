from copy import deepcopy
import cv2

import numpy as np
import random

def get_random_color(base=(None, None, None)):
    r, g, b = base
    
    if not r: r = random.randint(0, 255)
    if not b: b = random.randint(0, 255)
    if not g: g = random.randint(0, 255)

    return r, g, b

def convert(matrix, name ="IMG", colors = {1: (255, 255, 255), 0: (0, 0, 0)}):
    rows, columns =  len(matrix), len(matrix[0])
    base = [[0 for _ in range(columns)] for _ in range(rows)]

    for x in range(rows):
        for y in range(columns):
            pixel = matrix[x][y]
            try:
                base[x][y] = colors[pixel]
            except KeyError:
                print('Adding new color')
                pixel_color = [random.randint(0, 255) for x in range(3)]
                colors[pixel] = pixel_color
                base[x][y] = colors[pixel]

    base = np.asarray(base, dtype=np.uint8)
    cv2.imwrite(f'{name}.png', cv2.cvtColor(base, cv2.COLOR_RGB2BGR))
    #cv2.imshow("image", img)
    #cv2.waitKey()

#    numpy_matrix = np.asarray(base, dtype=np.uint8)
#    img = Image.fromarray(numpy_matrix)
#    img.save(f"{name}.png")
