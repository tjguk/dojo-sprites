# Basically, pygame about drawing things onto other things and ultimately onto the screen

# At heart, two concepts: Surfaces & Rects

# Everything you draw and draw onto is a surface: the window, images you load, text you draw, and any arbitrary surface you create

import pygame
from pygame.locals import *
pygame.init ()

screen = pygame.display.set_mode ((400, 320))
print screen

#
#
# import threading
# threading.Thread (target=pump).start ()

image = pygame.image.load ("c:/temp/tree.png").convert ()
print image

screen.blit (image, (0, 0))
pygame.display.update ()
pygame.event.pump ()

# Every image has a rectangle:

print screen.get_rect ()
print image.get_rect ()

# And you can create you own from scratch:

r = pygame.Rect (100, 50, 120, 130)
print r

#
# But the great thing is that it's got loads
# of obvious but useful attributes... and you
# can read or set them all.
#

print r.top
print r.left
print r.topleft

print r.bottom
print r.right
print r.bottomright

print r.topright
print r.bottomleft

print r.width
print r.height
print r.size

print r.centerx
print r.centery
print r.center

print r
r.top += 25
print r
r.center = (200, 125)
print r

#
# You can also use an array of methods to change attributes
# of the rect, including moving and sizing. These mostly come
# in pairs, one which returns a new instance and the other
# which mutates in-place
#

print r
_ = r.move ((50, -50))
print r
_ = r.move_ip ((50, -50))
print r

