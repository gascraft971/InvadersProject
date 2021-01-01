import pygame
from pygame.locals import *
from classes import Scene

class Level:
	def __init__(self, config, scene: Scene) -> None:
		self.config = config
		self.entities = pygame.sprite.Group()
		self.scene = scene
		self.surface = surface = pygame.Surface((self.config["window"]["width"], self.config["window"]["width"]))

	def getSurface(self) -> pygame.Surface:
		return self.surface