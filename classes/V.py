from classes import P

class V:
	""" A velocity class to store and calculate the velocity of an entity """
	def __init__(self, xVel = 0, yVel = 0):
		self.xVel = xVel
		self.yVel = yVel
	
	def setX(self, xVel: int):
		self.xVel = xVel
	
	def setY(self, yVel: int):
		self.yVel = yVel
	
	def calculateNewPosition(self, position: P) -> P:
		pass # TODO: Add this function that calculates a new position based on a P object
