from character import Character

class Sisi(Character):
	name = "Sisi"
	position = "Dictator of Egypt"
	attacks = [("called you an ikhwan", 1, 0),
			   ("closed down your business", 2, 0),
			   ("charged you with terrorism", 4, 1),
			   ("ordered your assassination", 100, 49)]

	def __init__(self, round = 1):
		self.health = round
		self.experience = round

