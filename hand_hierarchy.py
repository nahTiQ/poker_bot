'''Checks hands for pairs, straights, flushes, etc
Contains functions for evulating the players hand
'''

import console as c
from deck import Deck
import table

deck = Deck()
''''			'Ace Hearts' : 1,
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
				'2 Clubs' : 52,'''

''' Get hand values, pass them to function that contains card combos and returns a value'''

def get_card_values(cards):
		'''Return a list of unique values for each individual card. Pass this
		any list of cards and retun their card values in the dictionary'''
		unique_card_numbers = []
		for card in cards:
			if card in deck.card_values:
				unique_card_numbers.append(deck.card_values[card])
		return unique_card_numbers

def evaluate_hand(card_values):
	'''Check both the players hand with the cards on the table for card sequences
	This is the mother of methods. You get this shit right and you're a fucking
	animal
	evaluate_hand(get_card_values(player.comprehensive_hand(table)))) should return straight, flush, pair etc

	This should probably loop through all players
	'''
	if [1, 14] or [1, 27] or [1, 40] or [14, 27] or [14, 40] or [27, 40] in card_values:
		ace_pair = 28
		return ace_pair
	elif [2, 15] or [2, 28] or [2, 41] or [15, 28] or [15, 41] or [28, 41] in card_values:
		king_pair = 27
		return king_pair
	elif [3, 16] or [3, 29] or [3, 42] or [16, 29] or [16, 42] or [29, 42] in card_values:
		queen_pair = 26
		return queen_pair
	elif [4, 17] or [4, 30] or [4, 43] or [17, 30] or [17, 43] or [30, 43] in card_values:
		jack_pair = 25
		return jack_pair
	elif [5, 18] or [5, 31] or [5, 44] or [18, 31] or [18, 44] or [31, 44] in card_values:
		ten_pair = 24
		return ten_pair
	elif [6, 19] or [6, 32] or [6, 45] or [19, 32] or [19, 45] or [32, 45] in card_values:
		nine_pair = 23
		return nine_pair
	elif [7, 20] or [7, 33] or [7, 46] or [20, 33] or [20, 46] or [33, 46] in card_values:
		eight_pair = 22
		return eight_pair
	elif [8, 21] or [8, 34] or [8, 47] or [21, 34] or [21, 47] or [34, 47] in card_values:
		seven_pair = 21
		return seven_pair
	elif [9, 22] or [9, 35] or [9, 48] or [22, 35] or [22, 48] or [35, 48] in card_values:
		six_pair = 20
		return six_pair
	elif [10, 23] or [10, 36] or [10, 49] or [23, 36] or [23, 49] or [36, 49] in card_values:
		five_pair = 19
		return five_pair
	elif [11, 24] or [11, 37] or [11, 50] or [24, 37] or [24, 50] or [37, 50] in card_values:
		four_pair = 18
		return four_pair
	elif [12, 25] or [12, 38] or [12, 51] or [25, 38] or [25, 51] or [38, 51] in card_values:
		three_pair = 17
		return three_pair
	elif [13, 26] or [13, 39] or [13, 52] or [26, 39] or [26, 52] or [39, 52] in card_values:
		two_pair = 16
		return two_pair

	if [1,2,3,4,5] or [14,15,16,17,18] or [27,28,29,30,31] or [40,41,42,43,44] in card_values:
		royal_flush = 999999
		return royal_flush


def check_winner(players):
	'''Pass this a list of players at the end of the game. The player with the
	highest player.score attribute wins!'''
	# ----- TO DO -----
	# CHECK FOR TIE
	score = 0
	name = ''
	while True:
		for player in players:
			if player.fold == False and player.score > score:
				score = player.score
				name = player.name
		return player


	

