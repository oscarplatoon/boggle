import random

class BoggleBoard:

	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	length = 4

	def __init__(self, custom_length = None):
		# allow user to add custom length
		if custom_length is not None:
			self.length = custom_length
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
		# loop through our board and assign a random alphabet character
		for i, _ in enumerate(self.board):
			self.board[i] = random.choice(self.alphabet)
		self.print_board()

	
