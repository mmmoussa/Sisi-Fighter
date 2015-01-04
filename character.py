import random

class Character():
	name = "Mr. Evil"
	position = "Ruler of the Universe"

	# attacks consists of a list of tuples. Each tuple holds the attack, its power, and the number to be used in the attack success randomizer
	attacks = [("destroyed the universe", 100, 49), ("used his doomsday laser", 2, 1)]

	def __init__(self):
		self.health = random.randint(10, 20)
		self.experience = random.randint(20, 50)

	def __str__(self):
		return "{}, {}, {}HP and {}XP".format(self.name, self.position, self.health, self.experience)

	def attack(self):
		attack = random.randint(0, len(self.attacks) - 1)
		probabilityNum = random.randint(0, self.attacks[attack][2])
		if probabilityNum == 0:
			print("{} {}!".format(self.name, self.attacks[attack][0]))
			return self.attacks[attack][1]
		else:
			print("{} would've {}, but the plan failed.".format(self.name, self.attacks[attack][0]))
			return 0


