import random

class BoggleDice:

    def __init__(self, dice_string):
        self.values = dice_string

    def roll(self):
        value = random.choice(self.values)
        if value == "Q":
            value = "Qu"
        return value