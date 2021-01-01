import pygame
import time
from pygame.locals import *
from classes import Level, PlayerData, Scene, Player

class GameLevel(Level.Level):
	def __init__(self, config, scene: Scene) -> None:
		super().__init__(config, scene)
		self.bgImage = pygame.Surface((1, 1)) # TODO: Replace with an actual cool image
		self.originalSurface = pygame.transform.scale(self.bgImage, (self.config["window"]["width"], self.config["window"]["height"]))
		self.surface = self.originalSurface.copy()
		self.players = []

		self.spawnShips()
	
	def spawnShips(self) -> None: # TODO: Finish
		for playerIndex in range(1):
			player = Player.Player(self.config)
			self.players.append(PlayerData.PlayerData(playerIndex, "P{}".format(playerIndex), player))
			self.entities.add(player)
		
	def checkInput(self, player: dict) -> None: # TODO: Finish
		""" Check if there has been any input from the players """
		events = pygame.event.get()
		bindings = self.config["keymaps"][str(player.playerNumber)]

		for event in events:
			if event.type == KEYDOWN:
				for key in bindings.values():
					if globals()[key] == event.key:
						pass
			
			if event.type == JOYBUTTONDOWN and event.__dict__["joy"] is player.playerNumber:
				if event.__dict__["button"] is 0:
					player.player.event("BTN_X")
				if event.__dict__["button"] is 1:
					print("Button A pressed")
				if event.__dict__["button"] is 2:
					print("Button B pressed")
				if event.__dict__["button"] is 3:
					print("Button Y pressed")
		
		js = self.scene.joysticks[player.playerNumber]
		print("Axis X: ", js.get_axis(0), " - Axis Y: ", js.get_axis(1))
		if js.get_axis(0) != 0 or js.get_axis(1) != 0: # The controller is being pressed!
			eventName = "NONE"
			if js.get_axis(0) != 0:
				if round(js.get_axis(0)) == 1:
					eventName = "MOVE_RIGHT"
				elif round(js.get_axis(0)) == -1:
					eventName = "MOVE_LEFT"
			elif js.get_axis(1) != 0:
				if round(js.get_axis(1)) == 1:
					eventName = "MOVE_DOWN"
				elif round(js.get_axis(1)) == -1:
					eventName = "MOVE_UP"
			
			player.player.event(eventName)

	def update(self) -> None:
		""" The logic that runs every frame """
		# The part that checks for user input
		self.surface = self.originalSurface.copy()
		for player in self.players:
			self.checkInput(player)
			player.player.update()
		self.entities.draw(self.surface)