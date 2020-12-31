import pygame
from pygame.locals import *
from classes import Scene

class Level:
	def __init__(self, config):
		self.config = config
		self.surface = surface = pygame.Surface((self.config["window"]["width"], self.config["window"]["width"]))

	def getSurface(self):
		return self.surface