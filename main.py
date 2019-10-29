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

# List for player objects
player_list = []

# Create the table
table = Table()

# Create the deck
deck = Deck()

# Print banner
print('---------------------------------------------')
print('|                                           |')
print("|                 nameless                  |")
print("|              Poker Simulator              |")
print('|                                           |')
print('|                                           |')
print('---------------------------------------------')

# Create player
player_1 = Player(Player.create_player())
player_list.insert(0, player_1) # Put player_1 at the front of list of players so he's dealt cards first

# Ask for number of CPU opponents
number_of_players = table.ask_for_players()

# Create CPU opponents

create_players(number_of_players)

''' ----- PLAYER HAND TEST -----
	Test to check players hands 

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

# Player should see his hand here
print(player_1.hand)

print("Dealing the flop...")
table.accept_cards(deck.deal_flop())
print(table.cards)

print("Dealing the turn...")
table.accept_cards(deck.deal_turn())
print(table.cards)

print("Dealing the river...")
table.accept_cards(deck.deal_river())
print(table.cards)

''' ---- TEST FOR DUPLICATE CARDS -----
	Test for duplicates between players hands
	and whats left in the deck. If this returns
	true, then dealing is not working properly 

for player in player_list:
	for hand in player.hand:
		if hand in deck.cards:
			test = True 
		else:
			test = False
print(test)
'''