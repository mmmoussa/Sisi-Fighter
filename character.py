import random
from tkinter import *

class Character():
	name = "Mr. Evil"
	position = "Ruler of the Universe"

	# attacks consists of a list of tuples. Each tuple holds the attack, its power, and the probability of success

	def __init__(self):
		self.health = random.randint(10, 20)
		self.experience = random.randint(20, 50)

	def __str__(self):
		return "{}, {}, {}HP and {}XP".format(self.name, self.position, self.health, self.experience)

	def attack(self, label):
		attack = random.randint(0, len(self.attacks) - 1)
		probabilityNum = random.randint(0, 99)
		if self.attacks[attack][2] > probabilityNum:
			label.config(text="It is {}'s turn to attack:\n{} {}!".format(self.name, self.name, self.attacks[attack][0]))
			return self.attacks[attack][1]
		else:
			label.config(text="It is {}'s turn to attack:\n{} would've {}, but the plan failed.".format(self.name, self.name, self.attacks[attack][0]))
			return 0


