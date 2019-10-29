'''Table object'''
from players import Player

class Table:
	def __init__(self):
		self.players = []
		self.cards = []

	def players_at_table(self, number):
		'''Check if user is trying to add more than 7 players to the table'''
		try:
			number = int(number)
		except ValueError:
			print("You must enter a number!")
		else:
			while number > 7:
				number = int(number)
				print("You can not play with more than 7 other people.")
				number = int(input("How many people would you like to play with? (1-7)"))
