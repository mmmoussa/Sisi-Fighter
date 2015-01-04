import random
from character import Character

class Player(Character):
	attacks = [("assassinate the enemy", 10, 19),
			   ("protest", 3, 1),
			   ("spread the truth", 1, 0),
			   ("rest", -2, 0)]

	def __init__(self):
		self.name = input("Your name: ")
		self.health = 15

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
			except:
				print("That choice wasn't valid.\n")

		print("\nYou are choosing to {}".format(self.attacks[choice - 1][0]))
		failNum = random.randint(0, self.attacks[choice - 1][2])
		if failNum == 0:
			print("Your attack succeeded!")
			return self.attacks[choice - 1][1]
		else:
			print("Your attack failed.")
			return 0		

