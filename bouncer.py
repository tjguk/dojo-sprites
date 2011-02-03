import os, sys
import random

import pygame
from pygame.locals import *

class Bouncer (pygame.sprite.DirtySprite):
  def __init__ (self, image):
    super (Bouncer, self).__init__ ()
    self.image = image
    self.rect = self.image.get_rect (topleft=(random.randint (0, 100), random.randint (0, 100)))
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

    for group in self.groups ():
      for sprite in pygame.sprite.groupcollide (self, group, False):
        if sprite != self:
          self.movement = [m*-1 for m in self.movement]
          break

    self.dirty = 1
