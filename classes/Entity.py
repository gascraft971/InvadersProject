import pygame
from pygame.locals import *
from classes import P, V
import uuid

class Entity(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.id = uuid.uuid4()
		self.position = P(0, 0)
		self.velocity = V(0, 0)
		self.image = pygame.Surface((0, 0))
		self.rect = self.image.get_rect()
		self.rect.x = int(self.position.getX())
		self.rect.y = int(self.position.getY())