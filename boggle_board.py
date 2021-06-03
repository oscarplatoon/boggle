import random

class BoggleBoard:

	# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	length = 4

	def __init__(self, dice_list, custom_length = None, random_seed = None):
		
		# allow user to add custom length
		if custom_length is not None:
			self.length = custom_length

		# dice list size MUST match size of board
		assert(len(dice_list) == self.length ** 2)

		if random_seed is not None:
			self.randon_seed = random_seed

		self.dice_list = dice_list

		# initialize board with underscores
		self.board = ["_" for _ in range(self.length ** 2)]
		self.print_board()

	def print_board(self):
		for i, x in enumerate(self.board):
			print(x, end="")
			# add a newline for every row
			if (i + 1) % self.length == 0:
				print("\n", end="")

		print("\n", end="")

	def shake(self):
		# randomize dice shuffle
		random.shuffle(self.dice_list)

		# loop through our board and assign a random alphabet character
		for i, _ in enumerate(self.board):
			self.board[i] = self.dice_list[i].roll()

		# print board
		self.print_board()

		return self.board