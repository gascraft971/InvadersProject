from classes import Player

class PlayerData:
	def __init__(self, num: int, name: str, player: Player) -> None:
		self.playerNumber = num
		self.name = name
		self.player = player