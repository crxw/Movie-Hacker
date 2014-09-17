__author__ = 'caleb'
# TODO; maybe create a working linux terminal with animations, images, and sound to mimic the appearance of movie hacking.
# TODO; accept user typing
# TODO; fire off some activity, screen display, movie clip view, on user typing

# From http://inventwithpython.com/pygame/chapter2.html
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()