import pygame, uuid
from pygame.locals import *
from classes import P, V

class Entity(pygame.sprite.Sprite):
	def __init__(self, config) -> None:
		super().__init__()
		self.config = config
		self.id = uuid.uuid4()
		self.position = P.P(0, 0)
		self.rotation = 0 # Rotation of the ship in degrees. 0 is facing up. Clockwise.
		self.velocity = V.V(0, 0)
		self.originalImage = pygame.Surface((0, 0)) # Since we'll be changing this image, we can reference the original one here
		self.image = self.originalImage
		self.updateRect()
	
	def updateRect(self) -> None:
		self.image = pygame.transform.rotate(self.originalImage, -self.rotation) # We need -rotation, because normal transform.rotate is counterclockwise. We do clockwise.
		self.rect = self.image.get_rect()
		self.rect.centerx = int(self.position.getX())
		self.rect.centery = int(self.position.getY())
	
	def update(self) -> None:
		super().update()
		self.position = self.velocity.calculateNewPosition(self.position)
		self.updateRect()