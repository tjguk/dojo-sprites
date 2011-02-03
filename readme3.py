import pygame
from pygame.locals import *
pygame.init ()

screen = pygame.display.set_mode ((400, 320))
screenrect = screen.get_rect ()

#
# So we're now able to draw a bunch of sprites together
# Which is fairly handy. But what else are sprites and
# groups good for?
#
# They're a versatile combination for determining aspects
# of gameplay such as collision and related movement.
#
class Hero (pygame.sprite.Sprite):
  def __init__ (self):
    super (Hero, self).__init__ ()
    self.image = pygame.Surface ((25, 25))
    self.image.fill ((192, 192, 192))
    self.rect = self.image.get_rect ()

class Poison (pygame.sprite.Sprite):
  image = pygame.Surface ((20, 20))
  image.fill ((255, 0, 0))
  def __init__ (self, initial_position):
    super (Poison, self).__init__ ()
    self.rect = self.image.get_rect (center=initial_position)

hero = Hero ()
hero.rect.topright = screenrect.topright
hero1 = pygame.sprite.GroupSingle (hero)
poisons = pygame.sprite.Group (Poison ((10, 10)), Poison ((20, 20)))
sprites = pygame.sprite.Group (hero, poisons)

screen.fill ((0, 0, 0))
sprites.draw (screen)
pygame.display.update ()
pygame.event.pump ()

#
# No collisions
#
print pygame.sprite.spritecollide (hero, poisons, False)


#
# Now move our hero towards the left of the screen
#
hero.rect.left = 25
screen.fill ((0, 0, 0))
sprites.draw (screen)
pygame.display.update ()
pygame.event.pump ()

print pygame.sprite.spritecollide (hero, poisons, False)

#
# So we can easily detect which sprites are overlapping with
# which and take action: add energy, kill the character etc.
#

#
# Notice how the "hero" appears behind the "poisons": we'll
# come back to that later.
#