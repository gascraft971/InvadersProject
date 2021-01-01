import pygame
from pygame.locals import *
from classes import Ship

class Player(Ship.Ship):
	def __init__(self, config):
		super().__init__(config)
		# Here we load the image, scale it to 40 % of its original size and the set is as our image
		self.image = pygame.transform.scale(pygame.image.load(self.config["sprites"]["players"]["squadron_leader"]).convert_alpha(), (117, 90))
		# We need to reload the rectangle for our changes to the image take effect
		self.updateRect() # There we go
		print("Initialised 1 player")
