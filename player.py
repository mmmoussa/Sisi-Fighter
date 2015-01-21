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
		self.turns = 0
		self.choice = 1

	def __str__(self):
		return "{}, {}HP".format(self.name, self.health)

	def listAttacks(self, label, frame):
		message = "It is your turn to attack. You can:\n"
		label.config(text=message)
		count = 1
		self.radioChoice = IntVar()
		self.radioButtonsList = []
		for attack in self.attacks:
			b = Radiobutton(frame, text=attack[0].title(), variable=self.radioChoice, value=count)
			b.pack(side=TOP, anchor=W, padx=10)
			self.radioButtonsList.append(b)
			count += 1

		if self.turns == 0:
			self.radioChoice.set(1)
		else:
			self.radioChoice.set(self.choice)
		self.turns += 1
		
	def attackResult(self, label):
		for item in self.radioButtonsList:
			item.pack_forget()

		self.choice = self.radioChoice.get()

		message="You are choosing to {}.\n".format(self.attacks[self.choice - 1][0])
		failNum = random.randint(0, 99)
		if self.attacks[self.choice - 1][2] > failNum:
			message += "Your attack succeeded!"
			label.config(text=message)	
			return self.attacks[self.choice - 1][1]
		else:
			message += "Your attack failed."
			label.config(text=message)	
			return 0
		
		

