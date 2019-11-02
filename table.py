'''Table object'''
from random import randint

from players import Player
import console as c

class Table:
	def __init__(self):
		self.players = 0
		self.cards = []
		self.pot_round = 0
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
		'''Prints the table cards to the console'''
		print('+----- TABLE -----+')
		for card in self.cards:
			print(card)
		print('+-----------------+\n')

	def print_pot(self, players, player_bet):
		'''Take all bets and print pot to console
		----- TO DO -----
		Build seperate function that gets passed bot hand strength and bets
		based on "confidence in your hand" '''
		bot_bet = 0
		self.pot_round = 0
		print('\n+----- PLAYER BETS -----+')
		for player in players:
			if player == players[0]:
				bot_bet = 0
			else:
				bot_bet = randint(1,5)
			if player == players[0]:
				print(f"   {player.name} bet ${player_bet}")
			else:
				print(f'   {player.name.title()} bet ${bot_bet}')
			self.pot_round += bot_bet
		self.pot += player_bet + self.pot_round
		print(f"The current table pot is ${self.pot}")
		print('+----- END BETS -----+\n')

	def reset_table(self):
		self.pot = 0
		self.cards = []

	def play_again(play_bool):
		keep_playing = ''
		while keep_playing != 'y' and keep_playing != 'n':
			keep_playing = input("Whould you like to play again? (y/n)")
			if keep_playing.lower() == 'y':
				return True
			elif keep_playing.lower() == 'n':
				return False
			elif keep_playing != 'y' and keep_playing != 'n':
				print("You must select (Y) or (N)o")
				continue

	def who_wins(self, handstrengths):
		'''Give a dictionary of hand strengths?'''

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
