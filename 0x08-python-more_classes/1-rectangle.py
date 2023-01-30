class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def width(self):
		return self.width

	@width.setter
	def width(self, value):
		self.width = value

	def height(self, value):
		self.height = value
		return self.height	
	
