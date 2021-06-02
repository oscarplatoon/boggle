import random
#import string
import csv

class BoggleBoard:
  
  def __init__(self):
    self.board = []
    self.dice = []

    with open('boggle.csv') as csv_file:
      reader = csv.reader(csv_file)
      for row in reader:
        self.dice += row

  # part 1
  # def shake(self):
  #     for i in range(16):
  #       self.board.append(random.choice(string.ascii_uppercase))
  #     for n in range(0, len(self.board), 4):
  #       print(self.board[n:n+4])

  #part 2
  def new_board(self):
    for n in range(0, len(self.board), 4):
      print(self.board[n:n+4])

  def shake(self):
    for i in range(len(self.dice)):
      roll = random.randint(0,5)
      self.board.append(self.dice[i][roll])
    self.board = [i.replace('Q', 'Qu') for i in self.board]

    return self.board


b = BoggleBoard()
b.shake()
b.new_board()