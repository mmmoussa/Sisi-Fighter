from character import Character

class Sisi(Character):
	name = "Sisi"
	position = "Dictator of Egypt"
	attacks = [("called you an ikhwan", 1, 95),
			   ("closed down your business", 2, 80),
			   ("charged you with terrorism", 4, 50),
			   ("ordered your assassination", 20, 3)]

	def __init__(self, round = 1):
		self.health = round
		self.experience = round

