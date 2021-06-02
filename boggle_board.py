import random

class BoggleBoard:
  
  def __init__(self):
    self.board = ['_'] * 16
    self.dice_roll = [
      'AAEEGN',
      'ELRTTY',
      'AOOTTW',
      'ABBJOO',
      'EHRTVW',
      'CIMOTU',
      'DISTTY',
      'EIOSST',
      'DELRVY',
      'ACHOPS',
      'HIMNQU',
      'EEINSU',
      'EEGHNW',
      'AFFKPS',
      'HLNNRZ',
      'DEILRX'
      ]

  def board_view(self):
    print (self.board)
    
  def make_board(self):
    for i in range(0, len(self.board), 4):
      #going up by 4
      print(''.join(self.board [i:i + 4]))
  
  def shake(self):
    # used random.shuffle to randomize what letter you may get
    random.shuffle(self.dice_roll)
    # used to find the i in each die 
    for i in range(0, len(self.board)):
      abc_index = random.randint(0, 5)
      #replaces the number from the list to the matching letter from the list
      letter = self.dice_roll[i][abc_index]
      if letter == "Q":
        letter = "Qu"
      #replaces the '_' from self.board with the actual letter from the list
      self.board[i] = letter
      
      
new = BoggleBoard()
new.shake()
new.make_board()