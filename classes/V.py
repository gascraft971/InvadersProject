from classes import P

class V:
	""" A velocity class to store and calculate the velocity of an entity. Data is stored as floats. """
	def __init__(self, xVel = 0.0, yVel = 0.0) -> None:
		self.xVel = float(xVel)
		self.yVel = float(yVel)
	
	def setX(self, xVel) -> None:
		self.xVel = float(xVel)
	
	def setY(self, yVel) -> None:
		self.yVel = float(yVel)
	
	def addX(self, xVel) -> None:
		self.xVel += float(xVel)
	
	def addY(self, yVel) -> None:
		self.yVel += float(yVel)
	
	def getX(self) -> float:
		return self.xVel
	
	def getY(self) -> float:
		return self.yVel

	def calculateNewPosition(self, position: P.P) -> P.P:
		x = position.getX()
		y = position.getY()
		x += self.xVel
		y += self.yVel
		return P.P(x, y)
