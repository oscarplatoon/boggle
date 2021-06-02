import random
import string
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./data/dice.csv")

class BoggleBoard:
  
  def __init__(self):
    self.theboard = ['-'] * 16
    self.thedice = ['-'] * 16

  def simple_shake(self):
    
    for i, obj in enumerate (self.theboard):
      self.theboard[i] = chr(random.randint(65,90))
      # print (self.theboard)

  def shake(self):
    with open(path) as csv_file:
      csv_reader = csv.reader(csv_file)
      for i, row in enumerate(csv_reader):
        position = random.randint(0,15)
        success = False
        while success == False:
          if self.thedice[position] == '-':
            self.thedice[position] = (row[0][random.randint(0,5)])
            success = True
          else:
            position = random.randint(0,15)



        # while self.thedice[position] != '-':

          print(self.thedice)
        
        