'''Table object'''
from players import Player

class Table:
	def __init__(self):
		self.players = 0
		self.cards = []

	def ask_for_players(self):
		'''Ask for a number, convert to int, then return that number to pass
		to the create_players() function.'''
		while self.players == 0 or self.players > 7:
			number_of_players = input('How many players would you like to play with? (1-7)')
			try:
				number_of_players = int(number_of_players)
			except ValueError:
				print("You must enter a number between 1 and 7.")
			else:
				if number_of_players > 7:
					print("You must enter a number between 1 and 7.")
					continue
				else:
					return number_of_players
					break
			
	def accept_cards(self, cards_to_table):
		''' Accept cards from another function to be added to the table'''
		self.cards.append(cards_to_table)

	# def players_at_table(self, number):
		'''Check if user is trying to add more than 7 players to the table'''
	





		'''try:
			number = int(number)
		except ValueError:
			print("You must enter a number!")
		else:
			while number > 7:
				number = int(number)
				print("You can not play with more than 7 other people.")
				number = int(input("How many people would you like to play with? (1-7)"))'''
