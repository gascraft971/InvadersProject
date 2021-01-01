import pygame
import sys
from pygame.locals import *
from classes import Level, GameLevel

class Scene:
	def __init__(self, config) -> None:
		self.config = config
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode((self.config["window"]["width"], self.config["window"]["height"]))
		pygame.display.set_caption(self.config["window"]["title"])

		self.running = True # Indicates if the program is running: on False, the whole thing shuts down

	def checkEvents(self) -> None:
		"""
		Check for events: when the user closes the window, start the quitting process
		"""
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.running = False
			else:
				pygame.event.post(event) # Without this line, this would clear the event queue. Not good. We don't want that yet.
	
	def initControllers(self):
		self.joysticks = []
		print("Initiating controllers...")
		print("Found {} controllers".format(pygame.joystick.get_count()))

		for joystickIndex in range(pygame.joystick.get_count()):
			self.joysticks.append(pygame.joystick.Joystick(joystickIndex))
			self.joysticks[joystickIndex].init()
			print("Added controller {} to list".format(joystickIndex))

	def destroy(self) -> None:
		""" Quit and stuff """
		print("Quitting pygame. Bye!")
		pygame.quit()
		sys.exit(0)
    
	def main(self) -> None:
		""" The main loop: supervises everything on screen """
		self.initControllers()
		self.level = GameLevel.GameLevel(self.config, self)
		while self.running:
			self.checkEvents()
			self.level.update()
			self.display.blit(self.level.getSurface(), (0, 0))
			pygame.display.update()
			pygame.display.flip()
		self.destroy()