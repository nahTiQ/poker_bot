from random import shuffle,choice

from players import Player 
import console as c

class Deck:
	'''Controlling the deck for poker'''
	def __init__(self):
		self.card_values = {
				'Ace Hearts' : 1,
				'King Hearts' : 2,
				'Queen Hearts' : 3,
				'Jack Hearts' : 4,
				'10 Hearts' : 5,
				'9 Hearts' : 6,
				'8 Hearts' : 7,
				'7 Hearts' : 8,
				'6 Hearts' : 9,
				'5 Hearts' : 10,
				'4 Hearts' : 11,
				'3 Hearts' : 12,
				'2 Hearts' : 13,
				'Ace Spades' : 14,
				'King Spades' : 15,
				'Queen Spades' : 16,
				'Jack Spades' : 17,
				'10 Spades' : 18,
				'9 Spades' : 19,
				'8 Spades' : 20,
				'7 Spades' : 21,
				'6 Spades' : 22,
				'5 Spades' : 23,
				'4 Spades' : 24,
				'3 Spades' : 25,
				'2 Spades' : 26,
				'Ace Diamonds' : 27,
				'King Diamonds' : 28,
				'Queen Diamonds' : 29,
				'Jack Diamonds' : 30,
				'10 Diamonds' : 31,
				'9 Diamonds' : 32,
				'8 Diamonds' : 33,
				'7 Diamonds' : 34,
				'6 Diamonds' : 35,
				'5 Diamonds' : 36,
				'4 Diamonds' : 37,
				'3 Diamonds' : 38,
				'2 Diamonds' : 39,
				'Ace Clubs' : 40,
				'King Clubs' : 41,
				'Queen Clubs' : 42,
				'Jack Clubs' : 43,
				'10 Clubs' : 44,
				'9 Clubs' : 45,
				'8 Clubs' : 46,
				'7 Clubs' : 47,
				'6 Clubs' : 48,
				'5 Clubs' : 49,
				'4 Clubs' : 50,
				'3 Clubs' : 51,
				'2 Clubs' : 52,
				}
		# NOTE: Srsly bro? Srsly?


		# Should be named card_keys, but I'm not renaming it everywhere
		self.cards = ['Ace Clubs', 'King Clubs', 'Queen Clubs', 'Jack Clubs', '10 Clubs', '9 Clubs',
					'8 Clubs', '7 Clubs', '6 Clubs', '5 Clubs', '4 Clubs', '3 Clubs', '2 Clubs',
					'Ace Spades', 'King Spades', 'Queen Spades', 'Jack Spades', '10 Spades', 
					'9 Spades', '8 Spades', '7 Spades', '6 Spades', '5 Spades', '4 Spades', '3 Spades',
					'4 Spades', '3 Spades', '2 Spades', 'Ace Hearts', 'King Hearts', 'Queen Hearts',
					'Jack Hearts', '10 Hearts', '9 Hearts', '8 Hearts', '7 Hearts', '6 Hearts', 
					'5 Hearts', '4 Hearts', '3 Hearts', '2 Hearts', 'Ace Diamonds', 'King Diamonds',
					'Queen Diamonds', 'Jack Diamonds', '10 Diamonds', '9 Diamonds', '8 Diamonds', 
					'7 Diamonds', '6 Diamonds', '5 Diamonds', '4 Diamonds', '3 Diamonds', '2 Diamonds']

		self.discard = []


	def shuffle(self):
		# Code for shuffling the deck
		shuffle(self.cards)

	def discard_card(self):
		self.discard.append(self.cards.pop(0))

	def deal_to_players(self, list_of_players):
		''' Deal cards from the deck to all of the players hands
		Must be passed a list of player objects '''

		# Code for dealing cards
		# All players get 2 cards
		# Remove cards from the list with .pop() when they're dealt so they can't be dealt twice
		# Deal to player_1 first
		# Deal to the rest of the players
		for player in list_of_players:
			while len(player.hand) < 2:
				player.hand.append(self.cards.pop(0))

	def deal_flop(self):
		'''Discard a card and deal 3 cards to the table'''
		Deck.discard_card(self)
		cards_to_table = []

		for card in range(0,3):
			cards_to_table.append(self.cards.pop(card))
		return cards_to_table        

	def deal_turn(self):
		'''Deal the 4th card to the table'''
		'''Burn card then deal 1'''

		cards_to_table = []
		Deck.discard_card(self)
		cards_to_table.append(self.cards.pop(0))
		return cards_to_table 

	def deal_river(self):
		'''Burn card then deal the last card to the table'''
		cards_to_table = []
		Deck.discard_card(self)
		cards_to_table.append(self.cards.pop(0))
		return cards_to_table

	def print_discard(self):
		for card in self.discard:
			print(card)


	def reset_deck(self):
		''' Reset the deck back to it's original state'''
		self.cards = ['Ace Clubs', 'King Clubs', 'Queen Clubs', 'Jack Clubs', '10 Clubs', '9 Clubs',
					'8 Clubs', '7 Clubs', '6 Clubs', '5 Clubs', '4 Clubs', '3 Clubs', '2 Clubs',
					'Ace Spades', 'King Spades', 'Queen Spades', 'Jack Spades', '10 Spades', 
					'9 Spades', '8 Spades', '7 Spades', '6 Spades', '5 Spades', '4 Spades', '3 Spades',
					'4 Spades', '3 Spades', '2 Spades', 'Ace Hearts', 'King Hearts', 'Queen Hearts',
					'Jack Hearts', '10 Hearts', '9 Hearts', '8 Hearts', '7 Hearts', '6 Hearts', 
					'5 Hearts', '4 Hearts', '3 Hearts', '2 Hearts', 'Ace Diamonds', 'King Diamonds',
					'Queen Diamonds', 'Jack Diamonds', '10 Diamonds', '9 Diamonds', '8 Diamonds', 
					'7 Diamonds', '6 Diamonds', '5 Diamonds', '4 Diamonds', '3 Diamonds', '2 Diamonds']
		Deck.reset_discard(self)

	def reset_discard(self):
		self.discard = []



	def print_deck(self):
		'''Print cards left in the deck. This is mainly for troubleshooting purposes.'''
		for card in self.cards:
			print(card)
		print(f' There are {len(self.cards)} cards left in the deck')