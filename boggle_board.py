from hashlib import new
import string, random

class BoggleBoard:
  def __init__(self):
    self.board = '----\n'*4
    print(self.board)

  def shake(self):
    new_board = []
    for item in range(16):
      item = random.choice(string.ascii_letters).upper()
      if item == "Q":
        new_board.append("Qu")
      else:
        new_board.append(item)
      if len(new_board) == 4:
        a = ''.join(new_board[0:2])
        b = ''.join(new_board[2:4])
        print(a + b)
        new_board = []
      

board = BoggleBoard()
board.shake()


