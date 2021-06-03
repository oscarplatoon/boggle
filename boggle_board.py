import random
import string

class BoggleBoard:
  #init a boggle matrix 4 x 4
  #with shake method print out random letters
  #import random
  #Each row will be 4 elements long/ call on 4 times

  def __init__(self, size):
    self.size = 4
    #self.board =

  #%s to add letters? or f string
  def drawBoard(randomLetters):
    print(f'{randomLetters}, {randomLetters}, {randomLetters}, {randomLetters}')
    print(f'{randomLetters}, {randomLetters}, {randomLetters}, {randomLetters}')
    print(f'{randomLetters}, {randomLetters}, {randomLetters}, {randomLetters}')
    print(f'{randomLetters}, {randomLetters}, {randomLetters}, {randomLetters}')

  #Generate random letters
  def randomLetters(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

  
  #variable with input to shake board
  def shake(self):
    self.shake = input('Shake Board?: ')
    #Logic to call on __init__
