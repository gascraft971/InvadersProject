from classes.Ship import Ship
import pygame
from pygame.locals import *
from classes import Entity, Player

class Missile(Entity.Entity):
	def __init__(self, config, ship: Ship):
		super().__init__(config)
		self.ship = ship
		self.originalImage = pygame.transform.scale(pygame.image.load(self.config["sprites"]["missiles"]["regular"]["nopulse"]).convert_alpha(), (int(32 * 1), int(62 * 1)))
		self.image = self.originalImage
		self.position = P.P(self.ship.position.getX(), self.ship.position.getY())
		self.rotation = self.ship.rotation
		# We need to reload the rectangle for our changes to the image take effect
		self.updateRect() # There we go
		print("Initialised 1 missile")