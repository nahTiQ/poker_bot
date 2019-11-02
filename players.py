'''Create player objects and control their hands'''
import console as c

class Player:

	def __init__(self, name):
		'''Intialize a players hand. It should only be 2 cards'''
		self.name = name
		self.hand = []
		self.money = 100.00 # For implenting betting later
		self.fold = False
		self.score = 0

	def create_player():
		player = input("What is your poker handle? ")
		with open('player.txt', 'r') as player_file:
			if player in player_file:
				print(f"Welcome back to the table, {player}!")
			else:
				with open('player.txt', 'w') as player_file:
					player_file.write(player)
				print(f"Welcome to the table, {player}!")
		return player

	def print_hand(self):
		print('+-----YOUR HAND-----+')
		for card in self.hand:
			print(f'      {card}')
		print('+-------------------+\n')

	def bet_money(self):
		'''Ask player for bet amount and test it against players purse
		Retun amount and pass it to Table.print_pot'''
		if self.fold == True:
			return 0

		while self.fold == False:
			bet_message = f"How much would you like to bet? You have ${self.money}\n"
			bet_message += "You can type 'fold' or enter 0 to check\nBet: $"
			bet = input(bet_message)
			if bet.lower() == 'check' or bet == None:
				print(f'You check')
				return 0
				break
			elif bet.lower() == 'fold':
				print('You have folded your hand. =(')
				self.fold = True
				return 0
			else:
				try:
					bet = int(bet)
				except ValueError:
					print("You can not bet words!")
				else:
					if bet == 0 or bet == None:
						print('You check')
						return 0
					self.money -= bet
					print('')
					return bet

	def reset_players(self, player_list):
		'''Reset self values of the player for a new game'''
		for player in player_list:
			self.fold = False
			self.hand_score = 0

	def comprehensive_hand(self, table_cards):
		'''Combines the players hand with the cards on the table into
		a single list'''
		combo = []
		for card in table_cards:
			combo.append(card)

		for card in self.hand:
			combo.append(card)

		return combo

	def print_formatted_hand(self, comprehensive_hand):
		'''Print a formatted LINE of cards'''
		cards = ''
		for card in comprehensive_hand:
			cards += f"{card} "
		return cards

	def set_hand_score(self, value):
		'''Set the players hand score'''
		self.score = value


		''' THE FOLLOWING CODE CHECKS FOR CARD SEQUENCES...
			HOPEFULLY '''
