from random import choice

from deck import *
from players import Player
from table import Table

# idk where to put this, so it's going here
# Creates player variables, tho
def create_players(number_of_players):
	number_of_players = int(number_of_players)
	for number in range(0, number_of_players):
		list_of_player_names[number] = Player(list_of_player_names[number])

# List of CPU opponents
list_of_player_names = ['Player_2', 'Player_3', 'Player_4', 'Player_5', 'Player_6', 'Player_7', 'Player_8' ]

# Create the table
table = Table()
number_of_players = input("How many players would you like to play with? (1-7) ")

table.players_at_table(number_of_players)
create_players(number_of_players)
for item in list_of_player_names:
	try:
		print(f'{item.name.title()} has {item.hand} in his hand')
	except AttributeError:
		pass