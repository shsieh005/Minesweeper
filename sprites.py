import pygame
from settings import *
import random

class Tile:
  # Properties of a tile:
  # location on grid (r,c), tcpe (unknown, mine, clue, emptc), revealed, flagged 

  # tcpes list 
  # "." -> unknown
  # "r" -> mine
  # "C" -> clue
  # "/" -> empty
  def __init__(self, row, col, image, type, revealed=False, flagged=False):
    self.row = row * TILESIZE
    self.col = col * TILESIZE
    self.image  = image
    self.type = type
    self.revealed = revealed
    self.flagged = flagged

  # shows how an object is represented in string format
  # so when print(Tile) --> tcpe 
  def __repr__(self):
    return self.type

  def draw(self, board_surface):
    # col --> width, row --> height 
    if not self.flagged and self.revealed:
      board_surface.blit(self.image, (self.row, self.col))
    elif self.flagged and not self.revealed:
      board_surface.blit(tile_flag, (self.row, self.col))
    elif not self.revealed:
      board_surface.blit(tile_unknown, (self.row, self.col))


class Board:
  def __init__(self):
    self.board_surface = pygame.Surface((WIDTH, HEIGHT))
    self.board_list = [[Tile(row, col, tile_empty, ".") for col in range(COLUMNS)] for row in range(ROWS)]
    self.dug = [] # keep track of tiles we already checked

  def display_board(self):
    for r in self.board_list:
      print(r)
  
  def draw(self, screen):
    for row in self.board_list:
      for tile in row:
        tile.draw(self.board_surface)
    # blit board surface at (0, 0)
    screen.blit(self.board_surface, (0, 0))

  def place_mines(self, row, col):
    # place mines at grids across boards
    for _ in range(MINES_NUM):
      while True:
        c = random.randint(0, COLUMNS - 1)
        r = random.randint(0, ROWS - 1)
        print((r, c))
        if self.board_list[r][c].type == "." and r != row and c != col:
          self.board_list[r][c].image = tile_mine
          self.board_list[r][c].type = "X"
          break
  
  def place_clues(self):
    # place clues at grids across boards
    for r in range(ROWS):
      for c in range(COLUMNS):
        if self.board_list[r][c].type != "X":
          mine_count = self.check_neighbors(r, c)
          if mine_count > 0:
            self.board_list[r][c].type = "C"
            self.board_list[r][c].image = tile_numbers[mine_count - 1]

  @staticmethod
  def is_inside(r, c):
    return 0 <= r < ROWS and 0 <= c < COLUMNS

  def check_neighbors(self, r, c):
    total_mines = 0
    for r_offset in range(-1, 2):
      for c_offset in range(-1, 2):
        neighbor_r = r + r_offset
        neighbor_c = c + c_offset
        if self.is_inside(neighbor_r, neighbor_c) and self.board_list[neighbor_r][neighbor_c].type == "X":
          total_mines += 1
    return total_mines
  
  def dig(self, r, c):
    self.dug.append((r, c))
    if self.board_list[r][c].type == "X":
      self.board_list[r][c].revealed = True
      self.board_list[r][c].image = tile_exploded
      return False
    elif self.board_list[r][c].type == "C":
      self.board_list[r][c].revealed = True
      return True # once we hit a clue, we want to stop 
    
    self.board_list[r][c].revealed = True

    for row in range(max(0, r - 1), min(ROWS - 1, r + 1) + 1):
      for col in range(max(0, c - 1), min(COLUMNS - 1, c + 1) + 1):
         if (row, col) not in self.dug:
           self.dig(row, col)
    
    return True
  
  def explode(self):
    for row in self.board_list:
      for tile in row:
        if tile.flagged and tile.type != "X":
          tile.flagged = False
          tile.revealed = True
          tile.image = tile_not_mine
        elif tile.type == "X":
          tile.revealed = True
      

