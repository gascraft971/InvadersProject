import pygame, uuid
from pygame.locals import *
from classes import P, V

class Entity(pygame.sprite.Sprite):
	def __init__(self, config, scene) -> None:
		super().__init__()
		self.scene = scene
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
		if self.position.getX() > self.config["window"]["width"]:
			self.position.setX(self.config["window"]["width"])
			self.velocity.setX(0)
		elif self.position.getX() < 0:
			self.position.setX(0)
			self.velocity.setX(0)
		if self.position.getY() > self.config["window"]["height"]:
			self.position.setY(self.config["window"]["height"])
			self.velocity.setY(0)
		elif self.position.getY() < 0:
			self.position.setY(0)
			self.velocity.setY(0)
		self.updateRect()