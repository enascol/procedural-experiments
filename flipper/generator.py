import sys
import time
import pygame

sys.path.append("./")
from grid_generator.grid import *
from convert_to_image.convert import convert

rows, columns = 500, 500
screen =  pygame.display.set_mode((rows, columns))

pos = (250, 250)
grid = generate(500, 500)
block_size = 20

def draw_grid(grid):
    for x in range(rows):
        for y in range(columns):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)

            if (x, y) == pos:
                color = [random.randint(0, 255) for _ in range(3)]
            else:
                color = (255, 255, 255) if grid[x, y] == 1 else (0, 0, 0)
            
            pygame.draw.rect(screen, color, rect)
    
    pygame.display.flip()
while True: 
    draw_grid(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid = generate(rows, columns, random.randint(1, 100))
    
