WAVFILE = 'explode.wav'
import pygame
from pygame import *
import sys

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
pygame.mixer.get_init() 

exp = pygame.mixer.Sound('explode.wav')
ch = exp.play()
pygame.time.delay(1200)

pew = pygame.mixer.Sound('pew.ogg')
ch = pew.play()
pygame.time.delay(1000)
