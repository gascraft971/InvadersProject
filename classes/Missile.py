from classes.Ship import Ship
import pygame
from pygame.locals import *
from classes import Entity, Ship, P, V

class Missile(Entity.Entity):
	def __init__(self, config, scene, ship: Ship):
		super().__init__(config, scene)
		self.ship = ship
		self.originalImage = pygame.transform.scale(pygame.image.load(self.config["sprites"]["missiles"]["regular"]["nopulse"]).convert_alpha(), (int(32 * 0.3), int(62 * 0.3)))
		self.image = self.originalImage
		self.position = P.P(self.ship.position.getX(), self.ship.position.getY())
		self.velocity = V.V(self.config["physics"]["speed"]["max_reactor_speed"])
		self.rotation = self.ship.rotation
		# We need to reload the rectangle for our changes to the image take effect
		self.updateRect() # There we go
		print("Initialised 1 missile")