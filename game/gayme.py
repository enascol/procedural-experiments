from re import A
import time
from random import randint
import pygame
import sys
import random

sys.path.append("./")
from grid_generator import grid as grd
from cave_generator import automata

pygame.init()
rows = 1024
columns = 1024
screen = pygame.display.set_mode((columns, rows))

clock = pygame.time.Clock()
grid = grd.generate(rows, columns, 60)
new_grid = automata.run(grid, 4)

def show_grid(grid):
    surface = pygame.Surface((columns, rows))
    pa = pygame.PixelArray(surface)

    for x in range(rows):
        for y in range(columns):
            pixel_value = grid[x][y]
            pa[x, y] = automata.COLORS[pixel_value]
    
    del pa
    screen.blit(surface, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            y, x = pygame.mouse.get_pos()
            grid[x][y] = 1

    show_grid(new_grid)
    pygame.display.flip()
    clock.tick(60)