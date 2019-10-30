'''Table object'''
from players import Player
from random import randint

class Table:
	def __init__(self):
		self.players = 0
		self.cards = []
		self.pot = 0

	def ask_for_players(self):
		'''Ask for a number, convert to int, then return that number to pass
		to the create_players() function.'''
		while self.players == 0 or self.players > 7:
			number_of_players = input('How many players would you like to play with? (1-7) ')
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
		for card in cards_to_table:
			self.cards.append(card)

	def print_table(self):
		print('+----- TABLE -----+')
		for card in range(0, len(self.cards)):
			print(self.cards[card])
		print('+-----------------+\n')

	def print_pot(self, list_of_players, player_bet=0):
		'''Take all bets and print pot to console
		----- TO DO -----
		Build seperate function that gets passed bot hand strength and bets
		based on "confidence in your hand" '''
		bet_to_pot = 0
		for player in list_of_players:
			bot_bet = randint(1,5)
			print(f'{player.name.title()} bet ${bot_bet}')
			bet_to_pot += bot_bet
		self.pot += player_bet + bet_to_pot
		print(f"The current table pot is ${self.pot}")

	def reset_pot(self):
		self.pot = 0

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
