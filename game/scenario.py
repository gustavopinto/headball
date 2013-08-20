# -*- coding: utf-8 -*-
import sys, pygame
from vision.facedetector import FaceDetector, FaceNotFound

class Scenario:

	def __init__(self):
		pygame.init()

		self.size = self.width, self.height = 800, 600
		self.screen = pygame.display.set_mode(self.size)
		self.ball = self.load_object()

		self.face = FaceDetector()
		self.coordinates = (1,1)

	def load_object(self):
		from objects import GameObject
		icon = pygame.image.load('images/ball.gif')
		return GameObject(icon)		

	def update_scenario(self):
		backgorund = 0,0,0
		try:
			self.screen.fill(backgorund)
			self.screen.blit(self.ball.img, self.face.get_coordinates())
			self.coordinates = self.face.get_coordinates()
		except FaceNotFound: 
			self.screen.blit(self.ball.img, self.coordinates)
		
		pygame.display.flip()


	def run_game(self):

		speed = [1,1]

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()

			self.ball = self.ball.move(speed)

			if self.ball.pos.left < 0 or self.ball.pos.right > self.width:
				speed[0] = -speed[0]

			if self.ball.pos.top < 0 or self.ball.pos.bottom > self.height:
				speed[1] = -speed[1]

			self.update_scenario()
