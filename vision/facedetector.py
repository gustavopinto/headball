# -*- coding: utf-8 -*-

from SimpleCV import Camera, Display, Image

class FaceDetector:
	def __init__(self):
		self.cam = Camera()

	def get_coordinates(self):
	    img = self.cam.getImage()

	    faces = img.findHaarFeatures('face')

	    if faces is not None:
	        face = faces.sortArea()[-1]
	        face.draw()

	        return (face.x, face.y)

	    raise FaceNotFound("fail")


class FaceNotFound(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)