class P:
	"""
	A position class to store and calculate the position of an entity
	The x position and the y position are stored as floats and encapsulated
	"""
	def __init__(self, x: int = 0, y: int = 0):
		self.x = float(x)
		self.y = float(y)
	
	def setX(self, x: int):
		self.x = float(x)
	
	def setY(self, y: int):
		self.y = float(y)
	
	def getX(self) -> float:
		return self.x
	
	def getY(self) -> float:
		return self.y