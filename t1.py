import os, sys
import random

import pygame
from pygame.locals import *
pygame.init ()

screen = pygame.display.set_mode ((400, 320))

class Character (pygame.sprite.DirtySprite):

  image = pygame.image.load ("character.png").convert ()

  def __init__ (self, initial_location):
    pygame.sprite.DirtySprite.__init__ (self)
    self.rect = pygame.rect.Rect (initial_location, self.image.get_rect ().size)
    self.speed = 5

  def move (self, direction_keystroke):
    self.dirty = True
    original_rect = self.rect
    if direction_keystroke == K_UP:
      self.rect.move_ip (0, -self.speed)
    elif direction_keystroke == K_DOWN:
      self.rect.move_ip (0, self.speed)
    elif direction_keystroke == K_LEFT:
      self.rect.move_ip (-self.speed, 0)
    elif direction_keystroke == K_RIGHT:
      self.rect.move_ip (self.speed, 0)
    return [original_rect, self.rect]

class TreeSprite (pygame.sprite.DirtySprite):

  image = pygame.image.load ("tree.png").convert ()

  def __init__ (self, initial_location):
    pygame.sprite.DirtySprite.__init__ (self)
    self.rect = pygame.rect.Rect (initial_location, self.image.get_rect ().size)

class Terrain (pygame.sprite.DirtySprite):

  image = pygame.image.load ("ground.png").convert ()
  width = image.get_rect ().width
  height = image.get_rect ().height

  def __init__ (self, location):
    pygame.sprite.DirtySprite.__init__ (self)
    self.rect = pygame.rect.Rect (location, self.image.get_rect ().size)

def main ():

  background = pygame.sprite.RenderUpdates ()
  for n_row in range (1 + screen.get_rect ().height / Terrain.height):
    for n_col in range (1 + screen.get_rect ().width / Terrain.width):
      background.add (Terrain ((n_col * Terrain.width, n_row * Terrain.height)))
  character = Character ((50, 50))
  trees = pygame.sprite.RenderUpdates ([TreeSprite ((100, 100))])

  while True:
    background.draw (screen)
    trees.draw (screen)
    screen.blit (character.image, character.rect)
    pygame.display.update ()

    for event in pygame.event.get ():
      if event.type == QUIT:
        sys.exit ()
      elif event.type == KEYDOWN:
        print "Checking for keystroke", event.key
        if event.key in (K_UP, K_DOWN, K_LEFT, K_RIGHT):
          updated.extend (character.move (event.key))

if __name__ == '__main__':
  main ()
