import pygame
import collections
from pygame.locals import *
from classes import Level, Entity, Ship, PlayerData, Scene, Player

class GameLevel(Level.Level):
	def __init__(self, config, scene: Scene) -> None:
		super().__init__(config, scene)
		self.bgImage = pygame.Surface((1, 1)) # TODO: Replace with an actual cool image
		self.surface = pygame.transform.scale(self.bgImage, (self.config["window"]["width"], self.config["window"]["height"]))
		self.players = collections.OrderedDict()
		self.players[0] = PlayerData.PlayerData(0, "Gascraft2")

		self.spawnShips()
	
	def spawnShips(self) -> None: # TODO: Finish
		for _ in range(1):
			entity = Player.Player(self.config)
			self.entities.add(entity)
		
	def checkInput(self, player: dict) -> None: # TODO: Finish
		""" Check if there has been any input from the players """
		events = pygame.event.get()
		bindings = self.config["keymaps"][str(player.playerNumber)]

		for event in events:
			if event.type == KEYDOWN:
				for key in bindings.values():
					if globals()[key] == event.key:
						pass

			if event.type == JOYAXISMOTION and event.__dict__["joy"] is player.playerNumber:
				if event.__dict__["axis"] == 0:
					if round(event.__dict__["value"]) == 1:
						print("Saw RIGHT")
					elif round(event.__dict__["value"]) == -1:
						print("Saw LEFT")
				elif event.__dict__["axis"] == 1:
					if round(event.__dict__["value"]) == 1:
						print("Saw DOWN")
					elif round(event.__dict__["value"]) == -1:
						print("Saw UP")
			
			if event.type == JOYBUTTONDOWN and event.__dict__["joy"] is player.playerNumber:
				if event.__dict__["button"] is 0:
					print("Button X pressed")
				if event.__dict__["button"] is 1:
					print("Button A pressed")
				if event.__dict__["button"] is 2:
					print("Button B pressed")
				if event.__dict__["button"] is 3:
					print("Button Y pressed")

	def update(self) -> None:
		""" The logic that runs every frame """
		# The part that checks for user input
		for player in self.players.values():
			self.checkInput(player)
		self.entities.draw(self.surface)