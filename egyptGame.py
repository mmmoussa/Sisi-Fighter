import sys
import os

from sisi import Sisi
from player import Player

class EgyptGame():
	round = 1
	gameEnded = False

	def setup(self, label):
		label.config(text="Welcome to Sisi Fighter!\nThis game is made in support of a free and democratic Egypt.\nThe goal of the game is simple: defeat Sisi before he defeats you!")

		self.player = Player()
		self.enemies = [Sisi(1), Sisi(2), Sisi(3), Sisi(4), Sisi(5), Sisi(6), Sisi(7), Sisi(8), Sisi(9), Sisi(10)]
		self.enemy = self.getEnemy()

	def getEnemy(self):
		try:
			return self.enemies.pop(0)
		except:
			return None

	def playerTurn(self, label):
		damage = self.player.attack(label)
		if damage != -2:
			self.enemy.health -= damage
		else:
			self.player.health += 2
		if self.enemy.health < 0:
			self.enemy.health = 0

	def enemyTurn(self, label):
		damage = self.enemy.attack(label)
		self.player.health -= damage
		if self.player.health < 0:
			self.player.health = 0

	def roundEnd(self, label):
		self.player.health += self.enemy.experience
		label.config(text="Good job! You defeated {} #{}!".format(self.enemy.name, self.round))
	
	def newEnemy(self, label):
		self.enemy = self.getEnemy()
		if self.enemy == None:
			label.config(text="It seems there are no more {}s".format(self.enemy.name))
			self.gameEnded = True
		else:
			label.config(text="You're not finished yet! Incoming {}!".format(self.enemy))
			self.round += 1

	def __init__(self):
		'''
		while self.player.health > 0 and (self.enemy):
			print("Battle {}: {} vs. {}".format(self.round, self.player, self.enemy))
			print("{}'s turn:".format(self.player.name))
			self.playerTurn()
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
				print("="*80)
		'''

