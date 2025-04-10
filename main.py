import pygame
from settings import *
from sprites import *

class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    self.clock = pygame.time.Clock()
  
  def new(self):
    self.board = Board()
    self.board.display_board()
    self.first_click = True

  def run(self):
    self.playing = True
    while self.playing:
      self.clock.tick(FPS)
      self.events()
      # bc this is a click based game, don't need update 
      self.draw()
    else:
      self.end_screen()
  
  def draw(self):
    self.screen.fill(BGCOLOR)
    self.board.draw(self.screen)
    pygame.display.flip()

  def check_win(self):
    for row in self.board.board_list:
      for tile in row:
        if tile.type != "X" and not tile.revealed:
          return False
    return True

  def events(self):
    # when the user clicks x on the window, exits the game
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

      
      if event.type == pygame.MOUSEBUTTONDOWN:
        row, col = pygame.mouse.get_pos()
        # divide by tilesize to get index
        row //= TILESIZE
        col //= TILESIZE

        if self.first_click:
          self.board.place_mines(row, col)
          self.board.place_clues()

          self.first_click = False

        # left click to reveal tile 
        if event.button == 1:
          if not self.board.board_list[row][col].flagged:
            # dig and check if exploded 
            if not self.board.dig(row, col):
                #explode
                self.board.explode()
                self.playing = False

        # right click to flag
        if event.button == 3:
          if not self.board.board_list[row][col].revealed:
            # if its flagged --> not flagged, if not flagged --> flagged
            self.board.board_list[row][col].flagged = not self.board.board_list[row][col].flagged
        
        if self.check_win():
          self.win = True
          self.playing = False
          for row in self.board.board_list:
            for tile in row:
              if not tile.revealed:
                tile.flagged = True
  
  def end_screen(self):
    while True: 
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          return

game = Game()
while True: 
  game.new()
  game.run()