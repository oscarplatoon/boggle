import string
import random

class BoggleBoard:

  dice = ['AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW','CIMOTU','DISTTY','EIOSST','DELRVY','ACHOPS','HIMNQU','EEINSU','EEGHNW','AFFKPS','HLNNRZ','DEILRX']
  
  def __init__(self):
    self.letter_str = ''
    self.letter_list = []
      # print('____')
      # print('____')
      # print('____')
      # print('____')

  def shake(self):
    for index, die in enumerate(self.dice):
      self.random_letter = (random.choice(self.dice[index]))
      if self.random_letter == 'Q':
        self.letter_str += 'Qu '
        self.letter_list.append('Qu')
      else:
        self.letter_str += (self.random_letter + '  ')
        self.letter_list.append(self.random_letter)

    print(self.letter_str[0:12])
    print(self.letter_str[12:24])
    print(self.letter_str[24:36])
    print(self.letter_str[36:])

  def view_board(self):
    print(self.letter_str[0:12])
    print(self.letter_str[12:24])
    print(self.letter_str[24:36])
    print(self.letter_str[36:])

  # +1 right -1 left +4 under -4 over +5 down right +3 down left -3 up right -5 up left 
  # 0 1 2 3 4 7 8 11 12 15 indexes that need to be checked
  def include_word(self, word):
    self.word = word.upper()
    self.checked_indecies = [0, 1, 2, 3, 4, 7, 8, 11, 12, 15]
    for i, letter in enumerate(self.letter_list):
      if i in self.checked_indecies and letter == self.word[0]:
        if self.word[1] == self.letter_list[i+1]:
          if self.word[2] == self.letter_list[i+2]:
            if self.word[3] == self.letter_list[i+3]:
              return True
        
      else:
        return False      
        

    

    

newgame = BoggleBoard()
newgame = 
print(newgame.letter_str)
newgame.include_word('test')