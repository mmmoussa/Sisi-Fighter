import sys

from sisi import Sisi
from player import Player

class EgyptGame():
	round = 1

	def setup(self):
		print("\n"+"="*80)
		print("Welcome to Sisi Fighter!")
		print("This game is made in support of a free and democratic Egypt.")
		print("The goal of the game is simple: defeat Sisi before he defeats you!")
		print("="*80+"\n\n")

		self.player = Player()
		print("\n")
		self.enemies = [Sisi(1), Sisi(2), Sisi(3), Sisi(4), Sisi(5), Sisi(6), Sisi(7), Sisi(8), Sisi(9), Sisi(10)]
		self.enemy = self.getEnemy()

	def getEnemy(self):
		try:
			return self.enemies.pop(0)
		except:
			return None

	def playerTurn(self):
		damage = self.player.attack()
		if damage != -2:
			self.enemy.health -= damage
		else:
			self.player.health += 2
		if self.enemy.health < 0:
			self.enemy.health = 0

	def enemyTurn(self):
		damage = self.enemy.attack()
		self.player.health -= damage
		if self.player.health < 0:
			self.player.health = 0

	def roundEnd(self):
		self.round += 1
		self.player.health += self.enemy.experience
		print("Good job! You defeated Sisi!".format(self.enemy))
		print("="*80+"\n\n")
		self.enemy = self.getEnemy()
		if self.enemy == None:
			pass
		else:
			print("="*80)
			print("You're not finished yet! Incoming {}!".format(self.enemy))
			print("="*80+"\n\n")

	def __init__(self):
		self.setup()

		while self.player.health > 0 and (self.enemy):
			print("="*80)
			print("Battle {}: {} vs. {}".format(self.round, self.player, self.enemy))
			print("-"*80)
			print("{}'s turn:".format(self.player.name))
			self.playerTurn()
			print("-"*80)
			if self.enemy.health == 0:
				self.roundEnd()
				continue
			else:
				print("{}'s turn:".format(self.enemy.name))
				self.enemyTurn()
				print("-"*80)
				print("Round results:")
				print("{} has {}HP".format(self.player.name, self.player.health))
				print("{} has {}HP".format(self.enemy.name, self.enemy.health))
				print("="*80+"\n\n")

		if self.player.health == 0:
			print("Oh no! Sisi defeated you! How unfortunate! Better luck next time!\n")
		else:
			print("Congratulations! You defeated Sisi and liberated Egypt!\n")


EgyptGame()
