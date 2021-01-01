from classes import P

class V:
	""" A velocity class to store and calculate the velocity of an entity """
	def __init__(self, xVel = 0, yVel = 0) -> None:
		self.xVel = xVel
		self.yVel = yVel
	
	def setX(self, xVel: int) -> None:
		self.xVel = xVel
	
	def setY(self, yVel: int) -> None:
		self.yVel = yVel
	
	# TODO: Add getY and getY functions for getting the current value of xVel and yVel

	def calculateNewPosition(self, position: P) -> P:
		pass # TODO: Add this function that calculates a new position based on a P object
