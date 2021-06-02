import random
import string

class BoggleBoard:
  
  def __init__(self):
    self.board = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
    print(f"{self.board[0]}{self.board[1]}{self.board[2]}{self.board[3]}\n{self.board[4]}{self.board[5]}{self.board[6]}{self.board[7]}\n{self.board[8]}{self.board[9]}{self.board[10]}{self.board[11]}\n{self.board[12]}{self.board[13]}{self.board[14]}{self.board[15]}")
    print("Hit Enter to shake!")
  
  def shake(self):
    print(self.board)
    for x in range(len(self.board)) :
      self.board[x] = random.choice(string.ascii_letters)    
      print(self.board[x])
      print(self.board)
    
boggler = BoggleBoard()
boggler.shake()
