# -*- coding: utf-8 -*-

class GameObject:
	def __init__(self, image):
		self.img = image
		self.pos = image.get_rect().move(0, 0)

	def move(self, speed):
		self.pos = self.pos.move(speed)
		return self