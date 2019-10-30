'''Create player objects and control their hands'''
class Player:
	def __init__(self, name):
		'''Intialize a players hand. It should only be 2 cards'''
		self.name = name
		self.hand = []
		self.money = 100.00 # For implenting betting later

	def create_player():
		player = input("What is your poker handle? ")
		with open('player.txt', 'r') as player_file:
			if player in player_file:
				print(f"Welcome back to the table, {player}!")
			else:
				with open('player.txt', 'w') as player_file:
					player_file.write(player)
				print(f"Welcome to the table, {player}")
		return player

	def add_player_to_list():
		print('')

	def bet_money(self):
		while True:
			bet = input(f"How much would you like to bet? \nYou currently have ${self.money}\nBet: ")
			try:
				bet = float(bet)
			except ValueError:
				print(f"You can not bet words!\n")
				bet = input(f"How much would you like to bet?\nYou have ${self.money}.\nBet: ")
			else:
				if bet > self.money:
					print(f"You do not have enough to bet ${bet}.\n")
					continue
				else:
					self.money -= bet
					print(f"You have ${self.money} left.")
					return bet
					break

	def evaluate_hand(self, table_cards):
		print('You currently have {FEATURE COMING SOON}')

