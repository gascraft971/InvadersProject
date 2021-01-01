import pygame
from pygame.locals import *
from classes import Ship, P, V

class Player(Ship.Ship):
	def __init__(self, config) -> None:
		super().__init__(config)
		# Here we load the image, scale it to 40 % of its original size and the set is as our image
		self.originalImage = pygame.transform.scale(pygame.image.load(self.config["sprites"]["players"]["squadron_leader"]).convert_alpha(), (int(293 * 0.2), int(226 * 0.2)))
		self.image = self.originalImage
		self.position = P.P(50, 400)
		self.rotation = 90
		# We need to reload the rectangle for our changes to the image take effect
		self.updateRect() # There we go
		print("Initialised 1 player")
	
	def event(self, eventType: str) -> None: # TODO: Stop the player from leaving the screen by too far (maybe destroy or tp him?)
		if eventType == "MOVE_RIGHT":
			if self.velocity.getX() < self.config["physics"]["speed"]["max_reactor_speed"]:
				self.velocity.addX(self.config["physics"]["speed"]["reactor_boost"])
				self.rotation = 90
		elif eventType == "MOVE_LEFT":
			if self.velocity.getX() > -self.config["physics"]["speed"]["max_reactor_speed"]:
				self.velocity.addX(-self.config["physics"]["speed"]["reactor_boost"])
				self.rotation = 270
		elif eventType == "MOVE_DOWN":
			if self.velocity.getY() < self.config["physics"]["speed"]["max_thruster_speed"]:
				self.velocity.addY(self.config["physics"]["speed"]["thruster_boost"])
		elif eventType == "MOVE_UP":
			if self.velocity.getY() > -self.config["physics"]["speed"]["max_thruster_speed"]:
				self.velocity.addY(-self.config["physics"]["speed"]["thruster_boost"])
		

