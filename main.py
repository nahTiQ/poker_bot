from random import choice


from deck import *
from hand_hierarchy import *
from players import *
# Note: Any table methods not acting on an object need a Table. prefix
from table import Table
# Note: Any console methods need a c. prefix
import console as c


# Names for CPU opponents
# list_of_player_names = ['Player_2', 'Player_3', 'Player_4', 'Player_5', 'Player_6', 'Player_7', 'Player_8' ]
player_names = ['Chase', 'Jon', 'Kale', 'Ron', 'Ashley', 'Ty', 'Tina']

# idk where to put this, so it's going here
# Creates player variables, tho

''' ----- TO DO -----
Add more names and pass choice() to randomly grab player names
choice() currently grabs the first letter of each name for some reason
'''

def create_players(number_of_players):
	number_of_players = int(number_of_players)
	for number in range(0, number_of_players):
		player_list.append(Player((player_names[number])))

def play_more(keep_playing):
	'''Pass Table.play_again to this. If false, active = False'''
	if keep_playing == True:
		active = True
		return active

def check_all_players_hands(players):
	'''pass player list to this to evaluate all hands'''
	for player in players:
		player.set_hand_score(evaluate_hand(player.comprehensive_hand(table.cards)))


# List for player objects
player_list = []

# Create the table
table = Table()

# Create the deck
deck = Deck()

# Print banner
c.print_banner()

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
	print(f'Shuffling {len(deck.cards)} cards...')
	deck.shuffle()

	print('Dealing cards...\n')
	deck.deal_to_players(player_list)

# Player should see his hand here
	player_1.print_hand()
	c.printc(get_card_values(player_1.hand))
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the flop...\n")
	table.accept_cards(deck.deal_flop())
	player_1.print_hand()
	table.print_table()
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the turn...\n")
	table.accept_cards(deck.deal_turn())
	player_1.print_hand()
	table.print_table()
	table.print_pot(player_list, player_1.bet_money())

	print("Dealing the river...\n")
	table.accept_cards(deck.deal_river())
	player_1.print_hand()
	table.print_table()
	table.print_pot(player_list, player_1.bet_money())


	check_all_players_hands(player_list)
	winner = check_winner(player_list)
	print(f'{winner.name} has won the round and takes the table pot of ${table.pot}!\n')
	print(f'{winner.name} won the game with:\n{winner.print_formatted_hand(winner.comprehensive_hand(table.cards))}')


	active = play_more(table.play_again())
	if active == True:
		print('\n+---------- NEW ROUND ----------+\n')
		print('Resetting the board...')
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