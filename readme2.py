#
# So you've got a screen and you've got an image surface and you've
# got a rect which holds its current position.
#
import pygame
from pygame.locals import *
pygame.init ()

screen = pygame.display.set_mode ((400, 320))
tree = pygame.image.load ("c:/temp/tree.png")

clock = pygame.time.Clock ()

treepos = tree.get_rect (topleft=(0, 0))
while True:
  clock.tick (3)
  screen.fill ((0, 0, 0))
  screen.blit (tree, treepos)
  treepos.move_ip (10, 0)
  pygame.display.update ()
  pygame.event.pump ()

#
# And you decide that it would be a good object-oriented
# design to have a class which holds the image and its
# current position and which could draw itself on a
# surface.
#
# You've just reinvented the pygame Sprite. You just
# need an .image and a .rect.
#
class Tree (pygame.sprite.Sprite):
  def __init__ (self, initial_position):
    pygame.sprite.Sprite.__init__ (self)
    self.image = pygame.image.load ("c:/temp/tree.png")
    self.rect = self.image.get_rect (topleft=initial_position)
    self.movement = 10, 0
  def update (self):
    self.rect.move_ip (self.movement)

#
# Slightly odd that the base class doesn't
# have a .draw method, but most sprites live
# in groups... and you can easily add one yourself.
#

tree1 = Tree ((10, 10))
tree2 = Tree ((50, 50))

screen.fill ((0, 0, 0))
screen.blit (tree1.image, tree1.rect)
screen.blit (tree2.image, tree2.rect)
pygame.display.update ()
pygame.event.pump ()

#
# Not particularly useful on its own: a bit of encapsulation, nothing more.
# But now look at Sprite groups
#
trees = pygame.sprite.Group ()
trees.add (tree1, tree2)

screen.fill ((0, 0, 0))
trees.update ()
trees.draw (screen)
pygame.display.update ()
pygame.event.pump ()

