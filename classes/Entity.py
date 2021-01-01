import pygame, uuid
from pygame.locals import *
from classes import P, V

class Entity(pygame.sprite.Sprite):
	def __init__(self, config) -> None:
		super().__init__()
		self.config = config
		self.id = uuid.uuid4()
		self.position = P.P(200, 200)
		self.velocity = V.V(0, 0)
		self.image = pygame.Surface((0, 0))
		self.updateRect()
	
	def updateRect(self) -> None:
		self.rect = self.image.get_rect()
		self.rect.centerx = int(self.position.getX())
		self.rect.centery = int(self.position.getY())