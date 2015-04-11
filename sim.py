# coding=UTF_8
import pygame
from globalvals import *

MAX_SCREEN_WIDTH = 800
POINTS_PER_FRAME = 800
DECAY = 64

class SIM(object):
	def __init__(self):
		# calcul taille et zoom

		self.screen_w = MAX_SCREEN_WIDTH
		self.screen_scale = float(self.screen_w) / (MAX_X - MIN_X)
		#self.screen_scale = 0.01
		self.screen_h = int((MAX_Y - MIN_Y) * self.screen_scale)

		self.screen = pygame.display.set_mode([self.screen_w,self.screen_h])
		self.screen2 = self.screen.copy()

		pygame.display.set_caption("Aperçu projection")
		self.clock = pygame.time.Clock()

		self.xy_prev = (0,0)

	def play_stream(self, stream):

		def convert_coord(xy_laser):
			return ((MAX_X-xy_laser[0]) * self.screen_scale, (MAX_Y - xy_laser[1]) * self.screen_scale)
		def convert_color(c_laser):
			return [256*comp//(CMAX+1) for comp in c_laser]


		while True:
			self.screen2.fill((0,0,0))

			points = stream.read(POINTS_PER_FRAME)
			for point_cur in points:
				xy_cur = convert_coord(point_cur[0:2])
				pygame.draw.line(self.screen2, convert_color(point_cur[2:5]), self.xy_prev, xy_cur)
				self.xy_prev = xy_cur

			# effet rémanence
			self.screen.fill((DECAY,DECAY,DECAY),None,pygame.BLEND_RGB_SUB)
			self.screen.blit(self.screen2,(0,0),None,pygame.BLEND_ADD)

			pygame.display.flip()
			# FPS
			self.clock.tick(60)

		

