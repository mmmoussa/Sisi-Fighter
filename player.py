import random
import sys
from tkinter import *
import tkinter.messagebox
from character import Character

class Player(Character):
	name = "Mohamed"
	attacks = [("assassinate the enemy", 10, 5),
			   ("protest", 3, 60),
			   ("spread the truth", 1, 80),
			   ("rest", -2, 90)]

	def __init__(self):
		self.health = 10

	def __str__(self):
		return "{}, {}HP".format(self.name, self.health)

	def attack(self, label):
		message = "It is your turn to attack. You can:\n"
		count = 1
		for attack in self.attacks:
			message += ("    {}. {}\n".format(count, attack[0].title()))
			count += 1
		label.config(text=message)
		while True:
			try:
				choice = int(input("Choose the attack by number: "))
				try:
					throwaway = self.attacks[choice - 1]
					break
				except:
					tkinter.messagebox.showinfo("Invalid choice", "There is no attack for that number.")
			except KeyboardInterrupt:
				print("\n\nProgram interrupted.\n")
				sys.exit()
			except:
				tkinter.messagebox.showinfo("Invalid choice", "That choice wasn't valid.")

		message="You are choosing to {}.\n".format(self.attacks[choice - 1][0])
		failNum = random.randint(0, 99)
		if self.attacks[choice - 1][2] > failNum:
			message += "Your attack succeeded!"
			label.config(text=message)	
			return self.attacks[choice - 1][1]
		else:
			message += "Your attack failed."
			label.config(text=message)	
			return 0	

