class Game(object):
	def __init__(self, name, command, image, id_num):
		self.name = name
		self.command = command
		self.image = image
		self.id_num = id_num

	def __str__(self):
		return "'{}' '{}' '{}' '{}'".format(
			self.name,
			self.command,
			self.image,
			self.id_num,
		)

	def __repr__(self):
		return 'Game: {}'.format(self.name)
