import os, sys
import random

import pygame
from pygame.locals import *

class Bouncer (pygame.sprite.DirtySprite):
  def __init__ (self, image, topleft=(0,0)):
    super (Bouncer, self).__init__ ()
    self.image = image
    self.rect = self.image.get_rect (topleft=topleft)
    self.speed = random.randint (1, 10)
    self.movement = [self.speed*random.choice ([-1, 0, 1]), self.speed*random.choice ([-1, 0, 1])]
  def update (self):
    self.rect.move_ip (self.movement)
    if self.rect.left < screenrect.left:
      self.movement[0] = self.speed
    if self.rect.right > screenrect.right:
      self.movement[0] = -self.speed
    if self.rect.top < screenrect.top:
      self.movement[1] = self.speed
    if self.rect.bottom > screenrect.bottom:
      self.movement[1] = -self.speed
    self.dirty = 1
