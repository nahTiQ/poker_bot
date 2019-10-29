from random import shuffle,choice

from players import Player 
class Deck:
	'''Controlling the deck for poker'''
	def __init__(self):
		self.cards = ['Ace-Clubs', 'King-Clubs', 'Queen-Clubs', 'Jack-Clubs', '10-Clubs', '9-Clubs',
					'8-Clubs', '7-Clubs', '6-Clubs', '5-Clubs', '4-Clubs', '3-Clubs', '2-Clubs',
					'Ace-Spades', 'King-Spades', 'Queen-Spades', 'Jack-Spades', '10-Spades', 
					'9-Spades', '8-Spades', '7-Spades', '6-Spades', '5-Spades', '4-Spades', '3-Spades',
					'4-Spades', '3-Spades', '2-Spades', 'Ace-Hearts', 'King-Hearts', 'Queen-Hearts',
					'Jack-Hearts', '10-Hearts', '9-Hearts', '8-Hearts', '7-Hearts', '6-Hearts', 
					'5-Hearts', '4-Hearts', '3-Hearts', '2-Hearts', 'Ace-Diamonds', 'King-Diamonds',
					'Queen-Diamonds', 'Jack-Diamonds', '10-Diamonds', '9-Diamonds', '8-Diamonds', 
					'7-Diamonds', '6-Diamonds', '5-Diamonds', '4-Diamonds', '3-Diamonds', '2-Diamonds'  ]
		self.discard = []


	def shuffle(self):
		# Code for shuffling the deck
		shuffle(self.cards)

	def deal_to_players(self, list_of_players):
		self.list_of_players = list_of_players
		''' Deal cards from the deck to all of the players hands
		Must be passed a list of player objects '''

		# Code for dealing cards
		# All players get 2 cards
		# Remove cards from the list with .pop() when they're dealt so they can't be dealt twice
		# Deal to player_1 first
		# Deal to the rest of the players
		for player in self.list_of_players:
			while len(player.hand) < 2:
				player.hand.append(self.cards.pop(0))
		

				

	def deal_flop(self):
		'''Deal 3 cards to the table'''
		'''Burn card then deal 3'''

	def deal_turn(self):
		'''Deal the 4th card to the table'''
		'''Burn card then deal 1'''
		print('')

	def deal_river(self):
		'''Burn card then deal the river'''
		print('')

	def rebuild_deck(self):
		''' Reset the deck back to it's original state'''
		self.cards = ['Ace-Clubs', 'King-Clubs', 'Queen-Clubs', 'Jack-Clubs', '10-Clubs', '9-Clubs',
					'8-Clubs', '7-Clubs', '6-Clubs', '5-Clubs', '4-Clubs', '3-Clubs', '2-Clubs',
					'Ace-Spades', 'King-Spades', 'Queen-Spades', 'Jack-Spades', '10-Spades', 
					'9-Spades', '8-Spades', '7-Spades', '6-Spades', '5-Spades', '4-Spades', '3-Spades',
					'4-Spades', '3-Spades', '2-Spades', 'Ace-Hearts', 'King-Hearts', 'Queen-Hearts',
					'Jack-Hearts', '10-Hearts', '9-Hearts', '8-Hearts', '7-Hearts', '6-Hearts', 
					'5-Hearts', '4-Hearts', '3-Hearts', '2-Hearts', 'Ace-Diamonds', 'King-Diamonds',
					'Queen-Diamonds', 'Jack-Diamonds', '10-Diamonds', '9-Diamonds', '8-Diamonds', 
					'7-Diamonds', '6-Diamonds', '5-Diamonds', '4-Diamonds', '3-Diamonds', '2-Diamonds'  ]

	def print_deck(self):
		'''Print cards left in the deck. This is mainly for troubleshooting purposes.'''
		for card in self.cards:
			print(card)
		print(f' There are {len(self.cards)} cards left in the deck')