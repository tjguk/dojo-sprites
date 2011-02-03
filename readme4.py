import pygame
from pygame.locals import *
pygame.init ()

screen = pygame.display.set_mode ((400, 320))
screenrect = screen.get_rect ()


# But we're still redrawing all the window and all our our sprites
# all the time.
#
# So far we've covered only the simplest sprite and the simplest
# sprite group: there are several varieties of each, but we're
# going to jump to the Rolls Royce version: the LayeredDirty
# group holding DirtySprites.
#
# DirtySprites have an attribute -- .dirty -- which is set or
# reset to indicate whether they need to be redrawn.
#
# The LayeredDirty group takes account of this setting, and also
# allows for sprites to be drawn in specific layers, so that
# the background is drawn before the foreground and the foreground
# before the characters. That way, the hero walks in front of a
# tree and not behind it -- assuming that's what you want!
#

class Hero (pygame.sprite.DirtySprite):
  def __init__ (self, initial_position=(300, 200)):
    super (Hero, self).__init__ ()
    self.image = pygame.Surface ((50, 50))
    self.image.fill ((192, 192, 192))
    self.rect = self.image.get_rect (center=initial_position)
    self.movement = 20, 0
  def update (self):
    newrect = self.rect.move (self.movement).clamp (screenrect)
    if newrect != self.rect:
      self.dirty = 1
      self.rect = newrect

import random

class Food (pygame.sprite.DirtySprite):
  image = pygame.Surface ((20, 20))
  image.fill ((0, 0, 255))
  def __init__ (self, initial_position=None):
    super (Food, self).__init__ ()
    if initial_position is None:
      initial_position = (
        random.randint (0, screenrect.width),
        random.randint  (0, screenrect.height)
      )
    self.rect = self.image.get_rect (topleft=initial_position)
    self.dirty = 1

hero = Hero ()
food = pygame.sprite.Group (*[Food () for f in range (3)])
sprites = pygame.sprite.LayeredDirty (_use_update=True)
sprites.add (food, layer=1)
sprites.add (hero, layer=2)

screen.fill ((0, 0, 0))
sprites.update ()
updated = sprites.draw (screen)
print updated
pygame.display.update (updated)
pygame.event.pump ()
