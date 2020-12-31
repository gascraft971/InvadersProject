import pygame
from pygame.locals import *
from classes import Level

class GameLevel(Level.Level):
	def __init__(self, config):
		super().__init__(config)
		self.bgImage = pygame.image.load(self.config["graphics"]["bg"]).convert()
		self.surface = pygame.transform.scale(self.bgImage, (self.config["window"]["width"], self.config["window"]["height"]))