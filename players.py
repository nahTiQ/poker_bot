'''Create player objects and control their hands'''
class Player:
	def __init__(self, name):
		'''Intialize a players hand. It should only be 2 cards'''
		self.name = name
		self.hand = []
		self.money = 100 # For implenting betting later

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
