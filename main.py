from random import choice


from deck import *
from players import *
from table import Table

# Names for CPU opponents
# list_of_player_names = ['Player_2', 'Player_3', 'Player_4', 'Player_5', 'Player_6', 'Player_7', 'Player_8' ]
list_of_player_names = ['Chase', 'Jon', 'Kale', 'Ron', 'Ashley', 'Ty', 'Tina']

# idk where to put this, so it's going here
# Creates player variables, tho

''' ----- TO DO -----
Add more names and pass choice() to randomly grab player names
choice() currently grabs the first letter of each name for some reason
'''

def create_players(number_of_players):
	number_of_players = int(number_of_players)
	for number in range(0, number_of_players):
		player_list.append(Player((list_of_player_names[number])))

def play_more(keep_playing):
	'''Pass Table.play_again to this. If false, active = False'''
	if keep_playing == True:
		active = True
		return active

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

# Begin play loop
active = True
while active == True:
	print('Shuffling cards...')
	deck.shuffle()

	print('Dealing cards...\n')
	deck.deal_to_players(player_list)

# Player should see his hand here
	player_1.print_hand()
	player_1.evaluate_hand(player_1.comprehensive_hand(table.cards))
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the flop...\n")
	table.accept_cards(deck.deal_flop())
	player_1.print_hand()
	table.print_table()
	player_1.evaluate_hand(table.cards)
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the turn...\n")
	table.accept_cards(deck.deal_turn())
	player_1.print_hand()
	table.print_table()
	player_1.evaluate_hand(table.cards)
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the river...\n")
	table.accept_cards(deck.deal_river())
	player_1.print_hand()
	table.print_table()
	player_1.evaluate_hand(table.cards)
	table.print_pot(player_list, player_1.bet_money())

	print(f'These cards were discarded during the game: ')
	deck.print_discard()

	active = play_more(table.play_again())
	if active == True:
		print('\n+---------- NEW ROUND ----------+\n')
	player_1.reset_players(player_list)
	deck.reset_deck()
	table.reset_table()




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

''' ----- PLAYER HAND TEST -----
	Test to check players hands 

	for item in list_of_player_names:
	try:
		print(f'{item.name.title()} has {item.hand} in his hand')
	except AttributeError:
		pass
'''