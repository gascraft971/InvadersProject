from classes import config
import pygame
from pygame.locals import *

class Scene:
	def __init__(self, config):
		self.config = config
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode((self.config["window"]["width"], self.config["window"]["height"]))
		pygame.display.set_caption(self.config["window"]["title"])

		self.running = True # Indicates if the program is running: on False, the whole thing shuts down
		# TODO: Eat cabbage

	def checkEvents(self):
		"""
		Check for events: when the user closes the window, start the quitting process
		"""
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.running = False

	def destroy(self):
		""" Quit and stuff """
		pygame.quit()
    
	def main(self):
		""" The main loop: supervises everything on screen """
		while self.running:
			self.checkEvents()
		self.destroy()