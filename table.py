'''Table object'''
from players import Player
class Table:
	def __init__(self):
		self.players = []
		self.cards= []

	def players_at_table(self, number):
		'''Create player objects based on number of players at the table'''
		number = int(number)
		while number > 7:
			number = int(number)
			print("You can not play with more than 7 other people.")
			number = int(input("How many people would you like to play with? (1-7)"))