'''Create player objects and control their hands'''
class Player:

	def __init__(self, name):
		'''Intialize a players hand. It should only be 2 cards'''
		self.name = name
		self.hand = []
		self.money = 100.00 # For implenting betting later
		self.fold = False

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
		for card in range(0,2):
			print(f'      {self.hand[card]}')
		print('+-------------------+\n')

	def bet_money(self):
		'''Ask player for bet amount and test it against players purse
		Retun amount and pass it to Table.print_pot'''
		if self.fold == True:
			return 0

		while self.fold == False:
			bet = input(f"How much would you like to bet?\nYou have ${self.money}.\nBet: $")
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
		for player in player_list:
			self.fold = False

	def evaluate_hand(self, comprehensive_hand):
		'''Assign a point value to cards
		We could add all cards to a list as values, and check for repeated numbers
		ex - All 2's = 2, all 3's = 3 then check for number of instances
		of the number in the players hand'''
		hand_strength = 0
		three_of_a_kind_base = 30
		four_of_a_kind_base = 40
		combo = comprehensive_hand
		for card in combo:
			card_split = card.split()
			if card_split[0] == 'Ace':
				card_split[0] = 14
			elif card_split[0] == 'King':
				card_split[0] = 13
			elif card_split[0] == 'Queen':
				card_split[0] = 12
			elif card_split[0] == 'Jack':
				card_split[0] = 11
			try:
				card_split[0] = int(card_split[0])
			except ValueError:
				print("If you see this, then shit is fucked up.")
			else:
				hand_strength += card_split[0]
		print(f"Your current hand_strength is {hand_strength}")

	def comprehensive_hand(self, table_cards):
		'''Combines the players hand with the cards on the table into
		a single list'''
		combo = []
		for card in table_cards:
			combo.append(card)

		for card in self.hand:
			combo.append(card)

		return combo

