from random import choice

from deck import *
from players import *
from table import Table

# Names for CPU opponents
list_of_player_names = ['Player_2', 'Player_3', 'Player_4', 'Player_5', 'Player_6', 'Player_7', 'Player_8' ]

# idk where to put this, so it's going here
# Creates player variables, tho
def create_players(number_of_players):
	number_of_players = int(number_of_players)
	for number in range(0, number_of_players):
		player_list.append(Player(list_of_player_names[number]))

# Names for CPU opponents
list_of_player_names = ['Player_2', 'Player_3', 'Player_4', 'Player_5', 'Player_6', 'Player_7', 'Player_8' ]
player_list = []

# Create the table
table = Table()

# Create the deck
deck = Deck()
help(deck)
# Print banner
print('---------------------------------------------')
print('|                                           |')
print("|                  Klon3d's                 |")
print("|              Poker Simulator              |")
print('|                                           |')
print('|                                           |')
print('---------------------------------------------')

# Create players
Player(Player.create_player())

number_of_players = input("How many players would you like to play with? (1-7) ")

table.players_at_table(number_of_players)
create_players(number_of_players)

''' Test to check players hands 
for item in list_of_player_names:
	try:
		print(f'{item.name.title()} has {item.hand} in his hand')
	except AttributeError:
		pass
'''
print('Shuffling cards...')
shuffle(deck.cards)

print('Dealing cards...')
deck.deal_to_players(player_list)

for player in player_list:
	print(f"{player.name}'s hand: {player.hand}")
