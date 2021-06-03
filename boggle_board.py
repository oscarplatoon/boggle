import string
import random
import re


class BoggleBoard:
  
  # Step 1
  def __init__(self, start_board=None, blank_dice=None):
    self.start_board = (("_") * 4 + f'\n') * 4 
    self.blank_dice = 'Ready to Roll!' + f'\n' + (("_") * 4 + f'\n') * 4

  # def first_shake(self):

  
  # def shake(self):

# clear_board = BoggleBoard()
# print(isinstance(clear_board, BoggleBoard)) # clearboard is instance of BoggleBoard
# print(clear_board.start_board)
# print(clear_board.blank_dice)



# PseudoCode
# instance of shake modifies the board with random uppercase letters
# regex random char?
