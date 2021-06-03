import random


import random

class BoggleDice:

    def __init__(self, dice_string):
        self.values = dice_string


    def roll(self):
        return random.choice(self.values)