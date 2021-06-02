import random
import string
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./data/dice.csv")

class BoggleBoard:
  
  def __init__(self):
    self.board = ['-'] * 16
    self.dice = []

    # import the dice
    with open(path) as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.dice += row

  def __str__(self):
    output = ""
    elem_count = 0
    for elem in self.board:
        if elem == 'Q':
          output += 'Qu'+ " "
        else:
          output += elem + "  "
          
        elem_count += 1
        if elem_count == 4:
          output += "\n"
          elem_count = 0

    return output

  def shake(self):
    for elem_index in range(len(self.board)):
      self.board[elem_index] = random.choice(string.ascii_letters).upper()

  # def shake2(self)
myBoard = BoggleBoard()
myBoard.shake()
print(myBoard)