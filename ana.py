import pygame
from pygame.locals import *

pygame.init()

while(True):
   for event in pygame.event.get():
      if (event.type == KEYDOWN):
         print event
         if (event.key == K_a):
         	print "a"
         if (event.key == K_b):
         	print "b"