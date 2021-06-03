import random
import time

class BoggleBoard:
  flag = True   #flag to exit main loop (only false with input "q")
  dice =[
    ['A ','A ','E ','E ','G ','N '],['E ','L ','R ','T ','T ','Y '],
    ['A ','O ','O ','T ','T ','W '],['A ','B ','B ','J ','O ','O '],
    ['E ','H ','R ','T ','V ','W '],['C ','I ','M ','O ','T ','U '],
    ['D ','I ','S ','T ','T ','Y '],['E ','I ','O ','S ','S ','T '],
    ['D ','E ','L ','R ','V ','Y '],['A ','C ','H ','O ','P ','S '],
    ['H ','I ','M ','N ','Qu','U '],['E ','E ','I ','N ','S ','U '],
    ['E ','E ','G ','H ','N ','W '],['A ','F ','F ','K ','P ','S '],
    ['H ','L ','N ','N ','R ','Z '],['D ','E ','I ','L ','R ','X ']
    ]
  
  
  
  def __init__(self):
    self.board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
    self.show_board()
    while self.flag == True:
      self.ask_response()


  def shake(self):
    self.count = 0
    self.pointer = list(range(0,16))
    random.shuffle(self.pointer)
    for row in range(0,4):
      for space in range(0,4):
        self.board[row][space] = self.dice[self.pointer[self.count]][random.randint(0,5)]
        self.count += 1
    self.show_board()
    

  def show_board(self):
    print(f'\nBoggle Board\n')
    for row in range(0,4):
      output = ''
      for space in range(0,4):
        output += (self.board[row][space]) + ' '
      print(f'{output}')
    print(f'\n')

  def ask_response(self):
    self.response = input('Enter "s" to shake\nEnter "t" to shake and start timer\nEnter "q" to quit: ')
    if self.response == 's':
      self.shake()
    elif self.response == 't':
      self.shake()
      self.start_timer()
    elif self.response != 'q':
      print(f'\nInvalid response\n')
    else:
      self.flag = False

  def start_timer(self):
    self.t = 10
    while self.t > 0:
      print(f'\r{divmod(self.t,60)}', end ='\r')
      self.t -= 1
      time.sleep(1)
    print(f'\n\n\n\nTIMES UP!!!!\n')

game = BoggleBoard()



