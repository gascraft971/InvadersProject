import pygame
from pygame.locals import *
from classes import Entity

class Ship(Entity.Entity):
	def __init__(self, config) -> None:
		super().__init__(config)
