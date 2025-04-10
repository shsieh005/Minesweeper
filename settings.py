import pygame 
import os

# COLORS (r, g, b)
DARKGREY = (40, 40, 40)
BGCOLOR = DARKGREY

# game settings
TILESIZE = 32
ROWS = 15
COLUMNS = 15
MINES_NUM = 40
WIDTH = TILESIZE * COLUMNS
HEIGHT = TILESIZE * ROWS
FPS = 60
TITLE = "Minesweep!"

tile_numbers = []
for i in range(1, 9):
  # retrieve image, then transform the image to TILESIZE, TILESIZE
  tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileEmpty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileExploded.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileMine.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileFlag.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileNotMine.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileUnknown.png")), (TILESIZE, TILESIZE))