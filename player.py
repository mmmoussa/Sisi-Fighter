import random
import sys
from character import Character

class Player(Character):
	attacks = [("assassinate the enemy", 10, 5),
			   ("protest", 3, 60),
			   ("spread the truth", 1, 80),
			   ("rest", -2, 90)]

	def __init__(self):
		try:
			self.name = input("Your name: ")
		except KeyboardInterrupt:
			print("Program interrupted.\n")
			sys.exit()
		self.health = 10

	def __str__(self):
		return "{}, {}HP".format(self.name, self.health)

	def attack(self):
		print("It is your turn to attack. You can:")
		count = 1
		for attack in self.attacks:
			print("  {}. {}".format(count, attack[0].title()))
			count += 1
		while True:
			try:
				choice = int(input("Choose the attack by number: "))
				try:
					throwaway = self.attacks[choice - 1]
					break
				except:
					print("There is no attack for that number.\n")
			except KeyboardInterrupt:
				print("Program interrupted.\n")
				sys.exit()
			except:
				print("That choice wasn't valid.\n")

		print("\nYou are choosing to {}".format(self.attacks[choice - 1][0]))
		failNum = random.randint(0, 99)
		if self.attacks[choice - 1][2] > failNum:
			print("Your attack succeeded!")
			return self.attacks[choice - 1][1]
		else:
			print("Your attack failed.")
			return 0		

