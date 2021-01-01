import pygame
from pygame.locals import *
from classes import Entity

class Ship(Entity.Entity):
	def __init__(self, config, scene) -> None:
		super().__init__(config, scene)
