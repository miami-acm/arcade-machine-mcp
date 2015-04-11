class Game(object):
	def __init__(self, name, command, image):
		self.name = name
		self.command = command
		self.image = image

	def __str__(self):
		return "'{}' '{}' '{}'".format(self.name, self.command, self.image)

	def __repr__(self):
		return 'Game: {}'.format(self.name)
